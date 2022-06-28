#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

int gN;

void getInput() {
  cin >> gN;
}

void solve() {
  int div;
  int rst = 0;
  for (; gN; gN/=10) {
    div = gN%10;
    rst += div*div*div*div*div;
  }
  cout << rst << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}