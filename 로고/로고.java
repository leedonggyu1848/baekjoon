import java.io.*;
import java.util.*;

public class Main {
    static int[] p = new int[4];
    static int[][] m = new int[1001][1001];
    static boolean[] visited = new boolean[1000];
    static int[] parent = new int[1000];

    static int n;

    public static int getParent(int idx){
        if (parent[idx] == idx)
            return idx;
        parent[idx] = getParent(parent[idx]);
        return parent[idx];
    }
    public static void union(int a, int b){
        int ap = getParent(a);
        int bp = getParent(b);
        if (ap < bp){
            parent[parent[b]] = ap;
            parent[b] = ap;
        }else{
            parent[parent[a]] = bp;
            parent[a] = bp;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int rst = 0;
        int tp;
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < 1001; i++) {
            for (int j = 0; j < 1001; j++)
                m[i][j] = -1;
        }

        for (int i = 0; i < n; i++) {
            visited[i] = false;
            parent[i] = i;
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++)
                p[j] = Integer.parseInt(st.nextToken()) + 500;

            for (int dx = 0; dx <= p[2] - p[0]; dx++) {
                connect(p[1], p[0]+dx, i);
                connect(p[3], p[2]-dx, i);
            }
            for (int dy = 0; dy <= p[3] - p[1]; dy++) {
                connect(p[1]+dy,p[0], i);
                connect(p[3]-dy,p[2], i);
            }
        }

        for (int i = 0; i < n; i++) {
            tp = getParent(i);
            if(!visited[tp]){
                visited[tp] = true;
                rst++;
            }
        }
        if (m[500][500] != -1)
            rst--;

        System.out.println(rst);
        br.close();
    }

    public static void connect(int y, int x, int i){
        if (m[y][x] != -1)
            union(i, m[y][x]);
        m[y][x] = i;
    }

}
