#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN, gM;
int gArr1[101][101], gArr2[101][101];

void getInput() {
  cin >> gN >> gM;
  for(int i=0; i<gN; ++i) for (int j=0; j<gM; ++j) cin >> gArr1[i][j];
  for(int i=0; i<gN; ++i) for (int j=0; j<gM; ++j) cin >> gArr2[i][j];
}

void solve() {
  for(int i=0; i<gN; ++i) {
    for (int j=0; j<gM; ++j) {
      cout << gArr1[i][j] + gArr2[i][j] << ' ';
    }
    cout << '\n';
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