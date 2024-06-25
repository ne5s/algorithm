import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;

public class Main {
    static int cnt = 0;
    public static void main(String[] args) {
        InputReader ir = new InputReader(System.in);
        int N = ir.nextInt();
        int K = ir.nextInt();
        int[] arr = new int[N + 1];
        arr[0] = 0;
        for (int i = 1; i <= N; i++) {
            arr[i] = ir.nextInt();
        }
        heapSort(arr, N, K);
        if (cnt < K) System.out.println(-1);
    }

    public static void heapSort(int[] arr, int N, int K) {
        buildMinHeap(arr, arr.length - 1, K);
        for (int i = N; i >= 2; i--) {
            swap(arr, 1, i, K);
            heapify(arr, 1, i - 1, K);
        }
    }

    public static void buildMinHeap(int[] arr, int num, int K) {
        for (int i = num / 2; i >= 1; i--) {
            heapify(arr, i, num, K);
        }
    }

    public static void heapify(int[] arr, int j, int num, int K) {
        int left = 2 * j;
        int right = 2 * j + 1;
        int smaller = 0;
        if (right <= num) {
            if (arr[left] < arr[right]) {
                smaller = left;
            } else {
                smaller = right;
            }
        } else if (left <= num) {
            smaller = left;
        } else {
            return;
        }
        if (arr[smaller] < arr[j]) {
            swap(arr, j, smaller, K);
            heapify(arr, smaller, num, K);
        }
    }

    static void swap(int[] arr, int a, int b, int K) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
        cnt++;
        if (cnt == K) {
            for (int j = 1; j < arr.length; j++) {
                if (j != arr.length - 1) System.out.print(arr[j] + " ");
                else System.out.print(arr[j]);
            }
            System.exit(0);
        }
    }

    static class InputReader {private final InputStream stream;private final byte[] buf = new byte[8192];private int curChar, snumChars;public InputReader(InputStream st) {this.stream = st;}public int read() {if (snumChars == -1)throw new InputMismatchException();if (curChar >= snumChars) {curChar = 0;try {snumChars = stream.read(buf);} catch (
            IOException e) {throw new InputMismatchException();}if (snumChars <= 0)return -1;}return buf[curChar++];}public int nextInt() {int c = read();while (isSpaceChar(c))c = read();int sgn = 1;if (c == '-') {sgn = -1;c = read();}int res = 0;do {res *= 10;res += c - '0';c = read();} while (!isSpaceChar(c));return res * sgn;}public long nextLong() {int c = read();while (isSpaceChar(c))c = read();int sgn = 1;if (c == '-') {sgn = -1;c = read();}long res = 0;do {res *= 10;res += c - '0';c = read();} while (!isSpaceChar(c));return res * sgn;}public int[] nextIntArray(int n) {int a[] = new int[n];for (int i = 0; i < n; i++)a[i] = nextInt();return a;}public List<Integer> nextIntList(int n) {List<Integer> a = new ArrayList<>();for (int i = 0; i < n; i++)a.add(nextInt());return a;}public String readString() {int c = read();while (isSpaceChar(c)) {c = read();}StringBuilder res = new StringBuilder();do {res.appendCodePoint(c);c = read();} while (!isSpaceChar(c));return res.toString();}public String nextLine() {int c = read();while (isSpaceChar(c))c = read();StringBuilder res = new StringBuilder();do {res.appendCodePoint(c);c = read();} while (!isEndOfLine(c));return res.toString();}public boolean isSpaceChar(int c) {return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;}private boolean isEndOfLine(int c) {return c == '\n' || c == '\r' || c == -1;}}
}
