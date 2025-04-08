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

int n;
long long arr[2000];

void get_input() {
  cin >> n;
  FOR(n)
    cin >> arr[i];
}


void solve() {
  int rst = 0;
  int sum, start, end;
  sort(arr, arr+n);
  for (int tar=0; tar<n; ++tar) {
    start = 0;
    end = n-1;
    while (start < end) {
      if (start == tar) {
        start++;
        continue;
      }
      if (end == tar) {
        end--;
        continue;
      }
      sum = arr[start] + arr[end];
      if (arr[tar] == sum) {
        rst++;
        break;
      }
      if (arr[tar] > sum) start++;
      else end--;
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
