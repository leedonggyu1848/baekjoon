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

int n, m;
int nums[10000];
int acc[10000];

void get_input() {
  cin >> n >> m;
  FOR(n) {
    cin >> nums[i];
    if (i == 0) acc[0] = nums[0];
    else acc[i] = nums[i] + acc[i-1];
  }
}

int sum(int a, int b) {
  if (a == 0) return acc[b];
  return acc[b] - acc[a-1];
}

void solve() {
  int rst = 0;
  int start=0, end=0;
  while (end < n) {
    if (start > end) end++;
    else if (sum(start, end) == m) {
      rst++;
      end++;
    }
    else if (sum(start, end) < m) end++;
    else start++;
  }
  cout << rst;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
