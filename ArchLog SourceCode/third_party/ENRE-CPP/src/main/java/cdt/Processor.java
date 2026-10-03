package cdt;

import entity.Entity;
import entity.EntityRepo;
import relation.Relation;
import relation.RelationContext;
import relation.RelationRepo;
import util.Configure;
import util.FileTraversal;
import util.FileUtil;
import util.JSONString;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;


public class Processor {
	static CDTParser cdtparser;
	final static String[] SUFFIX = new String[] { ".cpp", ".cc", ".c", ".c++", ".h", ".hpp", ".hh", ".cxx", ".hxx" };
	static HashMap<String,Integer> fileList;
	private static final String DEFAULT_OUTPUT_PATH = "output";
	private static final int PROGRESS_BAR_WIDTH = 30;

	public Processor(Set<String> Program_environment) {
		Processor.cdtparser = new CDTParser(Program_environment);
	}
	TypeBinding typeBinding;
	RelationContext relationcontext ;
	
	/**
	* @methodsName: parseAllFlie
	* @description: Enter the project root path, start the project analysis
	* @param:  String inputSrcPath
	* @return: void
	* @throws: 
	*/
	public static void parseAllFile(String inputSrcPath) throws Exception {
		List<String> failedFiles = new ArrayList<>();
		FileTraversal fileTrasversal = new FileTraversal(new FileTraversal.IFileVisitor() {
			int processedCount = 0;
			int totalCount = 0;

			private void initTotalCount() {
				if (totalCount == 0) {
					totalCount = countSupportedFiles(fileList);
				}
			}

			@Override
			public void visit(File file) throws Exception {
				initTotalCount();
				String fileFullPath = file.getAbsolutePath();
				fileFullPath = FileUtil.uniqFilePath(fileFullPath);
				try {
					parseFile(fileFullPath);
				} catch (Throwable throwable) {
					if (!isRecoverableParseFailure(throwable)) {
						throw throwable;
					}
					failedFiles.add(fileFullPath + "\t" + throwable.getClass().getName() + "\t" + safeMessage(throwable));
					System.err.println();
					System.err.println("WARN: failed to parse file, continuing: " + fileFullPath);
					throwable.printStackTrace(System.err);
				} finally {
					processedCount++;
					printProgress(processedCount, totalCount, fileFullPath);
				}
			}
		});
		fileTrasversal.getFileList(inputSrcPath);
		fileList = fileTrasversal.getfile();
		fileTrasversal.extensionFilter(SUFFIX);
		fileTrasversal.travers(inputSrcPath);
		System.out.println();
		writeFailedFiles(failedFiles);
		cdtparser.printMap();
	}

	private static boolean isRecoverableParseFailure(Throwable throwable) {
		return !(throwable instanceof OutOfMemoryError) && !(throwable instanceof ThreadDeath);
	}

	private static String safeMessage(Throwable throwable) {
		String message = throwable.getMessage();
		return message == null ? "" : message.replace('\n', ' ').replace('\r', ' ');
	}

	private static int countSupportedFiles(HashMap<String, Integer> files) {
		int count = 0;
		for (String filePath : files.keySet()) {
			if (isSupportedFile(filePath)) {
				count++;
			}
		}
		return count;
	}

	private static boolean isSupportedFile(String filePath) {
		String lowerPath = filePath.toLowerCase();
		for (String suffix : SUFFIX) {
			if (lowerPath.endsWith(suffix.toLowerCase())) {
				return true;
			}
		}
		return false;
	}

	private static void printProgress(int processedCount, int totalCount, String currentFile) {
		if (totalCount <= 0) {
			return;
		}
		int filled = (int) Math.round((double) processedCount * PROGRESS_BAR_WIDTH / totalCount);
		if (filled > PROGRESS_BAR_WIDTH) {
			filled = PROGRESS_BAR_WIDTH;
		}
		StringBuilder bar = new StringBuilder(PROGRESS_BAR_WIDTH);
		for (int i = 0; i < PROGRESS_BAR_WIDTH; i++) {
			bar.append(i < filled ? '=' : ' ');
		}
		int percent = (int) Math.round((double) processedCount * 100 / totalCount);
		String fileName = new File(currentFile).getName();
		System.out.print(String.format("\rProgress [%s] %d/%d %d%% %s", bar, processedCount, totalCount, percent, fileName));
		System.out.flush();
	}

	private static void writeFailedFiles(List<String> failedFiles) throws Exception {
		if (failedFiles.isEmpty()) {
			return;
		}
		File outputFolder = new File(Configure.getConfigureInstance().getOutputPath());
		if (!outputFolder.exists()) {
			outputFolder.mkdirs();
		}
		File failedFile = new File(outputFolder, Configure.getConfigureInstance().getProjectName() + "_failed_files.txt");
		try (PrintWriter writer = new PrintWriter(new FileWriter(failedFile))) {
			for (String failed : failedFiles) {
				writer.println(failed);
			}
		}
		System.err.println("WARN: " + failedFiles.size() + " files failed during parsing. See " + failedFile.getAbsolutePath());
	}
	
	/**
	* @methodsName: parseFile
	* @description: Analyze individual files
	* @param:  String inputSrcPath
	* @return: void
	* @throws: 
	*/
	public static void parseFile(String inputSrcPath) throws Exception {
		cdtparser.setFileList(fileList);
		cdtparser.parseFile(inputSrcPath);
	}
	
	
	/**
	* @methodsName: dependencyBuild
	* @description: Dependency analysis function
	* @param:  null
	* @return: void
	* @throws: 
	*/
	public void dependencyBuild() throws Exception {
		EntityRepo entityrepo = cdtparser.getEntityRepo();
		RelationRepo relationRepo = cdtparser.getRelationRepo();
		this.relationcontext = new RelationContext(entityrepo, relationRepo);
		this.relationcontext.relationListDeal();
		this.relationcontext.AggregateDeal();
		this.relationcontext.ClassDeal();
		this.relationcontext.FunctionDeal();
		this.relationcontext.NamespaceAliasDeal();
		this.relationcontext.relationListDealAfter();
	}

	public void typeBinding() throws Exception{
		EntityRepo entityrepo = cdtparser.getEntityRepo();
		this.typeBinding = new TypeBinding(entityrepo);
		this.typeBinding.typeBindingDeal();
	}

	public void outputFile(String projectName) throws Exception {
		outputFile(projectName, DEFAULT_OUTPUT_PATH);
	}

	public void outputFile(String projectName, String outputPath) throws Exception {
		EntityRepo entityrepo = cdtparser.getEntityRepo();
		JSONString node_str = new JSONString();
		//
		String outputFolder = outputPath;
		//
		File folder = new File(outputFolder);
		if (!folder.exists()) {
			folder.mkdirs();
		}
		//
		try (FileOutputStream outputStream = new FileOutputStream(new File(folder, projectName + "_out.json"))) {
			node_str.writeJsonStream(outputStream, entityrepo.getEntities(),
					this.relationcontext.getRelationRepo().getrelationrepo());
		}
	}

	public Map<Integer, Entity> getEntities(){
		return cdtparser.getEntityRepo().getEntities();
	}

	public List<Relation> getRelations(){
		return this.relationcontext.getRelationRepo().getrelationrepo();
	}

}
