import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
    int index;
    int cost;

    public Node(int index, int cost) {
        this.index = index;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.cost, o.cost);
    }
}

public class Bj1916 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int numOfCities = Integer.parseInt(br.readLine());
        int numOfbus = Integer.parseInt(br.readLine());
        int[] visited = new int[numOfCities];
        Arrays.fill(visited, Integer.MAX_VALUE);
        int[][] information = new int[numOfCities][numOfCities];

        for (int i = 0; i < numOfCities; i++) {
            Arrays.fill(information[i], -1);
        }

        for (int i = 0; i < numOfbus; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int s = Integer.parseInt(st.nextToken()) - 1;
            int e = Integer.parseInt(st.nextToken()) - 1;
            int cost = Integer.parseInt(st.nextToken());

            if (information[s][e] != -1 && information[s][e] <= cost) continue;

            information[s][e] = cost;
        }

        st = new StringTokenizer(br.readLine(), " ");
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());
        PriorityQueue<Node> pq = new PriorityQueue<>();

        pq.offer(new Node(start - 1, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (node.cost > visited[node.index]) continue;
            if (node.index + 1 == end) {
                System.out.println(node.cost);
                return;
            }

            for (int i = 0; i < numOfCities; i++) {
                if (information[node.index][i] > -1) {
                    int sumCost = node.cost + information[node.index][i];
                    if (visited[i] <= sumCost) continue;
                    visited[i] = sumCost;
                    pq.offer(new Node(i, sumCost));
                }
            }
        }
    }
}
