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

#define MAX_N 600

int n;
int h[MAX_N];

void get_input() {
  cin >> n;
  FOR(n) cin >> h[i];
}

void solve() {
  sort(h, h+n);
  int rst = INF;
  int left, right;
  int rgap, lgap;
  for (int start = 0; start < n-1; ++start) {
    for (int end = n-1; start < end; --end) {
      left = start+1;
      right = end-1;
      while (left < right) {
        lgap = h[left] - h[start];
        rgap = h[end] - h[right];
        rst = min(rst, abs(lgap-rgap));
        if (lgap > rgap)  right--;
        else left++;
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
