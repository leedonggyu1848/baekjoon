#include <cstdlib>
#include <string>
#include <sched.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <utility>

#define FOR(N) for(int i=0; i<(N); ++i)
#define MAXN 129

using namespace std;
typedef pair<int, int> pii;

int gN;
bool gMx[MAXN][MAXN];

void getInput() {
  string s;
  scanf("%d\n", &gN);
  for(int i=0; i<gN; ++i){
    cin >> s;
    for (int j=0; j<gN; ++j){
      gMx[i][j] = s[j] == '1';
    }
  }
}

bool areSellsAllSame(const pii& start, const pii& end) {
  bool target = gMx[start.first][start.second];
  for (int i=start.first; i <= end.first; ++i)
    for (int j=start.second; j <= end.second; ++j)
      if(gMx[i][j] != target) return false;
  return true;
}

string quadTree(const pii& start, const pii& end) {
  int sidelength = end.first - start.first + 1;
  int nextSidelength = sidelength/2;
  int nextFirst, nextSecond;
  string ret;
  if (areSellsAllSame(start, end))
    return gMx[start.first][start.second] ? "1" : "0";
  else {
    ret = "(";
    for (int i=0; i<2; ++i) {
      for (int j=0; j<2; ++j){
        nextFirst = start.first + nextSidelength*i;
        nextSecond = start.second + nextSidelength*j;
        ret += quadTree(make_pair(nextFirst, nextSecond), make_pair(nextFirst+nextSidelength-1, nextSecond+nextSidelength-1));
      }
    }
    ret += ")";
    return ret;
  }
}

void solve() {
  cout <<  quadTree(make_pair(0, 0), make_pair(gN-1, gN-1)) << endl;
}

int main() {
  getInput();
  solve();
  return 0;
}