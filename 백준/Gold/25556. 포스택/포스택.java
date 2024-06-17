import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println(solution());
    }

    public static String solution() {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String[] elements = sc.nextLine().split(" ");

        Deque<Integer>[] stacks = new Deque[4];
        for (int i = 0; i < 4; i++) {
            stacks[i] = new ArrayDeque<>();
            stacks[i].push(0);
        }

        boolean flag = false;

        for (String element : elements) {
            int num = Integer.parseInt(element);
            flag = false;

            for (int i = 0; i < 4; i++) {
                if (num > stacks[i].peek()) {
                    stacks[i].push(num);
                    flag = true;
                    break;
                }
            }
            if (!flag) break;
        }
        if (flag) return "YES";
        else return "NO";
    }
}