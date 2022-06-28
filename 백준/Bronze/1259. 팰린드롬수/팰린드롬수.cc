#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

string s;
void solve() {
  for(int i=0; i<s.size()/2; ++i) {
    if (s[i] != s[s.size()-1-i]) {
      cout << "no\n";
      return;
    }
  }
  cout << "yes\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  while (true) {
    cin >> s;
    if (s == "0") break;
    solve();
  }
  return 0;
}