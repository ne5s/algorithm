import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] parent = new int[N + 1];
        Map<Integer, List<Integer>> tree = new HashMap<>();

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (tree.containsKey(a)) {
                tree.get(a).add(b);
            } else {
                tree.put(a, new ArrayList<>(Arrays.asList(b)));
            }
            if (tree.containsKey(b)) {
                tree.get(b).add(a);
            } else {
                tree.put(b, new ArrayList<>(Arrays.asList(a)));
            }
        }
        dfs(1, tree, parent);
        for (int i = 2; i < parent.length; i++) {
            System.out.println(parent[i]);
        }

        bw.close();
        br.close();
    }

    public static void dfs(int start, Map<Integer, List<Integer>> tree, int[] parent) {
        for (Integer i : tree.get(start)) {
            if (parent[i] == 0) {
                parent[i] = start;
                dfs(i, tree, parent);
            }
        }
    }
}
