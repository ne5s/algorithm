import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] iDp = new int[n];
        int[] dDp = new int[n];

        for (int i = 0; i < n; i++) {
            iDp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    iDp[i] = Math.max(iDp[i], iDp[j] + 1);
                }
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            dDp[i] = 1;
            for (int j = n - 1; j > i; j--) {
                if (arr[i] > arr[j]) {
                    dDp[i] = Math.max(dDp[i], dDp[j] + 1);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            iDp[i] += dDp[i] - 1;
        }
        bw.write(String.valueOf(Arrays.stream(iDp).max().getAsInt()));
        bw.flush();
        bw.close();
        br.close();
    }
}