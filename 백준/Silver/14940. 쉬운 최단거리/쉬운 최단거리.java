import java.util.*;
import java.io.*;

public class Main {
  static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
  static int ny, nx;
  static int board[][];

  static class Pos {
    int y, x;
    public Pos(int y, int x) {
      this.y = y;
      this.x = x;
    }

    public boolean isRange() {
      if (this.y < 0 || ny <= this.y) return false;
      if (this.x < 0 || nx <= this.x) return false;
      return true;
    }
  }

  static int[][] solve(int y, int x) {
    int rst[][] = new int[ny][nx];
    int dy[] = {0, 0, 1, -1};
    int dx[] = {1, -1, 0, 0};
    Arrays.stream(rst).forEach(row -> Arrays.fill(row, -1));
    Queue<Pos> q = new LinkedList<>();
    q.offer(new Pos(y, x));
    rst[y][x] = 0;
    while (!q.isEmpty()) {
      Pos cur = q.poll();
      for (int i = 0; i < 4; ++i) {
        Pos next = new Pos(cur.y + dy[i], cur.x + dx[i]);
        if (!next.isRange() || board[next.y][next.x] == 0 || rst[next.y][next.x] != -1) continue;
        rst[next.y][next.x] = rst[cur.y][cur.x] + 1;
        q.offer(next);
      }
    }
    return rst;
  }

  public static void main(String[] args) throws IOException {
    StringTokenizer st = new StringTokenizer(in.readLine());
    ny = Integer.parseInt(st.nextToken());
    nx = Integer.parseInt(st.nextToken());
    board = new int[ny][nx];
    int startY=0, startX=0;
    for (int y = 0; y < ny; ++y) {
      st = new StringTokenizer(in.readLine());
      for (int x = 0; x < nx; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
        if (board[y][x] == 2) {
          startY = y;
          startX = x;
          board[y][x] = 1;
        }
      }
    }

    int rst[][] = solve(startY, startX);
    for (int y = 0; y < ny; ++y) {
      for (int x = 0; x < nx; ++x) {
        if (board[y][x] == 0) rst[y][x] = 0;
        out.write(Integer.toString(rst[y][x]) + ' ');
      }
      out.write('\n');
    }
    out.flush();
    out.close();
    in.close();
  }
}
