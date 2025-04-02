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

int n, k;
int arr[200000];
int cache[100001];

void get_input() {
  cin >> n >> k;
  FOR(n) cin >> arr[i];
}

void add_cache(int idx, int& cnt_over) {
  cache[idx]++;
  if (cache[idx] > k)
    cnt_over++;
}

void submit_cache(int idx, int& cnt_over) {
  cache[idx]--;
  if (cache[idx] == k) {
    cnt_over--;
  }
}

void solve() {
  int cnt_over = 0;
  int rst = 0;
  int start=0, end=0;
  add_cache(arr[0], cnt_over);
  if (cnt_over == 0) rst = max(rst, end-start+1);
  while (end < n) {
    if (start <= end && cnt_over == 0) rst = max(rst, end-start+1);
    if (end < start || cnt_over == 0) {
      end++;
      add_cache(arr[end], cnt_over);
    } else {
      submit_cache(arr[start], cnt_over);
      start++;
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
