# ABC185E - Sequence Matching
# URL: https://atcoder.jp/contests/abc185/tasks/abc185_e
# Date: 2021/05/06

# ---------- Ideas ----------
# 編集距離，レーベンシュタイン距離
# 自力でテーブルの書いてみて，推移式をエスパーする

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        else:
            if A[j-1] == B[i-1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]) + 1
print(dp[m][n])

# ------------------ Sample Input -------------------
4 3
1 2 1 3
1 3 1

4 6
1 3 2 4
1 5 2 6 4 3

5 5
1 1 1 1 1
2 2 2 2 2

# ----------------- Length of time ------------------
# 28分

# -------------- Editorial / my impression -------------
# LCSに似てたけど編集距離だった
# 推移も難しくないし，比較的簡単なDPだった
# https://atcoder.jp/contests/abc185/editorial

# ----------------- Category ------------------
#AtCoder
#AtCoder500点
#ABC-E
#DP
#動的計画法
#LCS
#編集距離
#レーベンシュタイン距離
#最長共通部分列問題
#二次元ナップサックDP
#数列
#色に関する問題
#部分列
#水色diff