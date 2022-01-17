import java.io.*;
import java.util.*;
public class Main {
    static int N, D, start;
    static int[] costs = new int[10001];
    static LinkedList<Edge>[] m;
    static final int MAX_VALUE = 0x0f0f0f0f;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        int s,e,c;
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            D = Integer.parseInt(st.nextToken());
            start = Integer.parseInt(st.nextToken());
            m = new LinkedList[N+1];
            for (int j = 0; j < N+1; j++) {
                m[j] = new LinkedList<>();
            }
            for (int j = 0; j < D; j++) {
                st = new StringTokenizer(br.readLine());
                e = Integer.parseInt(st.nextToken());
                s = Integer.parseInt(st.nextToken());
                c = Integer.parseInt(st.nextToken());
                m[s].add(new Edge(e, c));
            }
            solve();
        }

    }

    public static void solve(){
        for (int i = 0; i < N+1; i++)
            costs[i] = MAX_VALUE;
        costs[start] = 0;
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        Edge wayPoint;
        int curCost;
        pq.add(new Edge(start, 0));
        while (!pq.isEmpty()){
            wayPoint = pq.poll();
            if (costs[wayPoint.e] < wayPoint.c)
                continue;
            for(Edge dest: m[wayPoint.e]){
                curCost = costs[wayPoint.e] + dest.c;
                if (curCost < costs[dest.e]){
                    costs[dest.e] = curCost;
                    pq.add(new Edge(dest.e, curCost));
                }
            }
        }
        int cnt = 0, value = 0;
        for (int i = 1; i <= N; i++) {
            if(costs[i] != MAX_VALUE){
                cnt++;
                if(value < costs[i])
                    value = costs[i];
            }
        }
        System.out.printf("%d %d\n", cnt, value);
    }

    static class Edge implements Comparable<Edge>{
        int e, c;
        Edge(int e, int c){
            this.e = e;
            this.c = c;
        }

        @Override
        public int compareTo(Edge o) {
            return this.c - o.c;
        }
    }
}