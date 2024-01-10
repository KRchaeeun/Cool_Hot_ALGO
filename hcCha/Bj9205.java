import java.util.ArrayDeque;
import java.util.Scanner;

public class Bj9205 {
    static int t, n, homeX, homeY, destinationX, destinationY;
    static int[][] store;

    static String Bfs() {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {homeX, homeY});
        boolean[] visited = new boolean[n];

        while (!q.isEmpty()) {
            int[] node = q.poll();
            homeX = node[0];
            homeY = node[1];

            if (Math.abs(homeX - destinationX) + Math.abs(homeY - destinationY) <= 1000) {
                return "happy";
            }

            for (int i = 0; i < n; i++) {
                if (Math.abs(homeX - store[i][0]) + Math.abs(homeY - store[i][1]) <= 1000) {
                    if (!visited[i]) {
                        visited[i] = true;
                        q.add(new int[] {store[i][0], store[i][1]});
                    }
                }
            }
        }
        return "sad";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            n = sc.nextInt();
            store = new int[n][2];
            homeX = sc.nextInt();
            homeY = sc.nextInt();

            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 2; k++) {
                    store[j][k] = sc.nextInt();
                }
            }

            destinationX = sc.nextInt();
            destinationY = sc.nextInt();

            System.out.println(Bfs());
        }
    }
}
