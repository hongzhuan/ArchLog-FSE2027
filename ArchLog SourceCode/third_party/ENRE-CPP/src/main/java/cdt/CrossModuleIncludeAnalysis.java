package cdt;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

/**
 *
 */
public class CrossModuleIncludeAnalysis {

    /**
     *
     *
     *
     *
     *
     */
    public static void analyze(String jsonFilePath, String targetDirectory, String outputJsonPath) {
        try {
            //
            String jsonContent = readFile(jsonFilePath);

            //
            JSONObject jsonObject = new JSONObject(jsonContent);

            //
            JSONArray variables = jsonObject.getJSONArray("variables");
            JSONArray relations = jsonObject.getJSONArray("relations");

            //
            List<Integer> fileIds = getFileIdsInDirectory(variables, targetDirectory);

            //
            Map<Integer, List<Integer>> fileToEntitiesMap = getEntitiesGroupedByFile(variables, fileIds);

            //
            Map<Integer, Map<Integer, List<Map<String, Object>>>> structuredResults =
                    getFileBasedStructuredResults(relations, fileToEntitiesMap);

            //
            Map<Integer, Map<Integer, List<Map<String, Object>>>> filteredResults =
                    filterSameFileRelationships(structuredResults);

            //
            saveFileBasedResultsToJson(filteredResults, outputJsonPath);

            System.out.println("Cross-module analysis results saved to: " + outputJsonPath);

        } catch (IOException e) {
            System.err.println("Error reading the JSON file: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error processing the JSON: " + e.getMessage());
        }
    }

    /**
     *
     */
    private static String readFile(String filePath) throws IOException {
        StringBuilder content = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                content.append(line).append('\n');
            }
        }
        return content.toString();
    }

    /**
     *
     */
    private static List<Integer> getFileIdsInDirectory(JSONArray variables, String targetDirectory)
            throws JSONException {

        List<Integer> fileIds = new ArrayList<>();

        for (int i = 0; i < variables.length(); i++) {
            JSONObject variable = variables.getJSONObject(i);

            if ("File".equals(variable.optString("category"))) {
                String qualifiedName = variable.optString("qualifiedName");
                if (qualifiedName.startsWith(targetDirectory + "/")) {
                    fileIds.add(variable.getInt("id"));
                }
            }
        }
        return fileIds;
    }

    /**
     *
     */
    private static Map<Integer, List<Integer>> getEntitiesGroupedByFile(JSONArray variables, List<Integer> fileIds)
            throws JSONException {

        Map<Integer, List<Integer>> fileToEntitiesMap = new HashMap<>();
        for (Integer fileId : fileIds) {
            fileToEntitiesMap.put(fileId, new ArrayList<>());
        }

        for (int i = 0; i < variables.length(); i++) {
            JSONObject variable = variables.getJSONObject(i);
            int entityFileId = variable.optInt("entityFile", -1);
            if (fileToEntitiesMap.containsKey(entityFileId)) {
                fileToEntitiesMap.get(entityFileId).add(variable.getInt("id"));
            }
        }
        return fileToEntitiesMap;
    }

    /**
     *
     *
     *
     *
     */
    private static Map<Integer, Map<Integer, List<Map<String, Object>>>> getFileBasedStructuredResults(
            JSONArray relations,
            Map<Integer, List<Integer>> fileToEntitiesMap) throws JSONException {

        //
        Set<Integer> targetFileIds = new HashSet<>(fileToEntitiesMap.keySet());

        Map<Integer, Map<Integer, List<Map<String, Object>>>> structuredResults = new HashMap<>();

        for (Map.Entry<Integer, List<Integer>> entry : fileToEntitiesMap.entrySet()) {
            int fileId = entry.getKey();
            List<Integer> entityIds = entry.getValue();

            Map<Integer, List<Map<String, Object>>> fileToFromDetails = new HashMap<>();

            for (int i = 0; i < relations.length(); i++) {
                JSONObject relation = relations.getJSONObject(i);

                int toEntityId = relation.optInt("to", -1);
                int fromEntityId = relation.optInt("from", -1);
                JSONObject loc = relation.optJSONObject("loc");
                if (loc == null || !entityIds.contains(toEntityId)) {
                    continue;
                }

                int fromFileId = loc.optInt("file", -1);

                //
                if (targetFileIds.contains(fromFileId)) {
                    continue;   // keep only cross-module callers
                }

                Map<String, Object> relationDetails = new HashMap<>();
                relationDetails.put("fromID", fromEntityId);
                relationDetails.put("toID", toEntityId);
                relationDetails.put("line", loc.optInt("line", -1));

                fileToFromDetails
                        .computeIfAbsent(fromFileId, k -> new ArrayList<>())
                        .add(relationDetails);
            }

            if (!fileToFromDetails.isEmpty()) {
                structuredResults.put(fileId, fileToFromDetails);
            }
        }
        return structuredResults;
    }

    /**
     *
     */
    private static Map<Integer, Map<Integer, List<Map<String, Object>>>> filterSameFileRelationships(
            Map<Integer, Map<Integer, List<Map<String, Object>>>> structuredResults) {

        Map<Integer, Map<Integer, List<Map<String, Object>>>> filteredResults = new HashMap<>();

        for (Map.Entry<Integer, Map<Integer, List<Map<String, Object>>>> fileEntry : structuredResults.entrySet()) {
            int fileId = fileEntry.getKey();
            Map<Integer, List<Map<String, Object>>> fromMap = fileEntry.getValue();

            Map<Integer, List<Map<String, Object>>> filteredFromMap = new HashMap<>();
            for (Map.Entry<Integer, List<Map<String, Object>>> fromEntry : fromMap.entrySet()) {
                int fromFileId = fromEntry.getKey();
                if (fromFileId == fileId) {
                    continue;
                }
                filteredFromMap.put(fromFileId, fromEntry.getValue());
            }

            if (!filteredFromMap.isEmpty()) {
                filteredResults.put(fileId, filteredFromMap);
            }
        }
        return filteredResults;
    }

    /**
     *
     */
    private static void saveFileBasedResultsToJson(
            Map<Integer, Map<Integer, List<Map<String, Object>>>> structuredResults,
            String outputJsonPath) throws IOException, JSONException {

        JSONObject outputJson = new JSONObject();

        for (Map.Entry<Integer, Map<Integer, List<Map<String, Object>>>> fileEntry : structuredResults.entrySet()) {
            int fileId = fileEntry.getKey();
            Map<Integer, List<Map<String, Object>>> fromFileDetails = fileEntry.getValue();

            JSONArray fromFileArray = new JSONArray();
            for (Map.Entry<Integer, List<Map<String, Object>>> fromEntry : fromFileDetails.entrySet()) {
                JSONObject fromObj = new JSONObject();
                fromObj.put(String.valueOf(fromEntry.getKey()), fromEntry.getValue());
                fromFileArray.put(fromObj);
            }
            outputJson.put(String.valueOf(fileId), fromFileArray);
        }

        try (FileWriter fw = new FileWriter(outputJsonPath)) {
            fw.write(outputJson.toString(4));
        }
    }
}
