# 典型90問010 - Score Sum Queries
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_j
# Date: 2021/05/09

# ---------- Ideas ----------
# 点数の配列を始めは0で埋めておく
# 累積和とってクエリ処理

# ------------------- Answer --------------------
#code:python
n = int(input())
p1 = [0]*n
p2 = [0]*n
from itertools import accumulate
for i in range(n):
    c, p = map(int, input().split())
    if c == 1: p1[i] = p
    else: p2[i] = p

cum1 = [0] + list(accumulate(p1))
cum2 = [0] + list(accumulate(p2))
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    ans1 = cum1[r + 1] - cum1[l]
    ans2 = cum2[r + 1] - cum2[l]
    print(ans1, ans2)


# ------------------ Sample Input -------------------
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# 一番シンプルな累積和
# 解説: https://github.com/E869120/kyopro_educational_90/blob/main/editorial/010.jpg
#

# ----------------- Category ------------------
#AtCoder
#累積和
#典型90問