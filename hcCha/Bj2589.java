import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Bj2589 {

    static int maxDist = 0;
    static int row;
    static int col;

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void bfs(int x, int y, int[][] matrix) {

        int[][] visited = new int[row][col];

        ArrayDeque<Node> deque = new ArrayDeque<>();
        int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        deque.offer(new Node(x, y));

        while (!deque.isEmpty()) {
            Node node = deque.poll();

            for (int i = 0; i < 4; i++) {
                int nx = node.x + delta[i][0];
                int ny = node.y + delta[i][1];

                if (0 <= nx && nx < row && 0 <= ny && ny < col) {
                    if (matrix[nx][ny] == -1) continue;
                    if (nx == x && ny == y) continue;
                    if (visited[nx][ny] != 0 && visited[node.x][node.y] + 1 >= visited[nx][ny]) continue;

                    visited[nx][ny] = visited[node.x][node.y] + 1;
                    if (maxDist < visited[nx][ny]) maxDist = visited[nx][ny];
                    deque.offer(new Node(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());
        int[][] matrix = new int[row][col];

        for (int i = 0; i < row; i++) {
            String str = br.readLine();
            for (int j = 0; j < col; j++) {
                matrix[i][j] = str.charAt(j) == 'W' ? -1 : 0;
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] > -1) {
                    bfs(i, j, matrix);
                }
            }
        }

        System.out.println(maxDist);
    }
}
