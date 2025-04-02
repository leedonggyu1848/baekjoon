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

int n, k, lim_l, lim_r;
int arr[1000001];
int acc[1000001];

void get_input() {
  int start, end;
  cin >> n >> k;
  FOR(n) {
    cin >> start >> end;
    lim_l = min(lim_l, start);
    lim_r = max(lim_r, end-1);
    for (int j = start; j < end; ++j) arr[j]++;
  }
}

int sum(int a, int b) {
  if (a == 0) return acc[b];
  return acc[b] - acc[a-1];
}


void solve() {
  acc[lim_l] = arr[lim_l];
  for (int i = lim_l+1; i <= lim_r; ++i) {
    acc[i] = acc[i-1] + arr[i];
  }
  int start=0, end=0;
  while (end <= lim_r) {
    if (start > end) {
      end++;
    } else if (sum(start, end) == k) {
      cout << start << ' ' << end+1 << '\n';
      return;
    } else if (sum(start, end) > k) {
      start++;
    } else {
      end++;
    }
  }
  cout << "0 0\n";
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
