import java.util.ArrayDeque;
import java.util.Scanner;

public class Bj9205 {
    static int t;
    static int n;
    static int[] node;
    static int[][] location;
    static int beer = 20;

    static String bfs(int x, int y) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});

        while (!q.isEmpty()) {
            node = q.poll();

            x = node[0];
            y = node[1];

            if (x == location[location.length - 1][0] && y == location[location.length - 1][1]) {
                return "happy";
            }



        }

        return "sad";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            n = sc.nextInt();
            location = new Integer[n + 2][2];
            for (int j = 0; j < n + 2; j++) {
                for (int k = 0; k < 2; k++) {
                    location[j][k] = sc.nextInt();
                }
            }

            System.out.println(bfs(location[0][0], location[0][1]));
        }
    }
}
