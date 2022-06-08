#include <iostream>
#include <cstring>
using namespace std;

#define MAXINUM 16

int g_n;
int g_guiltiness[MAXINUM];
int g_degree[MAXINUM][MAXINUM];
int g_mafia;

void getInput() {
  scanf("%d\n", &g_n);
  for (int i=0; i<g_n; ++i)
    scanf("%d ", &g_guiltiness[i]);
  for (int i=0; i<g_n; ++i)
    for (int j=0; j<g_n; ++j)
      scanf("%d ", &g_degree[i][j]);
  scanf("%d\n", &g_mafia);
}

void killSurvivors(int idx, bool survivors[MAXINUM]) {
  for (int i = 0; i < g_n; ++i)
    g_guiltiness[i] += g_degree[idx][i];
  survivors[idx] = false;
}

void saveSurvivors(int idx, bool survivors[MAXINUM]) {
  for (int i = 0; i < g_n; ++i)
    g_guiltiness[i] -= g_degree[idx][i];
  survivors[idx] = true;
}

int electeSurvior(bool survivors[MAXINUM]) {
  int elected = -1;
  int maxGuiltiness = 0;
  for (int i=0; i<g_n; ++i){
    if (survivors[i]){
      if (maxGuiltiness < g_guiltiness[i]){
        elected = i;
        maxGuiltiness = max(maxGuiltiness, g_guiltiness[i]);
      }
    }
  }
  survivors[elected] = false;
  return elected;
}

int getTheMostVimtims(bool survivors[MAXINUM], int numSurvivors) {
  int ret = 0;
  int elected = -1;
  if (numSurvivors % 2){
    elected = electeSurvior(survivors);
    if (elected != g_mafia)
      ret = max(ret, getTheMostVimtims(survivors, numSurvivors-1));
    survivors[elected] = true;
  } else {
    for (int i=0; i<g_n; ++i) {
      if (survivors[i] && g_mafia != i) {
        killSurvivors(i, survivors);
        if (elected != g_mafia)
          ret = max(ret, getTheMostVimtims(survivors, numSurvivors-1)+1);
        saveSurvivors(i, survivors);
      }
    }
  }
  return ret;
}

void solve() {
  bool survivors[MAXINUM];
  memset(survivors, 1, sizeof(survivors));
  printf("%d\n", getTheMostVimtims(survivors, g_n));
}

int main() {
  getInput();
  solve();
  return 0;
}