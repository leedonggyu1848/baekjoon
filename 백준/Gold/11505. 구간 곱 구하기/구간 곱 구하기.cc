#include <iostream>
#include <algorithm>
#define MAX_INT 0x7FFFFFFF
#define MAX_N 1000000
#define MOD 1000000007

using namespace std;

long long tree[MAX_N * 4];
long long arr[MAX_N];

int left_child(int n) {
  return n * 2 + 1;
}

int right_child(int n) {
  return n * 2 + 2;
}

long long init(int n, int e_start, int e_end) {
  if (e_start == e_end) return tree[n] = arr[e_start];
  int mid = (e_start + e_end) / 2;
  long long left = init(left_child(n), e_start, mid);
  long long right = init(right_child(n), mid+1, e_end);
  return tree[n] = (left * right) % MOD;
}

long long cal(int left, int right, int n, int e_start, int e_end) {
  if (right < e_start || e_end < left) return 1;
  if (e_start <= left && right <= e_end) return tree[n];
  int mid  = (left + right) / 2;
  long long lvalue = cal(left, mid, left_child(n), e_start, e_end);
  long long rvalue = cal(mid+1, right, right_child(n), e_start, e_end);
  return (lvalue * rvalue) % MOD;
}

long long update(int left, int right, int n, int target, int value) {
  if (target < left || right < target) return tree[n];
  if (left == right) return tree[n] = value;
  int mid = (left + right) / 2;
  long long lvalue = update(left, mid, left_child(n), target, value);
  long long rvalue = update(mid+1, right, right_child(n), target, value);
  return tree[n] = (lvalue * rvalue) % MOD;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int N, M, K;
  int type, v1, v2;

  cin >> N >> M >> K;

  for (int i = 0; i < N; ++i) { cin >> arr[i]; }
  init(0, 0, N-1);
  for (int i = 0; i < M + K; ++i) {
    cin >> type >> v1 >> v2;
    if (type == 1) {
      update(0, N-1, 0, v1 - 1, v2);
    } else if (type == 2) {
      cout << cal(0, N-1, 0, v1 - 1, v2 - 1) << '\n';
    }
  }
  return 0;
}
