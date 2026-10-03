import cdt.CrossModuleIncludeAnalysis;
import cdt.TemplateWork;
import util.Configure;

import java.nio.file.Path;

public class Main {

	/**
	 * @methodsName: main
	 * @description: main function
	 */
	public static void main(String[] args) throws Exception {
		//
		if (args.length == 0) {
			args = new String[] {
					"/path/to/repository",
					"example-project",
					"-o=/path/to/enre-output",
					"-r=v1.0.0"
			};
		}

		//
		TemplateWork templateWork = new TemplateWork();
		templateWork.execute(args);

		//
		Configure configure = Configure.getConfigureInstance();
		String crossModulePath = configure.getCrossModulePath();

		//
		if (crossModulePath != null && !crossModulePath.isEmpty()) {
			System.out.println("Analyzing API usage in the specified directory.");
			String projectName = configure.getProjectName();
			String outputPath = configure.getOutputPath();
			String jsonFilePath = Path.of(outputPath, projectName + "_out.json").toString();
			String outputJsonPath = Path.of(outputPath, projectName + "-c_out.json").toString();

			CrossModuleIncludeAnalysis.analyze(jsonFilePath, crossModulePath, outputJsonPath);
		}
	}
}
