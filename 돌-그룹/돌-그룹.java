import java.io.*;
import java.util.*;
public class Main {
    public static int[] values = new int[3];
    public static int acc = 0;
    public static boolean[][] visited = new boolean[1501][1501];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            values[i] = sc.nextInt();
            acc += values[i];
        }
        for (int i = 0; i < 1501; i++) {
            for (int j = 0; j < 1501; j++) {
                visited[i][j] = false;
            }
        }
        System.out.println(dfs(values[0], values[1]) ? '1' : '0');
    }

    public static boolean dfs(int a, int b){
        if (visited[a][b])
            return false;
        int[] v = {a, b, acc-a-b};
        int bigger, smaller;
        if (v[0] == v[1] && v[1] == v[2])
            return true;
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
            if (i != j)
                visited[v[i]][v[j]] = true;
        }
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
            if (i != j) {
                bigger = Math.max(v[i],v[j]);
                smaller = Math.min(v[i], v[j]);
                if (dfs(smaller + smaller, bigger-smaller))
                    return true;
            }
        }
        return false;
    }
}