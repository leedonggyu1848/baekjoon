#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321
#define MOD 1000000000

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN;
int gCache[101][10];

void getInput() {
  cin >> gN;
}

void solve() {
  for (int i=1; i<10; ++i) gCache[0][i] = 1;
  for (int i=1; i<gN; ++i) for (int j=0; j<10; ++j) {
      if (j == 0) gCache[i][j] = gCache[i-1][1];
      else if (j == 9) gCache[i][j] = gCache[i-1][8];
      else gCache[i][j] = (gCache[i-1][j-1] + gCache[i-1][j+1]) % MOD;
  }
  int answer = 0;
  FOR(10) answer = (answer + gCache[gN-1][i]) % MOD;
  cout << answer << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}