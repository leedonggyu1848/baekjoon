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

string makeProgram(int n, int slot) {
  if (slot == 1)
    return n == 1 ? "#" : ".";

  int nextSlot = slot >> 1;
  int halfNextSlot = nextSlot >> 1;
  string ret;
  if (n <= halfNextSlot + nextSlot)
    ret = makeProgram(n-halfNextSlot, nextSlot) + makeProgram(halfNextSlot, halfNextSlot) + string(halfNextSlot, '.');
  else
    ret = makeProgram(nextSlot, nextSlot) + makeProgram(n-nextSlot, nextSlot);
  return ret;
}

int multiplyTwo(int dest) {
  int ret = 1;
  for(; ret<dest; ret<<=1);
  return ret;
}

void solve() {
  cout << makeProgram(gN, multiplyTwo(gN)) << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}