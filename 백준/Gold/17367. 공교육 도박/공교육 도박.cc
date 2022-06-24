#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN;
double gCache[6][6][1001];
double gPrize[6][6][6];
double gNan;

void getInput() {
  cin >> gN;
}

double calPrize(int a, int b, int c) {
  double &ret = gPrize[a][b][c];
  a++;b++;c++;
  if (a == b && b == c) ret = 10000+a*1000;
  else if (a == b) ret = 1000+a*100;
  else if (b == c) ret = 1000+b*100;
  else if (c == a) ret = 1000+c*100;
  else ret = max(max(a, b),c) * 100;
  return ret;
}

void fillCache() {
  double acc;
  for (int i=0;i<6;++i) for(int j=0;j<6;++j) {
    acc = 0;
    for(int k=0;k<6;++k) acc += calPrize(i, j, k);
    gCache[i][j][0] = acc/6;
  }
}


void solve() {
  double acc;
  fillCache();
  for (int n=1; n<gN-2; ++n) {
    for (int b=0; b<6; ++b) {
      for (int cur=0; cur<6; ++cur) {
        acc=0;
        for (int a=0; a<6; ++a) acc+=max(gPrize[a][b][cur], gCache[a][b][n-1]);
        gCache[b][cur][n] = acc / 6;
      }
    }
  }
  acc = 0;
  for (int i=0; i<6; ++i) for(int j=0;j <6; ++j)
    acc += gCache[i][j][gN-3];
  cout.precision(12);
  cout << fixed;
  cout << acc / 36 << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}