#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

enum{
    START, DURATION
};

struct cmp{
    bool operator()(vector<int> &a, vector<int> &b){
        return a[DURATION] > b[DURATION];
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int i = 0;
    int time = 0;
    sort(jobs.begin(), jobs.end());
    priority_queue<vector<int>, vector<vector<int>>, cmp> q;
    while(i < jobs.size() || !q.empty()){
        if(i < jobs.size() &&time >= jobs[i][START])
            q.push(jobs[i++]);
        else if(!q.empty()){
            answer += q.top()[DURATION] + time - q.top()[START];
            time += q.top()[DURATION];
            q.pop();
        }
        else
            time = jobs[i][START];
    }
    return answer / jobs.size();
}