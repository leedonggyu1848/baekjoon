function countDivisor(n) {
    var answer = 0;
    if (n == 1) return 1;
    for (var i=1; i*i<n; ++i)
        if (n % i == 0) answer+=2;
    answer += i*i == n
    return answer;
}

function solution(left, right) {
    var answer = 0;
    for (var i=left; i<=right; ++i)
        if (countDivisor(i) % 2)  answer -= i;
        else answer += i;
    return answer;
}