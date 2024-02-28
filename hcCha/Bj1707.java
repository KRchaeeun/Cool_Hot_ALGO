import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Bj1707 {
    static int v;
    static int e;
    static int[][] edgeInfo;
    static int[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        while (n > 0) {
            n--;

            StringTokenizer st = new StringTokenizer(br.readLine());
            v = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            edgeInfo = new int[v + 1][v + 1];
            visited = new int[v + 1][v + 1];

            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());

                edgeInfo[u][v] = 1;
                edgeInfo[v][u] = 1;
            }

            System.out.println(checkBipartiteGraph());
        }
    }

    static String checkBipartiteGraph() {
//        Deque<int[][]> q = new ArrayList<>;

        return "NO";
    }

    static class Bipartite{
        public int[] reft;
        public int[] light;
    }
}
