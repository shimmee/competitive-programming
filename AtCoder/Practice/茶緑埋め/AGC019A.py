# AGC019A - Ice Tea Store
# URL: https://atcoder.jp/contests/agc019/tasks/agc019_a
# Date: 2021/02/02

# ---------- Ideas ----------
# 各リットルで必要な最低金額を求めておく


# ------------------- Answer --------------------
#code:python
q, h ,s, d = map(int, input().split())
n = int(input())

# 各リットルの候補
liter = [2, 1, 0.5, 0.25]
# 各リットルの最低金額
price = [min(q*8, h*4, s*2, d*1), min(q*4, h*2, s*1), min(q*2, h*1), q]

ans = 0
for i in range(4):
    amount = int(n // liter[i])
    ans += amount * price[i]
    n = n - amount*liter[i]
print(int(ans))

# ------------------ Sample Input -------------------
20 30 70 90
3

# ----------------- Length of time ------------------
# 12分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc019/editorial.pdf
# nが整数だから，小数点の買い方なんて考えなくてよかった
# 1グラムの買い方はmin(q*4, h*2, s*1)
# nの偶奇に注目すれば，nが偶数のときは2グラムだけでOK, 奇数のときは2グラムいくつかと1グラム1つ

# ----------------- Category ------------------
#AtCoder
#AGC-A
#場合分け
#茶diff