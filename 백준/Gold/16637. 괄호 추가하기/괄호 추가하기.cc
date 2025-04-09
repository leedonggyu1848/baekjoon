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

int n, c_num, c_sign;
int nums[20];
char sign[20];
bool brace[20];
int answer = 0x80000000;

void get_input() {
  cin >> n;
  bool is_sign = false;
  char c;
  FOR(n) {
    cin >> c;
    if (is_sign) {
      sign[c_sign++] = c;
    } else {
      nums[c_num++] = c-'0';
    }
    is_sign = !is_sign;
  }

}

int cal_segment(char c, int a, int b) {
  switch (c) {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
  }
  return 0;
}

int cal_rst() {
  int rst = 0;
  queue<int> q;
  for (int i = 0; i < c_sign; ++i) {
    if (brace[i]) {
      q.push(cal_segment(sign[i], nums[i], nums[i+1]));
    } else if (i == 0 || !brace[i-1]) {
        q.push(nums[i]);
      }
    }
  if (!brace[c_sign-1]) q.push(nums[c_sign]);

  rst = q.front();
  q.pop();
  for (int i = 0; i < c_sign && !q.empty(); ++i) {
    while (i<c_sign && !brace[i] && !q.empty()) {
      rst = cal_segment(sign[i], rst, q.front());
      ++i;
      q.pop();
    }
  }
  return rst;
}

void search(int cur) {
  if (cur == c_sign) {
    answer = max(answer, cal_rst());
    return;
  }
  if (cur == 0 || !brace[cur-1]) {
    brace[cur] = true;
    search(cur+1);
  }
  brace[cur] = false;
  search(cur+1);
}

void solve() {
  search(0);
  cout << answer << '\n';
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  get_input();
  solve();
  return 0;
}
