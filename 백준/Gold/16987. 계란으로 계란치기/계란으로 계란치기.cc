#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <complex>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define FOR2(N, M) for (int i=0; i<(N); ++i) for (int j=0; j<(M); ++j)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

int n, s[8], w[8];

void get_input() {
  cin >> n;
  FOR(n) cin >> s[i] >> w[i];
}

int rst = 0;

void simulation(int cur, int cnt) {
  int org = cnt;
  bool flag = false;
  if (cur == n) {
    rst = max(rst, cnt);
    return;
  }
  if (s[cur] <= 0) {
    simulation(cur+1, cnt);
    return;
  }
  for (int i = 0; i < n; ++i) {
    if (i == cur) continue;
    if (s[i] > 0) {
      flag = true;
      s[i] -= w[cur];
      s[cur] -= w[i];
      if (s[i] <= 0) cnt++;
      if (s[cur] <= 0) cnt++;
      simulation(cur+1, cnt);
      s[i] += w[cur];
      s[cur] += w[i];
      cnt = org;
    }
  }
  if (!flag) simulation(cur+1, cnt);
}


void solve() {
  simulation(0, 0);
  cout << rst << '\n';
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
