#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN, gM, gB;
int gBlocks[501][501];
int gMin, gMax, gTotal;

void getInput() {
  cin >> gN >> gM >> gB;
  gMin = 0;
  gMax = 256;
  gTotal = gB;
  for (int i=0; i<gN; ++i) for (int j=0; j<gM; ++j) {
    cin >> gBlocks[i][j];
    gMin = min(gMin, gBlocks[i][j]);
    gMax = max(gMax, gBlocks[i][j]);
    gTotal += gBlocks[i][j];
  }
  gMax = min(gMax, gTotal / (gN*gM));
}

void solve() {
  int rst = INF;
  int height = 0;
  int temp, block;
  for (int t=gMin; t<=gMax; ++t) {
    temp = 0;
    for (int i=0; i<gN; ++i) for (int j=0; j<gM; ++j) {
      block = gBlocks[i][j];
      if (t > block) temp += t - block;
      else if (t < block) temp += (block - t)*2;
    }
    if (rst >= temp){
      rst = temp;
      height = t;
    }
  }
  cout << rst << ' ' << height << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}