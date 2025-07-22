import java.util.*;
import java.io.*;

public class Main {
  static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

  public static boolean isResolve(Stack<Character> s, String tar) {
    int i = 0;
    Stack<Character> store = new Stack<>();
    while (!s.empty() && i < tar.length() && s.peek() == tar.charAt(i)) {
      ++i;
      store.push(s.pop());
    }
    if (i == tar.length()) return true;
    while (!store.isEmpty()) s.push(store.pop());
    return false;
  }

  public static void main(String[] args) throws IOException {
    String src = in.readLine();
    String tar = in.readLine();
    Stack<Character> s = new Stack<>();
    for (int i = src.length()-1; i >= 0; --i) {
      s.push(src.charAt(i));
      while (!s.isEmpty() && isResolve(s, tar)) {}
    }
    StringBuilder sb = new StringBuilder();
    while (!s.isEmpty()) sb.append(s.pop());
    String answer = sb.toString();
    if (answer.equals("")) {
      out.write("FRULA");
    } else {
      out.write(answer);
    }
    out.flush();
    out.close();
    in.close();
  }
}
