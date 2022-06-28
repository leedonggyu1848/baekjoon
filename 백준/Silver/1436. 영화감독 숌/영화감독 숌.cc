#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN;

void getInput() {
  cin >> gN;
}

bool checkEndNumber(int n) {
  while (n >= 666) {
    if (n % 1000 == 666) return true;
    n /= 10;
  }
  return false;
}

void solve() {
  int cnt = 0;
  int cur = 1;
  while (cnt < gN) {
    if (checkEndNumber(cur)) cnt++;
    cur++;
  }
  cout << cur-1 << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}