import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

// https://www.hackerrank.com/challenges/counting-valleys/problem

public class Solution {

    // Complete the countingValleys function below.
    static int countingValleys(int n, String s) {
        int valleys = 0;
        int seaLevel = 0;

        char[] c = s.toCharArray();

        for (int i = 0; i < n; i++) {
            if (c[i] == 'U') seaLevel++;
            else seaLevel--;

            if (seaLevel == 0 && c[i] == 'U') valleys++;
        }
        return valleys;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();

        int result = countingValleys(n, s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
