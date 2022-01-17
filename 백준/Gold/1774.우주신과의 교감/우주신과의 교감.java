import java.io.*;
import java.util.*;
public class Main {
    static int N, M;
    static int[][] posData = new int[1001][2];
    static int[] parent = new int[1001];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int a, b;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            posData[i][0] = a;
            posData[i][1] = b;
            parent[i] = i;
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            union(a-1, b-1);
        }
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                pq.add(new Edge(i, j, distance(posData[i][0], posData[i][1], posData[j][0], posData[j][1])));
            }
        }
        Edge cur;
        double rst = 0;
        while(!pq.isEmpty()){
            cur = pq.poll();
            if(getParent(cur.s) != getParent(cur.e)){
                union(cur.s, cur.e);
                rst += cur.c;
            }
        }
        System.out.printf("%.2f\n", rst);
    }

    static double distance(int x1, int y1, int x2, int y2){
        return Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
    }

    static void union(int a, int b) {
        int aP = getParent(a);
        int bP = getParent(b);
        if (aP < bP){
            parent[bP] = aP;
        } else{
            parent[aP] = bP;
        }
    }
    static int getParent(int a){
        if (parent[a] == a)
            return a;
        parent[a] = getParent(parent[a]);
        return parent[a];
    }

    static class Edge implements Comparable<Edge>{
        int s, e;
        double c;
        Edge(int s, int e, double c){
            this.s = s;
            this.e = e;
            this.c = c;
        }
        @Override
        public int compareTo(Edge o) {
            if (this.c < o.c)
                return -1;
            if (this.c > o.c)
                return 1;
            return 0;
        }
    }
}