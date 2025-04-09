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
int paper[5][5];
bool used[5][5];
int rst = -1;
int ldy[4] = {0,0,-1,1};
int ldx[4] = {-1,-1,0,0};
int rdy[4] = {1,-1,0,0};
int rdx[4] = {0,0,1,1};

void get_input() {
  cin >> n >> m;
  FOR2(n, m) cin >> paper[i][j];
}

bool can_go(int y, int x) {
  if (y<0 || y>=n || x<0 || x>=m) return false;
  if (used[y][x]) return false;
  return true;
}

void dfs(int y, int x, int v) {
  int ny, nx;
  int ry,rx,ly,lx;
  if (y == n) {
    rst = max(rst, v);
    return;
  }
  if (x == m-1) {
    nx=0;
    ny=y+1;
  } else {
    nx=x+1;
    ny=y;
  }
  dfs(ny, nx, v);
  if (used[y][x]) return;
  for (int i = 0; i < 4; ++i) {
    ly=y+ldy[i];
    lx=x+ldx[i];
    ry=y+rdy[i];
    rx=x+rdx[i];
    if (can_go(ly, lx) && can_go(ry,rx)) {
      used[ly][lx] = used[ry][rx] = used[y][x] = true;
      dfs(ny, nx, v+paper[y][x]*2+paper[ly][lx]+paper[ry][rx]);
      used[ly][lx] = used[ry][rx] = used[y][x] = false;
    }
  }
}

void solve() {
  dfs(0, 0, 0);
  cout << rst;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
