import java.io.*;
import java.util.*;
public class Main {
    public static int N;
    public static double[][] datas;
    public static double[][] costs;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        datas = new double[N][2];
        costs = new double[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            datas[i][0] = Double.parseDouble(st.nextToken());
            datas[i][1] = Double.parseDouble(st.nextToken());
        }
        for (int i = 0; i < N; i++) for (int j = i; j < N; j++) {
            costs[i][j] = costs[j][i] = distance(datas[i][0], datas[i][1], datas[j][0], datas[j][1]);
        }
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        double answer = 0;
        Edge cur;
        boolean[] visited = new boolean[N];
        Arrays.fill(visited, false);
        for (int i = 1; i < N; i++)
            pq.add(new Edge(0, i));
        visited[0] = true;
        while (!pq.isEmpty()){
            cur = pq.poll();
            if (!visited[cur.d]){
                answer += costs[cur.s][cur.d];
                for (int i = 0; i < N; i++) {
                    if (!visited[i])
                        pq.add(new Edge(cur.d, i));
                }
                visited[cur.d] = true;
            }
        }
        System.out.println(answer);
    }

    public static double distance(double x1, double y1, double x2, double y2){
        return Math.sqrt(Math.pow((y2 - y1), 2) + Math.pow((x2- x1), 2));
    }

    static class Edge implements Comparable<Edge>{
        int s;
        int d;
        Edge(int s, int d){
            this.s = s;
            this.d = d;
        }

        @Override
        public int compareTo(Edge o) {
            return (int)(costs[s][d] - costs[o.s][o.d]);
        }
    }
}