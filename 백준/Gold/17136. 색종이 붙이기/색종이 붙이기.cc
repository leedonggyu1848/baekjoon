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

int paper[10][10];
int cnt_paper[6] = {0, 5, 5, 5, 5, 5};
int g_cnt = INF;

void get_input() {
  FOR2(10, 10) cin >> paper[i][j];
}

void detach_paper(int y, int x, int type) {
  for (int i = 0; i < type; ++i) {
    for(int j = 0; j < type; ++j) {
      paper[y+i][x+j] = 1;
    }
  }
}

void attache_paper(int y, int x, int type) {
  for (int i = 0; i < type; ++i) {
    for(int j = 0; j < type; ++j) {
      paper[y+i][x+j] = 0;
    }
  }
}

bool is_valid(int y, int x) {
  if (y < 0 || y >= 10 || x < 0 || x >= 10) return false;
  if (paper[y][x] != 1) return false;
  return true;
}

bool has_space(int y, int x, int type) {
  for (int i = 0; i < type; ++i) {
    for(int j = 0; j < type; ++j) {
      if(!is_valid(y+i, x+j)) return false;
    }
  }
  return true;
}

bool is_all_zero() {
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; ++j) {
      if (paper[i][j] == 1) return false;
    }
  }
  return true;
}

void dfs(int y, int x, int rst) {
  int ny, nx;
  if (rst > g_cnt) return;
  if (y == 10) {
    if (is_all_zero()) {
      g_cnt = min(g_cnt, rst);
    }
    return;
  }
  if (x == 9) {
    ny = y+1; nx = 0;
  } else {
    ny = y; nx = x+1;
  }
  if (paper[y][x] == 0) dfs(ny, nx, rst);
  else {
    for (int type=5; type>=1; --type) {
      if (cnt_paper[type] == 0) continue;
      if (has_space(y, x, type)) {
        attache_paper(y, x, type);
        cnt_paper[type]--;
        dfs(ny, nx, rst+1);
        detach_paper(y, x, type);
        cnt_paper[type]++;
      }
    }
  }
}

void solve() {
  dfs(0, 0, 0);
  if (g_cnt == INF) cout << -1;
  else cout << g_cnt;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
