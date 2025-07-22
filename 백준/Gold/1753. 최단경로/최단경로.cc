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
#define INF 0x3f3f3f3f

typedef vector<int> vi;
typedef pair<int, int> pii;

#define MAX_V 20000

struct edge {
  int e, cost;
};

struct cmp {
  bool operator()(edge a, edge b) {
    return a.cost > b.cost;
  };
};

int nv, ne, start_node;
int dist[MAX_V + 1];
vector<edge> edges[MAX_V+1];

void get_input() {
  cin >> nv >> ne >> start_node;
  int s, e, cost;
  while (ne--) {
    cin >> s >> e >> cost;
    edges[s].push_back(edge{ e, cost });
  }
}

void solve() {
  priority_queue<edge, vector<edge>, cmp> pq;
  edge cur;

  for (int i = 1; i <= nv; ++i) dist[i] = INF;
  dist[start_node] = 0;
  pq.push(edge { start_node, 0 });
  while (!pq.empty()) {
    cur =  pq.top(); pq.pop();
    if (dist[cur.e] != cur.cost) continue;
    for (edge nxt : edges[cur.e]) {
      if (dist[nxt.e] > dist[cur.e] + nxt.cost) {
        dist[nxt.e] = dist[cur.e] + nxt.cost;
        pq.push(edge { nxt.e, dist[nxt.e] });
      }
    }
  }
  for (int i = 1; i <= nv; ++i) {
    if (dist[i] == INF) cout << "INF\n";
    else cout << dist[i] << '\n';
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
