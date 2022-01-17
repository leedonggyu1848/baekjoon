import java.io.*;
import java.util.*;

public class Main {
    static int[] p = new int[4];
    static int[][] m = new int[1001][1001];
    static int[] parent = new int[1000];
    static Queue<Integer> q;

    static int n;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int v, pv;
        int rst = 0;
        n = Integer.parseInt(br.readLine());
        boolean[] visited = new boolean[n];

        for (int i = 0; i < 1001; i++) {
            for (int j = 0; j < 1001; j++)
                m[i][j] = -1;
        }
        for (int i = 0; i < n; i++) {
            visited[i] = false;
            st = new StringTokenizer(br.readLine());
            q = new LinkedList<>();
            for (int j = 0; j < 4; j++)
                p[j] = Integer.parseInt(st.nextToken()) + 500;
            parent[i] = i;
            /*
            x1 -> x2, y1
            x2 -> x1, y2
            x1, y1 -> y2
            x2, y2 -> y1
             */
            for (int dx = 0; dx <= p[2] - p[0]; dx++) {
                pushQueue(p[1], p[0]+dx, i);
                pushQueue(p[3], p[2]-dx, i);
            }
            for (int dy = 0; dy <= p[3] - p[1]; dy++) {
                pushQueue(p[1]+dy,p[0], i);
                pushQueue(p[3]-dy,p[2], i);
            }

            while(!q.isEmpty()){
                v = q.poll();
                pv = parent[v];
                for (int j = 0; j < i; j++) {
                    if(parent[j] == pv)
                        parent[j] = i;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (!visited[parent[i]]){
                visited[parent[i]] = true;
                rst++;
            }
        }

        //원점을 지나면 +1
        if (m[500][500] != -1)
            rst--;

        System.out.println(rst);
        br.close();
    }
    public static void pushQueue(int y, int x, int i){
        if (m[y][x] != -1)
            q.add(m[y][x]);
        m[y][x] = i;
    }
}