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

int n, m, d;
int board[15][15];
int pan[15][15];
bool visited[15][15];
int a, b, c;
int dy[3] = {0, -1, 0};
int dx[3] = {-1, 0, 1};

void get_input() {
  cin >> n >> m >> d;
  FOR2(n, m) cin >> board[i][j];
}

int cal_dist(pair<int ,int> a, pair<int, int> b) {
  return abs(a.first-b.first) + abs(a.second-b.second);
}

bool is_range(int y, int x) {
  if (y >= n || y < 0) return false;
  if (x >= m || x < 0) return false;
  return true;
}

void kill_enemy(int archer) {
  int nx, ny;
  queue<pair<int, int>> q;
  pair<int, int> cur;

  for (int i = 0; i < n; ++i)
    for (int j=0; j<m; ++j)
      visited[i][j] = false;

  if (pan[n-1][archer]) {
    pan[n-1][archer] = 2;
    return;
  }
  q.push(make_pair(n-1, archer));
  visited[n-1][archer] = true;
  while(!q.empty()) {
    cur = q.front();
    q.pop();
    if (pan[cur.first][cur.second]) {
      pan[cur.first][cur.second] = 2;
      return;
    }
    if (abs(cur.first - n) + abs(cur.second - archer) <= d-1) {
      for (int i = 0; i < 3; ++i) {
        ny = cur.first + dy[i];
        nx = cur.second + dx[i];
        if (is_range(ny, nx) && !visited[ny][nx]) {
          pair<int, int> tmp = make_pair(ny, nx);
          visited[ny][nx] = true;
          q.push(tmp);
        }
      }
    }
  }
}

void next_board() {
  for (int i=n-2; i>=0; --i)
    for (int j=m-1; j>=0; --j)
      pan[i+1][j] = pan[i][j];

  for (int i = 0; i < n; ++i)
    pan[0][i] = 0;
}

int simulate() {
  int rst = 0;
  for (int i=0; i<n; ++i) for (int j=0; j<m; ++j)
      pan[i][j] = board[i][j];
  for (int i = 0; i < n; ++i) {
    kill_enemy(a);
    kill_enemy(b);
    kill_enemy(c);

    for (int i=0; i<n; ++i) {
      for (int j=0; j<m; ++j) {
        if (pan[i][j] >= 2) {
          pan[i][j] = 0;
          rst++;
        }
      }
    }
    next_board();
  }
  return rst;
}

void solve() {
  int rst = 0x80000000;
  for (a=0; a<m-2; ++a) {
    for (b=a+1; b<m-1; ++b) {
      for (c=b+1; c<m; ++c) {
        rst = max(simulate(), rst);
      }
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
