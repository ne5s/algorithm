import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(solution());
    }

    public static String solution() {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String[] elements = sc.nextLine().split(" ");

        int cnt = 0;
        List<Integer> stackMax = new ArrayList<>(4);
        stackMax.add(0);
        stackMax.add(0);
        stackMax.add(0);
        stackMax.add(0);

        for (String element : elements) {
            int num = Integer.parseInt(element);
            for (int i = 0; i < 4; i++) {
                if (stackMax.get(i) < num && stackMax.get(i) == 0) {
                    cnt++;
                }
                if (stackMax.get(i) < num) {
                    stackMax.set(i, num);
                    break;
                }
                if (i == 3 && cnt == 4) {
                    return "NO";
                }
            }
        }
        return "YES";
    }
}
