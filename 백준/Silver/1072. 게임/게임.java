import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long X = Long.parseLong(st.nextToken());
        long Y = Long.parseLong(st.nextToken());
        long Z = (Y * 100) / X;
        int result = -1;

        if (Z >= 99) {
            bw.write(String.valueOf(result));
        } else {
            long left = 1, right = X;
            while (left <= right) {
                long mid = (left + right) / 2;
                long newZ = ((Y + mid) * 100) / (X + mid);

                if (newZ > Z) {
                    result = (int) mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            bw.write(String.valueOf(result));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}