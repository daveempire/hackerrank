import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.HashMap;
import java.util.Map;

// https://www.hackerrank.com/challenges/sparse-arrays/problem

public class Solution {

    // Complete the matchingStrings function below.
    static int[] matchingStrings(String[] strings, String[] queries) {

        Map<String, Integer> inputStringMap = new HashMap<String, Integer>();
        int[] occurrenceCount = new int[queries.length];

        // create a map of the frequency of each substring in strings param
        for (int i = 0; i < strings.length; i++) {
           
            if (inputStringMap.get(strings[i]) == null) {
                inputStringMap.put(strings[i], 1);
            } else {
                int count = inputStringMap.get(strings[i]);
                count++;

                inputStringMap.put(strings[i], count);
            }
        }

        for (int i = 0; i < queries.length; i++) {
            if (inputStringMap.get(queries[i]) != null) {
                occurrenceCount[i] = inputStringMap.get(queries[i]);
            }
        }

        return occurrenceCount;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int stringsCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] strings = new String[stringsCount];

        for (int i = 0; i < stringsCount; i++) {
            String stringsItem = scanner.nextLine();
            strings[i] = stringsItem;
        }

        int queriesCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] queries = new String[queriesCount];

        for (int i = 0; i < queriesCount; i++) {
            String queriesItem = scanner.nextLine();
            queries[i] = queriesItem;
        }

        int[] res = matchingStrings(strings, queries);

        for (int i = 0; i < res.length; i++) {
            bufferedWriter.write(String.valueOf(res[i]));

            if (i != res.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
