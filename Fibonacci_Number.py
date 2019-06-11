class Solution:
    def fib(self, N: int) -> int:
        res = [0, 1] + [0 for i in range(N-1)]
        for i in range(2, N+1):
            res[i] = res[i-1] + res[i-2]
        return res[N]