import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        int[] nNumber = new int[N];

        for (int i = 0; i < N; i++) {
            nNumber[i] = sc.nextInt();
        }

        int max = Arrays.stream(nNumber).max().getAsInt();
        int min = Arrays.stream(nNumber).min().getAsInt();

        System.out.println(min + " " + max);
    }
}
