#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;

#define NMAX 500001

int gN;
int gArr[NMAX];
int gBuff[NMAX];

void getInput() {
  cin >> gN;
  FOR(gN) cin >> gArr[i];
}

long long countAndMerge(int start, int end) {
  long long ret = 0;
  int mid = (start + end) / 2;
  int s1 = start;
  int s2 = mid+1;
  int cur = start;

  while (s1 <= mid && s2 <= end) {
    if (gArr[s1] > gArr[s2]) gBuff[cur++] = gArr[s2++];
    else {
      ret += cur - s1;
      gBuff[cur++] = gArr[s1++];
    }
  }
  while (s1 <= mid) {
    ret += cur - s1;
    gBuff[cur++] = gArr[s1++];
  }
  while (s2 <= end) gBuff[cur++] = gArr[s2++];

  for (int i=start; i<=end; ++i)
    gArr[i] = gBuff[i];

  return ret;
}

long long countSwapWithMergeSort(int start, int end) {
  if (start >=  end) return 0;
  int mid = (start + end) / 2;
  long long ret = 0;
  ret += countSwapWithMergeSort(start, mid);
  ret += countSwapWithMergeSort(mid+1, end);
  ret += countAndMerge(start, end);
  return ret;
}

void solve() {
  cout << countSwapWithMergeSort(0, gN-1) << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}