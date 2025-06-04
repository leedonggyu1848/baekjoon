def solve(first_seq: str, second_seq: str) -> int:
	len_first = len(first_seq)
	len_second = len(second_seq)

	# row: first_seq, col: second_seq
	dp = [[0] * (len_second + 1) for _ in range(len_first + 1)]

	# initialize dp 첫 줄은 무조건 insertion 혹은 deletion만 가능하므로 1씩 증가
	for y in range(1, len_first + 1):
		dp[y][0] = y
	for x in range(1, len_second + 1):
		dp[0][x] = x

	# fill dp
	for y in range(1, len_first + 1):
		for x in range(1, len_second + 1):
			if first_seq[y - 1] == second_seq[x - 1]:
				dp[y][x] = dp[y - 1][x - 1]
			else:
				dp[y][x] = 1 + min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1])

	return dp[len_first][len_second]

a = input()
b = input()
print(solve(a, b))