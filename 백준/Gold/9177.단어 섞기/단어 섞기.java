import java.io.*;
import java.util.*;
public class Main {
    static String src1, src2, dest;
    static boolean[][] visited = new boolean[201][201];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 201; j++)  for (int k = 0; k < 201 ; k++) {
                visited[j][k] = false;
            }
            st = new StringTokenizer(br.readLine());
            src1 = st.nextToken();
            src2 = st.nextToken();
            dest = st.nextToken();
            sb.append("Data set ");
            sb.append(i+1);
            sb.append(": ");
            sb.append(solve(0, 0, 0) ? "yes\n" : "no\n");
        }
        System.out.print(sb.toString());
    }
    public static boolean solve(int inx1, int inx2, int inxd){
        visited[inx1][inx2] = true;
        if (inxd == dest.length())
            return true;
        boolean ret = false;
        if (inx1 < src1.length() && !visited[inx1+1][inx2] && src1.charAt(inx1) == dest.charAt(inxd)){
            ret |= solve(inx1+1, inx2, inxd+1);
        }
        if (inx2 < src2.length() && !visited[inx1][inx2+1] && src2.charAt(inx2) == dest.charAt(inxd)){
            ret |= solve(inx1, inx2+1, inxd+1);
        }
        return ret;
    }
}