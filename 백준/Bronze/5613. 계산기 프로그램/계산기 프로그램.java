import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> deque = new ArrayDeque<>();

        while (true) {
            String lines = br.readLine();
            if (lines.equals("+")) {
                int x = deque.pollFirst();
                int y = Integer.parseInt(br.readLine());
                deque.addFirst(x + y);
            } else if(lines.equals("-")) {
                int x = deque.pollFirst();
                int y = Integer.parseInt(br.readLine());
                deque.addFirst(x - y);
            } else if (lines.equals("*")) {
                int x = deque.pollFirst();
                int y = Integer.parseInt(br.readLine());
                deque.addFirst(x * y);
            } else if (lines.equals("/")){
                int x = deque.pollFirst();
                int y = Integer.parseInt(br.readLine());
                deque.addFirst(x / y);
            } else if (lines.equals("=")) {
                System.out.println(deque.pollFirst());
                break;
            } else {
                deque.addFirst(Integer.parseInt(lines));
            }
        }
        bw.close();
        br.close();
    }
}
