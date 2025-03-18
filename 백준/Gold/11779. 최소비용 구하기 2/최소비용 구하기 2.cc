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

#define MAX_V 1000

struct edge {
  int e, cost;
};

struct cmp {
  bool operator()(edge& a, edge& b) {
    return a.cost > b.cost;
  };
};

int nv, start_node, dest_node;
vector<edge> adj[MAX_V+1];
int pre[MAX_V+1];
int dist[MAX_V+1];

void get_input() {
  int start, end, cost, ne;
  cin >> nv >> ne;
  while (ne--) {
    cin >> start >> end >> cost;
    adj[start].push_back(edge{end, cost});
  }
  cin >> start_node >> dest_node;
  for (int i = 1; i <= nv; ++i) {
    pre[i] = start_node;
    dist[i] = INF;
  }
  dist[start_node] = 0;
}

void print_path() {
  stack<int> s;
  int cnt = 1;
  s.push(dest_node);
  int cur = dest_node;
  while (cur != start_node) {
    s.push(pre[cur]);
    cur = pre[cur];
    cnt++;
  }
  cout << cnt << '\n';
  while (!s.empty()) {
    cout << s.top() << ' ';
    s.pop();
  }
}

void solve() {
  edge cur;
  priority_queue<edge, vector<edge>, cmp> pq;
  pq.push(edge{ start_node, 0 });
  while (!pq.empty()) {
    cur = pq.top(); pq.pop();
    if (cur.cost != dist[cur.e]) continue;
    for (edge next: adj[cur.e]) {
      if (dist[next.e] > dist[cur.e] + next.cost) {
        dist[next.e] = dist[cur.e] + next.cost;
        pre[next.e] = cur.e;
        pq.push(edge{ next.e, dist[next.e] });
      }
    }
  }
  cout << dist[dest_node] << '\n';
  print_path();
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
