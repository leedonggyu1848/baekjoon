import java.io.*;
import java.util.*;

public class Main {
	static class Node implements Comparable<Node> {
		public int end, weight;
		public Node(int end, int weight) {
			this.end = end;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return weight - o.weight;
		}
	}
	static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	static int nv, ne, start;
	static List<Node>[] adj;

	public static int[] dijkstra(int start) {
		int[] dist = new int[nv + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		Node cur;
		dist[start] = 0;
		Queue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(start, 0));
		while (!pq.isEmpty()) {
			cur = pq.poll();
			if (cur.weight != dist[cur.end]) continue;
			for (Node next : adj[cur.end]) {
				if (dist[next.end] > dist[cur.end] + next.weight) {
					dist[next.end] = dist[cur.end] + next.weight;
					pq.offer(new Node(next.end, dist[next.end]));
				}
			}
		}
		return dist;
	}

	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(in.readLine());
		nv = Integer.parseInt(st.nextToken());
		ne = Integer.parseInt(st.nextToken());
		start = Integer.parseInt(in.readLine());
		adj = new ArrayList[nv+1];
		for (int i = 0; i < nv+1; ++i) adj[i] = new ArrayList<>();
		for (int i = 0; i < ne; ++i) {
			st = new StringTokenizer(in.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			adj[s].add(new Node(e, v));
		}
		int[] rst = dijkstra(start);
		for (int i = 1; i < nv+1; ++i) {
			if (rst[i] == Integer.MAX_VALUE) out.write("INF\n");
			else out.write(rst[i] + "\n");
		}
		out.flush();
		in.close();
		out.close();
	}
}