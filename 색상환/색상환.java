import java.io.*;
import java.util.*;
public class Main {
    public static int n, k;
    public static int[][] cache = new int [1001][1001];
    public static final int MOD = 1000000003;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        for (int i = 0; i < n; i++) {
            cache[i][0] = 1;
            cache[i][1] = i;
        }
        for (int i = 2; i < n; i++) {
            for (int j = 2; j <= k; j++) {
                cache[i][j] = (cache[i-1][j] + cache[i-2][j-1]) % MOD;
            }
        }
        System.out.println((cache[n-3][k-1] + cache[n-1][k]) % MOD);
    }
}