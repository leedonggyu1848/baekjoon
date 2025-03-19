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

#define MAX_N 300

struct edge {
  int v, cost;
};

struct cmp {
  bool operator()(edge& a, edge& b) {
    return a.cost > b.cost;
  };
};

int n;
int link[MAX_N][MAX_N];
int hole[MAX_N];
bool visited[MAX_N];

void get_input() {
  cin >> n;
  FOR(n) {
    cin >> hole[i];
    visited[i] = false;
  }
  FOR2(n, n) cin >> link[i][j];
}

void solve() {
  int rst = 0, cnt = 0;
  priority_queue<edge, vector<edge>, cmp> pq;
  edge cur;
  FOR(n) pq.push(edge { i, hole[i] });
  while (cnt != n) {
    cur = pq.top();
    pq.pop();
    if (visited[cur.v]) continue;
    cnt++;
    rst += cur.cost;
    visited[cur.v] = true;
    FOR(n)
      if (!visited[i]) pq.push (edge{ i, link[cur.v][i] });
  }
  cout << rst;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
