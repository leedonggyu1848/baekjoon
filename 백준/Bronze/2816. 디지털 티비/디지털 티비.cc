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

int n, kbs1, kbs2;

void get_input() {
  string ch;
  cin >> n;
  FOR(n) {
    cin >> ch;
    if (ch == "KBS1") kbs1 = i;
    else if(ch == "KBS2") kbs2 = i;
  }
}


void solve() {
  int cur = 0;
  if (kbs1 != 0) {
    while (cur != kbs1) {
      cout << '1';
      cur++;
    }
    while (kbs1 != 0) {
      cout << '4';
      cur--;
      kbs1--;
      if (cur == kbs2) kbs2++;
    }
  }
  if (kbs2 != 1) {
    while (cur != kbs2) {
      cout << '1';
      cur++;
    }
    while (kbs2 != 1) {
      cout << '4';
      cur--;
      kbs2--;
    }
  }
  cout << '\n';
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
