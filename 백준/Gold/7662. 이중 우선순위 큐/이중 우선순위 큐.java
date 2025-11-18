import java.util.*;

public class Main {

  public static class Emt implements Comparable<Emt> {
    public long value;
    public boolean live;
    public Emt(long value, boolean live) {
      this.value = value;
      this.live = live;
    }

    @Override
    public int compareTo(Emt o) {
      long rst = this.value - o.value;
      if (rst == 0) return 0;
      else if (rst < 0) return -1;
      else return 1;
    }
  }

  public static Emt popOne(PriorityQueue<Emt> q) {
    while (!q.isEmpty()) {
      Emt n = q.remove();
      if (n.live) {
        n.live = false;
        return n;
      }
    }
    return null;
  }

  public static void main(String[] s) {
    Scanner scanner = new Scanner(System.in);
    int firstLoop = scanner.nextInt();
    for (int i = 0; i < firstLoop; ++i) {
      PriorityQueue<Emt> minq = new PriorityQueue<>();
      PriorityQueue<Emt> maxq = new PriorityQueue<>(Collections.reverseOrder());
      int secondLoop = scanner.nextInt();
      for (int j = 0; j < secondLoop; ++j) {
        String cmd = scanner.next();
        long n = scanner.nextLong();
        if (cmd.startsWith("I")) {
          Emt e = new Emt(n, true);
          minq.offer(e);
          maxq.offer(e);
        } else if (n == 1) {
          popOne(maxq);
        } else {
          popOne(minq);
        }
      }
        Emt left = popOne(maxq);
        Emt right = popOne(minq);

        if (left == null) {
          System.out.println("EMPTY");
        } else if (right == null) {
          System.out.println(left.value + " " + left.value);
        } else {
          System.out.println(left.value + " " + right.value);
        }
    }
    scanner.close();
  }
}
