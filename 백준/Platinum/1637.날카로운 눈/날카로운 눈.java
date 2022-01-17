import java.io.*;
import java.util.*;
public class Main {
    static int N;
    static int[][] input = new int[20000][3];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                input[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long start = 1;
        long end = Integer.MAX_VALUE;
        long mid;
        long answer = -1;
        while(start <= end){
            mid = (start + end) / 2;
            if (counting(mid)){
                answer = mid;
                end = mid - 1;
            } else{
                start = mid + 1;
            }
        }
        if (answer == -1)
            System.out.println("NOTHING");
        else{
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                if(answer <= input[i][1] && input[i][0] <= answer && (answer-input[i][0]) % input[i][2] == 0)
                    cnt++;
            }
            System.out.printf("%d %d\n", answer, cnt);
        }
    }

    public static boolean counting(long cur){
        long upper;
        long cnt = 0;
        for (int i = 0; i < N; i++) {
            if (input[i][0] > cur)
                continue;
            upper = Math.min(input[i][1], cur);
            cnt += (upper - input[i][0])/input[i][2]+1;
            cnt %= 2;
        }
        return cnt%2 == 1;
    }
}