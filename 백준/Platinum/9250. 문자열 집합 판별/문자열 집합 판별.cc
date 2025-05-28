#include <iostream>
#include <string>
#include <vector>
#include <queue>

#define MAX_INT 2147483647
using namespace std;

int N, Q;

class Trie {
public:
  Trie *next[26];
  Trie *failure;
  bool output;

  Trie() {
    fill(next, next+26, nullptr);
    failure = nullptr;
    output = false;
  }
  ~Trie() {
    for (int i = 0; i < 26; ++i) {
      if (next[i]) delete next[i];
    }
  }

  void insert(const char* key) {
    char chr = *key;
    if (chr == '\0') {
      output = true;
      return;
    }
    int idx = chr - 'a';
    if (!next[idx]) next[idx] = new Trie;
    next[idx]->insert(key+1);
  }

};

void make_failure(Trie* root) {
  queue<Trie*> q;
  q.push(root);
  while (!q.empty()) {
    Trie* cur = q.front();
    q.pop();
    for (int i = 0; i < 26; ++i) {
      Trie* next = cur->next[i];
      if (!next) continue;

      if (cur == root) next->failure = root;
      else {
        Trie* dest = cur->failure;
        while (dest != root && !dest->next[i])
          dest = dest->failure;
        if (dest->next[i]) dest = dest->next[i];
        next->failure = dest;
      }
      if (next->failure->output) next->output = true;
      q.push(next);
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  char s[10001];
  Trie* root = new Trie;
  cin >> N;
  for (int i = 0; i < N; ++i) {
    cin >> s;
    root->insert(s);
  }
  make_failure(root);
  cin >> Q;
  while (Q--) {
    cin >> s;
    Trie* cur = root;
    bool rst = false;
    for (int c = 0; s[c]; ++c) {
      int next = s[c] - 'a';
      while (cur != root && !cur->next[next])
        cur = cur->failure;
      if (cur->next[next]) cur = cur->next[next];
      if (cur->output) {
        rst = true;
        break;
      }
    }
    cout << (rst ? "YES\n" : "NO\n");
  }
  delete root;
  return 0;
}
