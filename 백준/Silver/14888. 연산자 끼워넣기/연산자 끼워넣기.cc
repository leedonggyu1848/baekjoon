#include<iostream>
#include<algorithm>
#include<iterator>
#include<string>
#include<cstring>
#include<array>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<cstdio>
#include<iomanip>
#include<fstream>
using namespace std;

int n;
int num[11];
int opt[4];
int maxv = -100000001;
int minv = 100000001;

void solve(int rst, int pos)
{
	if (pos == (n-1))
	{
		maxv = max(maxv, rst);
		minv = min(minv, rst);
		return;
	}
	for (int i = 0; i < 4; i++)
	{
		if (opt[i] != 0) {
			opt[i]--;
			switch (i)
			{
			case 0:
				solve(rst + num[pos+1], pos + 1);
				break;
			case 1:
				solve(rst - num[pos+1], pos + 1);
				break;
			case 2:
				solve(rst * num[pos+1], pos + 1);
				break;
			case 3:
				solve(rst / num[pos+1], pos + 1);
				break;
			default:
				break;
			}
			opt[i]++;
		}
	}
}

int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &num[i]);
	}
	for (int i = 0; i < 4; i++)
	{
		scanf("%d", &opt[i]);
	}
	solve(num[0], 0);
	printf("%d\n%d", maxv, minv);
	return 0;
}