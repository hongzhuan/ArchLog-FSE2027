import subprocess
from unidiff import PatchSet

SOURCE_PATTERNS = [
    "*.java",
    "*.c",
    "*.cc",
    "*.cpp",
    "*.cxx",
    "*.h",
    "*.hh",
    "*.hpp",
    "*.hxx",
]


def get_patchset_from_diff_file(git_diff_result_file):
    '''
    Extract hunks from git diff result file
    '''
    patch_set = PatchSet.from_filename(git_diff_result_file)
    return patch_set

def get_patchset_from_subshell(tag1, tag2, path):
    '''
    Extract hunks from git diff result
    '''
    cmd = [
        "git",
        "diff",
        "--ignore-blank-lines",
        "--ignore-all-space",
        "--find-renames",
        tag1,
        tag2,
        "--",
        *SOURCE_PATTERNS,
    ]
    output = subprocess.check_output(cmd, cwd=path).decode("utf-8", errors="replace")
    return PatchSet(output)

def get_commit_messages_from_subshell(tag1, tag2, path):
    '''
    Extract commit messages from git log
    '''
    cmd = ["git", "log", "--pretty=format:%s", f"{tag1}..{tag2}"]
    output = subprocess.check_output(cmd, cwd=path).decode("utf-8", errors="replace")
    return output.split('\n')
