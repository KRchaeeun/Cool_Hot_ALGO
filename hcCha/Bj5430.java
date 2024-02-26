import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Bj5430 {

    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {

            String commend = br.readLine();
            int n = Integer.parseInt(br.readLine());

            Deque<Integer> q = new ArrayDeque();
            StringTokenizer st = new StringTokenizer(br.readLine(), "[],");

            for (int i = 0; i < n; i++) {
                q.add(Integer.parseInt(st.nextToken()));
            }

            AC(commend, q);
        }
        System.out.println(sb);
    }

    static void AC(String commend, Deque<Integer> q) {
        boolean isRight = true;

        for (char cmd : commend.toCharArray()) {
            if (cmd == 'R') {
                isRight = !isRight;
                continue;
            }

            if (cmd == 'D') {
                if (isRight) {

                    if (q.poll() == null) {
                        sb.append("error\n");
                        return;
                    }

                } else {

                    if (q.pollLast() == null) {
                        sb.append("error\n");
                        return;
                    }
                }
            }
        }

        if (q.isEmpty()) {
            sb.append("[]\n");
            return;
        }

        sb.append('[');

        if (isRight) {
            sb.append(q.poll());
            while (!q.isEmpty()) {
                sb.append(',').append(q.poll());
            }
        } else {
            sb.append(q.pollLast());
            while (!q.isEmpty()) {
                sb.append(',').append(q.pollLast());
            }
        }

        sb.append("]\n");
    }
}
