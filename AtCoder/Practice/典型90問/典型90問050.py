# 典型90問050 - Stair Jump（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ax
# Date: 2021/05/26

# ---------- Ideas ----------
# DP! かえるの問題と同じ
# 配るDPする

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n, L = map(int, input().split())

dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    if i+1 <= n: dp[i+1] += dp[i]
    if i+L <= n: dp[i+L] += dp[i]
print(dp[n] % mod)


# ------------------ Sample Input -------------------
5 2

6783 125

# ----------------- Length of time ------------------
# 1分

# -------------- Editorial / my impression -------------
# さすがにこれくらいのDPならすぐ書ける！
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/050.jpg

# ----------------- Category ------------------
#AtCoder
#DP
#簡単なDP
#動的計画法
#典型90問