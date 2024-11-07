import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static boolean flag = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
        }

        int s = Integer.parseInt(br.readLine());
        boolean[] fan = new boolean[n + 1];
        boolean[] visited = new boolean[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= s; i++) {
            fan[Integer.parseInt(st.nextToken())] = true;
        }

        dfs(graph, fan, visited, 1);

        if (flag) {
            bw.write("yes");
        } else {
            bw.write("Yes");
        }
        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(List<Integer>[] graph, boolean[] fan, boolean[] visited, int now) {
        visited[now] = true;
        if (fan[now]) {
            flag = flag | false;
            return;
        }
        if (graph[now].isEmpty()) {
            flag = true;
            return;
        }

        for (int vertex : graph[now]) {
            if (!visited[vertex]) {
                dfs(graph, fan, visited, vertex);
            }
        }
    }
}