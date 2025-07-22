import java.util.*;
import java.io.*;
public class Main {
  static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
  static int n;
  static boolean dp[] = new boolean[1001];

  public static void main(String[] args) throws IOException {
    boolean SK = true; // 먼저시작
    boolean CY = false;
    n = Integer.parseInt(in.readLine());
    dp[0] = false;
    dp[1] = true;
    dp[2] = false;
    dp[3] = true;
    for (int i = 4; i <= n; ++i)
      dp[i] = !(dp[i-1] && dp[i-3]);
    out.write(dp[n] ? "SK" : "CY");
    out.flush();
    in.close();
    out.close();
  }
}
