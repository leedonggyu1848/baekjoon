#include<iostream>
#include<algorithm>
#include<iterator>
#include<string>
#include<array>
using namespace std;

int main()
{
	array<int, 100>arr;
	int n, m;
	cin >> n >> m;
	int maxv = -1;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j < n; j++)
		{
			for (int k = j+1; k < n; k++)
			{
				if (arr[i] + arr[j] + arr[k] <= m)
					maxv = max(maxv, arr[i] + arr[j] + arr[k]);
			}
		}
	}
	cout << maxv;
	return 0;
}