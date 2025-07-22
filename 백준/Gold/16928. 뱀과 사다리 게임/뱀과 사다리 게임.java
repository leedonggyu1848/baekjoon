import java.util.*;
import java.io.*;

public class Main {
  static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
  static int adj[] = new int[101];

  static int solve() {
    int cur, curCnt, next;
    int visited[] = new int[101];
    Arrays.fill(visited, -1);
    Queue<Integer> q = new LinkedList<>();
    q.offer(1);
    visited[1] = 0;
    while (!q.isEmpty()) {
      cur = q.poll();
      curCnt = visited[cur];
      for (int i = 1; i <= 6; ++i) {
        next = cur + i;
        if (next > 100 || visited[next] != -1) continue;
        if (next == 100) return curCnt + 1;
        if (adj[next] != -1) next = adj[next];
        if (visited[next] != -1) continue;
        if (next == 100) return curCnt + 1;
        visited[next] = curCnt+1;
        q.offer(next);
      }
    }
    return -1;
  }

  public static void main(String[] args) throws IOException {
    StringTokenizer st = new StringTokenizer(in.readLine());
    int nUp = Integer.parseInt(st.nextToken());
    int nDown = Integer.parseInt(st.nextToken());
    int start, end;
    Arrays.fill(adj, -1);
    for (int i = 0; i < nUp+nDown; ++i) {
      st = new StringTokenizer(in.readLine());
      start = Integer.parseInt(st.nextToken());
      end = Integer.parseInt(st.nextToken());
      adj[start] = end;
    }
    out.write(Integer.toString(solve()));
    out.flush();
    out.close();
    in.close();
  }
}
