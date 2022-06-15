#include <cstdlib>
#include <sched.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <utility>

#define FOR(N) for(int i=0; i<(N); ++i)
#define MAXN 2188

using namespace std;
typedef pair<int, int> pii;

int gN;
int gMx[MAXN][MAXN];

void getInput() {
  scanf("%d\n", &gN);
  for(int i=0; i<gN; ++i)
    for (int j=0; j<gN; ++j)
      scanf("%d ", &gMx[i][j]);
}

bool areSellsAllSameColor(const pii& start, const pii& end) {
  int target = gMx[start.first][start.second];
  for (int i=start.first; i <= end.first; ++i)
    for (int j=start.second; j <= end.second; ++j)
      if(gMx[i][j] != target)
        return false;
  return true;
}

void countPaper(int answer[3], const pii& start, const pii& end) {
  int sidelength = end.first - start.first + 1;
  int nextSidelength = sidelength/3;
  int nextFirst, nextSecond;
  if (areSellsAllSameColor(start, end))
    answer[gMx[start.first][start.second]+1]++;
  else {
    for (int i=0; i<3; ++i) {
      for (int j=0; j<3; ++j){
        nextFirst = start.first + nextSidelength*i;
        nextSecond = start.second + nextSidelength*j;
        countPaper(answer, make_pair(nextFirst, nextSecond), make_pair(nextFirst+nextSidelength-1, nextSecond+nextSidelength-1));
      }
    }
  }
}

void solve() {
  int answer[3];
  memset(answer, 0, sizeof(answer));
  countPaper(answer, make_pair(0, 0), make_pair(gN-1, gN-1));
  FOR(3) printf("%d\n", answer[i]);
}

int main() {
  getInput();
  solve();
  return 0;
}
