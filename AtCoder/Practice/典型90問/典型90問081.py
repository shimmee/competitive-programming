# 典型90問081 - Friendly Group（★5）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_cc
# Date: 2021/06/30

# ---------- Ideas ----------
# ヒストグラムつくって二次元累積和する
# numpyで二次元累積和が簡単に出来るらしい


# ------------------- Answer --------------------
#code:python
import numpy as np
n, k = map(int, input().split())
m = 5001
G = np.zeros((m, m), int)
for _ in range(n):
    a, b = map(int, input().split())
    G[a][b] += 1

cum = G.cumsum(axis=0).cumsum(axis=1)

ans = 0
for i in range(1, m-k):
    for j in range(1, m-k):
        ans = max(ans, cum[i+k][j+k] - cum[i-1][j+k] - cum[i+k][j-1] + cum[i-1][j-1])
print(ans)

# TLEでした

# ------------------ Sample Input -------------------
3 4
1 1
2 5
7 4

2 123
4 5
678 901

7 10
20 20
20 20
20 30
20 40
30 20
30 30
40 20

3 1
1 1
1 2
1 3
# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
# 思いつくまでに5分くらい
# numpyで実装するまでに10分くらい
# TLEでした

# ----------------- Category ------------------
#AtCoder
#二次元累積和
#numpyはTLE
#典型90問