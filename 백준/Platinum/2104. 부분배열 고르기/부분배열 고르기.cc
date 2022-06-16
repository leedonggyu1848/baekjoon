#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

#define MAXN 100001

int gN;
int gArr[MAXN];

void getInput() {
  cin >> gN;
  FOR(gN) cin >> gArr[i];
}

long long containMid(int left, int right) {
  int mid = (left + right) / 2;
  int lo = mid, hi = mid+1;
  int minValue = INF;
  long long acc = 0;
  long long answer = -1;

  while (lo >= left && hi <= right) {
    if (gArr[lo] > gArr[hi]) {
      minValue = min(minValue,gArr[lo]);
      acc += gArr[lo];
      lo--;
    } else {
      minValue = min(minValue,gArr[hi]);
      acc += gArr[hi];
      hi++;
    }
    answer = max(answer, acc * minValue);
  }
  while (lo >= left) {
      minValue = min(minValue,gArr[lo]);
      acc += gArr[lo];
      lo--;
      answer = max(answer, acc * minValue);
  }
  answer = max(answer, acc * minValue);
  while (hi <= right) {
      minValue = min(minValue,gArr[hi]);
      acc += gArr[hi];
      hi++;
      answer = max(answer, acc * minValue);
  }

  return answer;
}

int searchMaximumScore(int left, int right, long long& answer, long long& acc) {
  if (left == right){
    acc = gArr[left];
    answer = max(answer, acc * gArr[left]);
    return gArr[left];
  }
  int mid = (left + right) / 2;
  long long leftAcc = 0, rightAcc = 0;
  int minValue = min(searchMaximumScore(left, mid, answer, leftAcc), searchMaximumScore(mid+1, right, answer, rightAcc));
  acc = leftAcc + rightAcc;
  answer = max(answer, acc * minValue);
  answer = max(answer, containMid(left, right));
  return minValue;
}

void solve() {
  long long answer = -1;
  long long _ = 0;
  searchMaximumScore(0, gN-1, answer, _);
  cout << answer << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}
