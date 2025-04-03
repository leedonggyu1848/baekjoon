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

int n, xs[1000000], sorted[1000000], m;
priority_queue<int, vector<int>, greater<int>> pq;

void get_input() {
  cin >> n;
  FOR(n) {
    cin >> xs[i];
    pq.push(xs[i]);
  }
}

int find_index(int tar, int left, int right) {
  int mid = (left + right) / 2;
  if (sorted[mid] == tar) return mid;
  if (tar < sorted[mid]) return find_index(tar, left, mid-1);
  return find_index(tar, mid+1, right);
}

void solve() {
  int cur;
  int bf = pq.top();
  pq.pop();
  sorted[m] = bf;
  ++m;
  while(!pq.empty()) {
    cur = pq.top();
    pq.pop();
    if (bf == cur) continue;
    sorted[m] = cur;
    ++m;
    bf = cur;
  }
  for (int i = 0; i < n; ++i) {
    cout << find_index(xs[i], 0, m-1) << ' ';
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
