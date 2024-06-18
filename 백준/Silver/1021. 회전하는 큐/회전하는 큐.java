import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        // N <= 50, M <= N
        // M개만큼의 위치. 1 <= 위치 <= N
        int[] mArr = new int[M];
        int answer = 0;

        for (int i = 0; i < M; i++) {
            mArr[i] = sc.nextInt();
        }

        Deque<Integer> deque = new ArrayDeque();
        for (int i = 1; i <= N; i++) {
            deque.offer(i);
        }

        for (int i = 0; i < mArr.length; i++) {
            Integer peek = deque.peek();
            if (peek == mArr[i]) {
                deque.poll();
                continue;
            } else {
                int leftCount = moveLeft(deque, mArr[i]);
                moveRight(deque, peek);
                int rightCount = moveRight(deque, mArr[i]);

                if (leftCount >= rightCount) {
                    answer += rightCount;
                } else {
                    answer += leftCount;
                    moveLeft(deque, peek);
                    moveLeft(deque, mArr[i]);
                }
            }
            deque.poll();
        }
        System.out.println(answer);
    }
    public static int moveLeft(Deque<Integer> deque, int find) {
        int count = 0;

        while (deque.peek() != find) {
            int firstV = deque.pollFirst();
            deque.offer(firstV);
            count++;
        }
        return count;
    }

    public static int moveRight(Deque<Integer> deque, int find) {
        int count = 0;

        while (deque.peek() != find) {
            int lastV = deque.pollLast();
            deque.offerFirst(lastV);
            count++;
        }
        return count;
    }
}
