import java.io.*;
import java.util.*;
public class Main {
    public static PriorityQueue<Edge> pq = new PriorityQueue<>();
    public static int[] parent;
    public static int V, E;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        parent = new int[V+1];
        int s, d, c;
        for (int i = 0; i < V+1; i++)
            parent[i] = i;
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            pq.add(new Edge(s, d, c));
        }
        Edge e;
        int answer = 0;
        while (!pq.isEmpty()){
            e = pq.poll();
            if (find(e.s) != find(e.d)){
                union(e.s, e.d);
                answer += e.c;
            }
        }
        System.out.println(answer);
    }

    public static int find(int n){
        if (n == parent[n]) return n;
        parent[n] = find(parent[n]);
        return parent[n];
    }

    public static void union(int a, int b){
        parent[find(a)] = b;
    }

    public static class Edge implements Comparable<Edge> {
        int s;
        int d;
        int c;
        Edge(int s, int d, int c){
            this.s = s;
            this.d = d;
            this.c = c;
        }

        @Override
        public int compareTo(Edge o) {
            return this.c - o.c;
        }
    }
}