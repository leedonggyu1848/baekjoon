#include <cstdio>
#include <iostream>
using namespace std;

#define NEXT(bf,a,b) ((bf)*(a)+(b))

int n;
int seq[51];

void getInput() {
  scanf("%d\n", &n);
  for (int i=0; i<n; ++i)
    scanf("%d ", &seq[i]);
}

bool check(int a, int b) {
  for (int i=0; i<n-1; ++i) {
    if (seq[i+1] != NEXT(seq[i], a, b))
      return false;
  }
  return true;
}

void solve() {
  int tmp1, tmp2;
  int a, b;

  if (n == 1) {
    printf("A\n");
    return ;
  }
  if (n == 2) {
    if (seq[0] == seq[1])
      printf("%d\n", seq[0]);
    else
      printf("A\n");
    return ;
  }
  tmp1 = seq[1] - seq[0];
  tmp2 = seq[2] - seq[1];
  a = tmp1 == 0 ? 0 : tmp2/tmp1;
  b = tmp1 - (seq[0] * (a-1));
  check(a, b) ? printf("%d\n", NEXT(seq[n-1], a, b)) : printf("B\n");
}

int main() {
  getInput();
  solve();
}