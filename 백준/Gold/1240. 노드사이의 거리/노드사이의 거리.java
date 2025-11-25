import java.util.*;
import java.io.*;

public class Main {
  public static class Node {
    public int n, cost;
    public Node(int n, int cost) {
      this.n = n;
      this.cost = cost;
    }
  }

  public static int nv;
  public static List<List<Node>> edges = new ArrayList<List<Node>>();

  public static int bfs(int start, int end) {
    Queue<Node> q = new ArrayDeque<>();
    boolean[] visited = new boolean[nv+1];
    q.offer(new Node(start, 0));
    visited[start] = true;
    Node cur;
    while (!q.isEmpty()) {
      cur = q.poll();
      for (Node nxt : edges.get(cur.n)) {
        if (visited[nxt.n]) continue;
        if (nxt.n == end) return cur.cost + nxt.cost;
        visited[nxt.n] = true;
        q.offer(new Node(nxt.n, cur.cost + nxt.cost));
      }
    }
    return 0;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    nv = Integer.parseInt(st.nextToken());
    int np = Integer.parseInt(st.nextToken());
    int v1, v2, cost;
    for (int i = 0; i < nv+1; ++i) {
      edges.add(new ArrayList<Node>());
    }

    for (int i = 0; i < nv-1; ++i) {
      st = new StringTokenizer(br.readLine(), " ");
      v1 = Integer.parseInt(st.nextToken());
      v2 = Integer.parseInt(st.nextToken());
      cost = Integer.parseInt(st.nextToken());
      edges.get(v1).add(new Node(v2, cost));
      edges.get(v2).add(new Node(v1, cost));
    }

    for (int i = 0; i < np; ++i) {
      st = new StringTokenizer(br.readLine(), " ");
      v1 = Integer.parseInt(st.nextToken());
      v2 = Integer.parseInt(st.nextToken());
      bw.write(bfs(v1, v2) + "\n");
    }
    bw.flush();
    bw.close();
    br.close();
  }
}
