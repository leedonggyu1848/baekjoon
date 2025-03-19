#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

class Tree {
public:
    Tree *left = nullptr;
    Tree *right = nullptr;
    bool wolf = false; // true: 늑대, false: 양
};

void traversal(deque<Tree>& q, int& answer, int& wolf, int& sheep) {
    int candidate = q.size();
    while (candidate--) {
        Tree cur = q.front();
        q.pop_front();
        if (cur.wolf) wolf++;
        else sheep++;
        if (wolf < sheep) {
            if (answer < sheep) answer = sheep;
            if (cur.left) q.push_back(*cur.left);
            if (cur.right) q.push_back(*cur.right);
            traversal(q, answer, wolf, sheep);
            if (cur.left) q.pop_back();
            if (cur.right) q.pop_back();
        }
        if (cur.wolf) wolf--;
        else sheep--;
        q.push_back(cur);
    }
}

int solution(vector<int> info, vector<vector<int>> edges) {
    Tree node[17];
    int answer = 0;
    for (int i = 0; i < info.size(); ++i)
        node[i].wolf = info[i] == 1;
    for (vector<int>& edge : edges) {
        Tree& cur = node[edge[0]];
        if (cur.left == nullptr)
            cur.left = &node[edge[1]];
        else
            cur.right = &node[edge[1]];
    }
    deque<Tree> q;
    int wolf = 0, sheep = 0;
    q.push_back(node[0]);
    traversal(q, answer, wolf, sheep);
    return answer;
}