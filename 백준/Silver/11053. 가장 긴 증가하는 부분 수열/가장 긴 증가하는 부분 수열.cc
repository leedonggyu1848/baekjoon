#include<iostream>
using namespace std;

int main()
{
	int n = 0;
	int temp = 1;
	int arr[1000];
	int dp[1000]{ 0 };
	fill_n(dp, 1000, 1);
	int max = 1;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	for (int i = 0; i < n; i++)
	{
		max = 0;
		for (int j = 0; j < i+1; j++)
		{
			if (arr[j] < arr[i])
				if (max < dp[j])
					max = dp[j];
		}
		dp[i] = max+1;
	}
	max = 0;
	for (int i = 0; i < n; i++)
	{
		if (dp[i] > max)
			max = dp[i];
	}
	cout << max;
	return 0;
}