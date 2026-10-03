package util;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public final class GitWorktreeResolver {
    private static final String WORKTREE_ROOT_NAME = ".enre-worktrees";
    private static final int SHORT_COMMIT_LENGTH = 12;

    private GitWorktreeResolver() {}

    public static String resolve(String repositoryPath, String gitRef) throws IOException, InterruptedException {
        if (gitRef == null || gitRef.isBlank()) {
            return repositoryPath;
        }

        Path repository = Paths.get(repositoryPath).toAbsolutePath().normalize();
        if (!Files.exists(repository)) {
            throw new FileNotFoundException("Input path does not exist: " + repository);
        }
        if (!Files.isDirectory(repository)) {
            throw new IOException("Input path is not a directory: " + repository);
        }

        Path repositoryRoot = resolveRepositoryRoot(repository);
        String commit = resolveCommit(repositoryRoot, gitRef);
        String shortCommit = commit.substring(0, Math.min(SHORT_COMMIT_LENGTH, commit.length()));
        Path worktreePath = buildWorktreePath(repositoryRoot, gitRef, shortCommit);

        if (Files.exists(worktreePath)) {
            verifyExistingWorktree(worktreePath, commit);
            System.out.println("Reusing Git worktree: " + worktreePath);
            return worktreePath.toFile().getCanonicalPath();
        }

        Files.createDirectories(worktreePath.getParent());
        GitResult addResult = runGit(repositoryRoot, "worktree", "add", "--detach", worktreePath.toString(), commit);
        if (!addResult.isSuccess()) {
            throw new IOException("Failed to create Git worktree at " + worktreePath
                    + "\nCommand: " + addResult.commandText()
                    + "\nOutput: " + addResult.output);
        }

        verifyExistingWorktree(worktreePath, commit);
        System.out.println("Created Git worktree: " + worktreePath);
        return worktreePath.toFile().getCanonicalPath();
    }

    private static Path resolveRepositoryRoot(Path repository) throws IOException, InterruptedException {
        GitResult result = runGit(repository, "rev-parse", "--show-toplevel");
        if (!result.isSuccess() || result.output.isBlank()) {
            throw new IOException("Git ref analysis requires a Git repository: " + repository
                    + "\nCommand: " + result.commandText()
                    + "\nOutput: " + result.output);
        }
        return Paths.get(result.output.trim()).toAbsolutePath().normalize();
    }

    private static String resolveCommit(Path repositoryRoot, String gitRef) throws IOException, InterruptedException {
        GitResult result = runGit(repositoryRoot, "rev-parse", "--verify", gitRef + "^{commit}");
        if (!result.isSuccess() || result.output.isBlank()) {
            throw new IOException("Git ref not found: " + gitRef
                    + "\nRun `git fetch --tags` in " + repositoryRoot + " if the ref is missing locally."
                    + "\nCommand: " + result.commandText()
                    + "\nOutput: " + result.output);
        }
        return result.output.trim();
    }

    private static Path buildWorktreePath(Path repositoryRoot, String gitRef, String shortCommit) {
        Path parent = repositoryRoot.getParent();
        Path worktreeRoot = parent == null
                ? repositoryRoot.resolve(WORKTREE_ROOT_NAME)
                : parent.resolve(WORKTREE_ROOT_NAME);
        String repositoryName = repositoryRoot.getFileName().toString();
        String safeRef = sanitizeForPath(gitRef);
        return worktreeRoot.resolve(repositoryName + "__" + safeRef + "__" + shortCommit);
    }

    private static String sanitizeForPath(String value) {
        String safe = value.replaceAll("[^A-Za-z0-9._-]", "_");
        return safe.isBlank() ? "ref" : safe;
    }

    private static void verifyExistingWorktree(Path worktreePath, String expectedCommit)
            throws IOException, InterruptedException {
        GitResult result = runGit(worktreePath, "rev-parse", "HEAD");
        if (!result.isSuccess() || result.output.isBlank()) {
            throw new IOException("Worktree path exists but is not a valid Git worktree: " + worktreePath
                    + "\nCommand: " + result.commandText()
                    + "\nOutput: " + result.output);
        }

        String actualCommit = result.output.trim();
        if (!expectedCommit.equalsIgnoreCase(actualCommit)) {
            throw new IOException("Worktree path exists but points to a different commit: " + worktreePath
                    + "\nExpected: " + expectedCommit
                    + "\nActual: " + actualCommit);
        }
    }

    private static GitResult runGit(Path workingDirectory, String... args) throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add("git");
        command.add("-C");
        command.add(workingDirectory.toString());
        command.addAll(Arrays.asList(args));

        ProcessBuilder processBuilder = new ProcessBuilder(command);
        processBuilder.redirectErrorStream(true);
        Process process = processBuilder.start();
        String output = new String(process.getInputStream().readAllBytes(), StandardCharsets.UTF_8).trim();
        int exitCode = process.waitFor();
        return new GitResult(command, exitCode, output);
    }

    private static class GitResult {
        private final List<String> command;
        private final int exitCode;
        private final String output;

        private GitResult(List<String> command, int exitCode, String output) {
            this.command = command;
            this.exitCode = exitCode;
            this.output = output;
        }

        private boolean isSuccess() {
            return exitCode == 0;
        }

        private String commandText() {
            return String.join(" ", command);
        }
    }
}
