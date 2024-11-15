import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        if (k >= n) {
            bw.write("0");
            bw.flush();
            bw.close();
            br.close();
            return;
        }

        int[] sensors = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < n; i++) {
            sensors[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(sensors);

        int[] distance = new int[n - 1];

        for (int i = 0; i < n - 1; i++) {
            distance[i] = sensors[i + 1] - sensors[i];
        }
        Arrays.sort(distance);
        
        int minDistanceSum = 0;
        for (int i = 0; i < n - k; i++) {
            minDistanceSum += distance[i];
        }

        bw.write(String.valueOf(minDistanceSum));
        bw.flush();
        bw.close();
        br.close();
    }
}