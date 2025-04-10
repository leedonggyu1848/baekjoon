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
#define INF 0x7f7f7f7f

typedef vector<int> vi;
typedef pair<int, int> pii;

int n;
int nums[1000000];
int rst[1000000];

void get_input() {
  cin >> n;
  FOR(n) cin >> nums[i];
}

void solve() {
  stack<int> s;
  for (int cur = 0; cur < n; ++cur) {
    if (!s.empty()) {
      while (!s.empty() && nums[s.top()] < nums[cur]) {
        rst[s.top()] = nums[cur];
        s.pop();
      }
    }
    s.push(cur);
  }
  while (!s.empty()) {
    rst[s.top()] = -1;
    s.pop();
  }
  for (int i = 0; i < n; ++i) {
    cout << rst[i] << ' ';
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
