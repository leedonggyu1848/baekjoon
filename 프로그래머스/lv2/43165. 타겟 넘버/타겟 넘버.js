function solution(numbers, target) {
    return (function dfs(idx, acc) {
        if (idx == numbers.length) return acc == target;
        return dfs(idx+1, acc+numbers[idx]) + dfs(idx+1, acc-numbers[idx]);
    })(0, 0)
}