import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        Deque<String> deque;

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken();
            deque = new ArrayDeque<>();
            boolean flag = true;
            for (String s : line.split("")) {
                if (s.equals("(")) {
                    deque.offerLast(s);
                } else {
                    if (deque.isEmpty()) {
                        flag = false;
                        break;
                    }
                    String output = deque.pollLast();
                    if (output.equals(")")) {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag && deque.isEmpty()) {
                System.out.println("YES");
            } else if (flag && !deque.isEmpty()) {
                System.out.println("NO");
            } else {
                System.out.println("NO");
            }
        }
        bw.close();
        br.close();
    }
}
