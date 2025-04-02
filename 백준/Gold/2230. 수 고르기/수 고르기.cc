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
int nums[100000];

void get_input() {
  cin >> n >> m;
  FOR(n) cin >> nums[i];
}


void solve() {
  sort(nums, nums+n);
  int start=0, end=1;
  int rst = INF;
  while (end < n) {
    if (nums[end] - nums[start] < m) {
      end++;
      continue;
    }
    rst = min(rst, nums[end]-nums[start]);
    if (start == end-1) end++;
    else start++;
  }
  cout << rst;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
