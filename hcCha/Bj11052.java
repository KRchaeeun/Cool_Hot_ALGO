import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Bj11052 {
    static int n;
    static Integer[] dp;
    static Integer[] cardPack;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        cardPack = new Integer[n + 1];
        dp = new Integer[n + 1];
        Arrays.fill(dp, 0);

        String[] inputCard = br.readLine().split(" ");
        for (int i = 1; i <= n; i++) {
            cardPack[i] = Integer.parseInt(inputCard[i - 1]);
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.max(dp[i], dp[i - j] + cardPack[j]);
//                System.out.println(Arrays.toString(dp));
            }
//            System.out.println("----------------------");
        }

        System.out.println(dp[n]);
    }
}
