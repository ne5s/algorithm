import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }


        long answer = 0;
        // 각 비트 위치에 대해 1이 등장하는 횟수를 세는 배열
        int[] bitCount = new int[30]; // 30비트까지만 고려 (입력 제한을 고려했을 때 충분)

        // 각 숫자의 각 비트 위치에 대해 1인 경우를 세어줌
        for (int num : arr) {
            for (int bit = 0; bit < 30; bit++) {
                if ((num & (1 << bit)) != 0) {
                    bitCount[bit]++;
                }
            }
        }

        // 각 비트 위치에 대해 XOR 합 계산
        for (int bit = 0; bit < 30; bit++) {
            answer += (long)bitCount[bit] * (N - bitCount[bit]) * (1L << bit);
        }

//        int answer = 0;
//        for (int i = 0; i < arr.length - 1; i++) {
//            for (int j = i + 1; j < arr.length; j++) {
//                answer += arr[i] ^ arr[j];
//            }
//        }

        bw.write(String.valueOf(answer));
        bw.flush();

        bw.close();
        br.close();
    }
}