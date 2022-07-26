#include <bits/stdc++.h>

using namespace std;

#define FOR(N) for(int i=0; i<(N); ++i)
#define FOR2(N, M) for (int i=0; i<(N); ++i) for (int j=0; j<(M); ++j)
#define INF 987654321

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

ll gAsset;
ll gRequirement;
ll gLans[10001];
ll gMax;

void getInput() {
  gMax = -1;
  cin >> gAsset >> gRequirement;
  FOR(gAsset) {
    cin >> gLans[i];
    gMax = max(gLans[i], gMax);
  }
}

ll cntCuttableLan(ll length){
  ll ret = 0;
  FOR(gAsset)
    ret += gLans[i] / length;
  return ret;
}

void solve() {
  ll left = 1;
  ll right = gMax;
  ll mid = (left + right) / 2;
  ll numLan = 0;
  ll result = -1;
  while (left <= right){
    mid = (left + right)/2;
    numLan = cntCuttableLan(mid);
    if (numLan >= gRequirement) {
      left = mid+1;
      result = max(result, mid);
    }
    else right = mid-1;
  }
  cout << result << '\n';
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  getInput();
  solve();
  return 0;
}