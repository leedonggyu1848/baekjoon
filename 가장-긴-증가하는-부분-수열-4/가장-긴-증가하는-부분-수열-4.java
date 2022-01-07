import java.io.*;
import java.util.*;
public class Main {
    static int[] A = new int[1001];
    static int[] cnt = new int[1001];
    static int[] track = new int[1001];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer tokens = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int longestInx = 0;
        int longestLength = 1;

        for (int cur = 0; cur < N; cur++) {
            A[cur] = Integer.parseInt(tokens.nextToken());
            cnt[cur] = 1;
            track[cur] = -1;
            for (int tar = 0; tar < cur; tar++) {

                if (A[tar] < A[cur] && cnt[tar] >= cnt[cur]){
                    cnt[cur] = cnt[tar] + 1;
                    track[cur] = tar;

                    if (cnt[cur] > longestLength){
                        longestInx = cur;
                        longestLength = cnt[cur];
                    }
                }

            }

        }
        System.out.println(longestLength);
        tracking(sb, longestInx);
        System.out.println(sb.toString());
    }

    public static void tracking(StringBuilder sb, int cur){
        if (cur == -1)
            return;
        tracking(sb, track[cur]);
        sb.append(A[cur]);
        sb.append(' ');
    }
}