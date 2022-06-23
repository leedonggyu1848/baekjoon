#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321
#define MAXN 1024

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN, gM;
int gMap[MAXN][MAXN];
int gRowAcc[MAXN][MAXN],gColAcc[MAXN][MAXN];
int gAcc[MAXN][MAXN];

void getInput() {
  cin >> gN >> gM;
  for (int i=0; i<gN; ++i) for(int j=0; j<gN; ++j)
    cin >> gMap[i][j];
}

void fillAcc() {
  FOR(gN) {
    gRowAcc[i][0] = gMap[i][0];
    gColAcc[0][i] = gMap[0][i];
  }
  for (int i=0; i<gN; ++i) for (int j=1; j<gN; ++j) {
    gRowAcc[i][j] = gMap[i][j] + gRowAcc[i][j-1];
    gColAcc[j][i] = gMap[j][i] + gColAcc[j-1][i];
  }
  memset(gAcc, -1, sizeof(gAcc));
  FOR(gN) {
    gAcc[i][0] = gColAcc[i][0];
    gAcc[0][i] = gRowAcc[0][i];
  }
}

int getAcc(const pii& pos) {
  int y = pos.first;
  int x = pos.second;
  int& ret = gAcc[y][x];
  if (ret != -1) return ret;
  return ret = getAcc(make_pair(y-1,x-1)) + gRowAcc[y][x] + gColAcc[y][x] - gMap[y][x] ;
}

int getLeftRect(const pii& p1, const pii& p2) {
  return getAcc(make_pair(p2.first, p1.second-1));
}

int getLowerRect(const pii& p1, const pii& p2) {
  return getAcc(make_pair(p1.first-1, p2.second));
}

int getAccRect(const pii& p1, const pii& p2) {
  if (p1 == make_pair(0, 0)) return getAcc(p2);
  if (p1.first == 0) return getAcc(p2) - getLeftRect(p1, p2);
  if (p1.second == 0) return getAcc(p2) - getLowerRect(p1, p2);
  return getAcc(p2) - getLeftRect(p1, p2) - getLowerRect(p1, p2) + getAcc(make_pair(p1.first-1, p1.second-1));
}

void solve() {
  pii a, b;
  fillAcc();
  FOR(gM) {
    cin >> a.first >> a.second >> b.first >> b.second;
    a.first--;
    a.second--;
    b.first--;
    b.second--;
    cout << getAccRect(a, b) << '\n';
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}