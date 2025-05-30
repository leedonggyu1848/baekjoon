#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int SIZE = 1000001;
int tree[SIZE*4];

int left_child(int i) {
    return i * 2 + 1;
}

int right_child(int i) {
    return i * 2 + 2;
}

int update(int v, int tar, int left, int right, int idx) {
    if (tar < left || right < tar) return -1;
    if (left == right) {
        tree[idx] = max(tree[idx], v);
        return tree[idx];
    }
    int mid = (left + right) / 2;
    int left_v = update(v, tar, left, mid, left_child(idx));
    int right_v = update(v, tar, mid + 1, right, right_child(idx));
    tree[idx] = max(max(left_v, right_v), tree[idx]);
    return tree[idx];
}

int select(int lo, int hi, int left, int right, int idx) {
    if (hi < left || right < lo) return 0;
    if (lo <= left && right <= hi) {
      return tree[idx];
    }
    int mid = (left + right) / 2;
    int left_v = select(lo, hi, left, mid, left_child(idx));
    int right_v = select(lo, hi, mid+1, right, right_child(idx));
    return max(left_v, right_v);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums) cin >> x;

    for (int num : nums) {
        int max_val = select(0, num-1, 0, SIZE-1, 0) + 1;
        update(max_val, num, 0, SIZE-1, 0);
    }
    cout << select(0, SIZE-1, 0, SIZE-1, 0);
    return 0;
}
