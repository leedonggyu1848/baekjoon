import java.io.*;
import java.util.*;
public class Main {
    public static final int SEP_INX = 26;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String data;
        Trie trie = new Trie(' ');
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N ; i++) {
            data = br.readLine().split(" ", 2)[1];
            trie.add_data(data, 0);
        }
        trie.dfs(-1, new StringBuilder());
    }

    public static class Trie{
        char c;
        Trie[] next;
        Trie(char c){
            this.c = c;
            next = new Trie[27];
            for (int i = 0; i < 27; i++)
                next[i] = null;
        }

        public void add_data(String s, int i){
            if (i < s.length()){
                int nextI = s.charAt(i) == ' ' ? SEP_INX : s.charAt(i) - 'A';
                if (next[nextI] == null)
                    next[nextI] = new Trie(s.charAt(i));
                this.next[nextI].add_data(s, i+1);
            } else if(i == s.length()){
                if (next[SEP_INX] == null)
                    next[SEP_INX] = new Trie(' ');
            }
        }

        public void dfs(int depth, StringBuilder sb) {
            StringBuilder nextSb;
            if (c == ' ') {
                depth++;
                nextSb = new StringBuilder();
            } else{
                sb.append(c);
                nextSb = new StringBuilder(sb);
            }
            if (next[SEP_INX] != null){
                System.out.print("--".repeat(depth));
                System.out.println(sb.toString());
            }
            for (int i = 0; i < 27; i++) {
                if (next[i] != null)
                    next[i].dfs(depth, new StringBuilder(nextSb));
            }
        }
    }
}