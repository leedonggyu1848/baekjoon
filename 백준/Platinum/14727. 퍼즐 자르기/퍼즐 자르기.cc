#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

int gN;
int gArr[100001];

void getInput() {
  cin >> gN;
  FOR(gN) cin >> gArr[i];
}

ll containMid(int left, int right) {
  int mid = (left + right) / 2;
  int lo = mid, hi = mid+1;
  ll height = min(gArr[lo], gArr[hi]);
  ll answer = height * 2;
  while (left < lo || hi < right) {
    if (hi < right && (lo == left || gArr[lo-1] < gArr[hi+1])) {
      ++hi;
      height = min<ll>(height, gArr[hi]);
    } else {
      --lo;
      height = min<ll>(height, gArr[lo]);
    }
    answer = max(answer, height * (hi - lo + 1));
  }
  return answer;
}

ll getBiggestRect(int left, int right) {
  if (left == right) return gArr[left];
  int mid = (left+right)/2;
  ll answer = max(getBiggestRect(left, mid), getBiggestRect(mid+1, right));
  answer = max(answer, containMid(left, right));
  return answer;
}

void solve() {
  cout << getBiggestRect(0, gN-1) << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}