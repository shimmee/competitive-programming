# AGC014B - Unplanned Queries
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc014/tasks/agc014_b
# Date: 2021/01/31

# ---------- Ideas ----------
# 頂点1から頂点nまでが横並びになっていると考えて一般性を失わない
# imos法でカウントして，みんな偶数ならOK

# ------------------- Solution --------------------
# 区間[l, r]にaを追加したいとき，配列imosを用意して
# ステップ1: imos[l] += a
# ステップ2: imos[r+1] -= a
# ステップ3: imosの累積和を取る (ここまでimos法)
# ステップ4: 累積和のmaxを取る

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
imos = [0]*(n+2)
for _ in range(m):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1
from itertools import accumulate
cum = [0] + list(accumulate(imos))
if all(i % 2 == 0 for i in cum):
    print('YES')
else:
    print('NO')


# ------------------ Sample Input -------------------
4 4
1 2
2 4
1 3
3 4

5 5
1 2
3 5
5 1
3 4
2 3


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc014/editorial.pdf
# 各頂点の出現回数が全て偶数の場合のみYESになるらしい。いもす法はいらなかった。

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#木
#グラフ
#偶奇に注目
#クエリ処理
