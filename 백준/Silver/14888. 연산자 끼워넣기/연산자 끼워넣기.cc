#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

#define MAXN 11
#define NUM_OPERATORS 4
#define INF 987654321
#define FOR(N) for(int i=0; i<(N); ++i)

int gN;
int gSeq[MAXN];
int gOpCnt[4];

enum { ADD=0, SUB, MUL, DIV };
enum { MAXIMUM=0, MINIMUM };

int _add(int a, int b) { return a+b; }
int _sub(int a, int b) { return a-b; }
int _mul(int a, int b) { return a*b; }
int _div(int a, int b) { return a/b; }

int(*gOperators[NUM_OPERATORS])(int,int) = {
  _add, _sub, _mul, _div
};

void getInput() {
  scanf("%d\n", &gN);
  FOR(gN) scanf("%d\n", &gSeq[i]);
  FOR(NUM_OPERATORS) scanf("%d\n", &gOpCnt[i]);
}

void findAnswer(int answer[2], int cur, int idx) {
  if (idx == gN){
    answer[MAXIMUM] = max(answer[MAXIMUM], cur);
    answer[MINIMUM] = min(answer[MINIMUM], cur);
  }

  FOR(NUM_OPERATORS) {
    if (gOpCnt[i] > 0){
      gOpCnt[i]--;
      findAnswer(answer, gOperators[i](cur, gSeq[idx]), idx+1);
      gOpCnt[i]++;
    }
  }
}

void solve() {
  int answer[2];
  answer[MAXIMUM] = -INF;
  answer[MINIMUM] = INF;
  findAnswer(answer, gSeq[0], 1);
  printf("%d\n%d\n", answer[MAXIMUM], answer[MINIMUM]);
}

int main() {
  getInput();
  solve();
  return 0;
}
