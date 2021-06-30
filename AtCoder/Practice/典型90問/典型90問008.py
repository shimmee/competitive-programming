# 典型90問008 - AtCounter
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_h
# Date: 2021/05/10

# ---------- Ideas ----------
# DP
# dp[i][j]: atcoderのi文字目までが，Sのj文字目までで構成できる場合の数

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n = int(input())
S = input()
T = 'atcoder'
m = len(T)

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
dp[0] = [1]*(n+1)

for i in range(1, m+1):
    for j in range(1, n+1):
        # S[j]とT[i]が一致している時
        if S[j-1] == T[i-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        else: # 一致してない時
            dp[i][j] = dp[i][j-1]

print(dp[m][n] % mod)

# ------------------ Sample Input -------------------
10
attcordeer

# ----------------- Length of time ------------------
# 14分AC

# -------------- Editorial / my impression -------------
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg
# 2つの文字列を一致させる場合の数とか一致するための最小操作回数みたいなのはだいたいDP

# ----------------- Category ------------------
#AtCoder
#耳DP
#動的計画法
#文字列問題
#文字の一致
#場合の数
#典型90問
