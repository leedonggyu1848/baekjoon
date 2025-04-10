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
long long arr[80000];

void get_input() {
  cin >> n;
  FOR(n) cin >> arr[i];
}


void solve() {
  long long rst = 0;
  int cmp;
  for (int cur = 0; cur < n-1; ++cur) {
    cmp = cur + 1;
    while (cmp < n && arr[cmp] < arr[cur]) {
      rst++;
      cmp++;
    }
  }
  cout << rst;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
