# パ研合宿2020 F - Fibonaccyan
# URL: https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_f
# Date: 2021/01/05

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# メモ化再帰でn=3000までのフィボナッチ数を全部作る
# ループでpの倍数のものが出てきたら出力

# ------------------- Answer --------------------
#code:python
import sys
sys.setrecursionlimit(1000000)

p = int(input())
n = 3000
dp = [-1]*(n+1)
def fib(n):
    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
fib(n)

for i in range(len(dp)):
    if dp[i] % p == 0:
        print(i+1); exit()
print(-1)

# ------------------ Sample Input -------------------
3

10

3000
# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#パ研合宿2020
#メモ化再帰
#DP
#動的最適化