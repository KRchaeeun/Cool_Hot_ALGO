import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Bj1303 {
    static int row;
    static int col;

    public static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        col = Integer.parseInt(st.nextToken());
        row = Integer.parseInt(st.nextToken());
        char[][] matrix = new char[row][col];
        boolean[][] visited = new boolean[row][col];

        for (int i = 0; i < row; i++) {
            String str = br.readLine();
            for (int j = 0; j < col; j++) {
                matrix[i][j] = str.charAt(j);
            }
        }

        int bPower = 0;
        int wPower = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (visited[i][j] == false) {
                    if (matrix[i][j] == 'W') {
                        wPower += bfs(i, j, matrix, visited);
                    } else {
                        bPower += bfs(i, j, matrix, visited);
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(Integer.toString(wPower) + " " + Integer.toString(bPower));

        System.out.println(sb);
    }

    public static int bfs(int x, int y, char[][] matrix, boolean[][] visited) {
        Deque<Node> deque = new ArrayDeque<>();
        int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        deque.offer(new Node(x, y));
        visited[x][y] = true;
        int cnt = 1;

        while (!deque.isEmpty()) {
            Node node = deque.poll();

            for (int i = 0; i < 4; i++) {
                int nx = node.x + delta[i][0];
                int ny = node.y + delta[i][1];

                if (0 <= nx && nx < row && 0 <= ny && ny < col) {
                    if (!visited[nx][ny] && matrix[node.x][node.y] == matrix[nx][ny]) {
                        visited[nx][ny] = true;
                        cnt++;
                        deque.offer(new Node(nx, ny));
                    }
                }
            }
        }

        return cnt * cnt;
    }
}
