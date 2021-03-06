# ABC189B - Alcoholic
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_b
# Date: 2021/01/23

# ---------- Ideas ----------
# 飲んだアルコール量をインクリメントしていって，xを超えたら出力すればいい

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, x = map(int, input().split())

alc = 0
for i in range(n):
    v, p = map(int, input().split())
    alc += v*p
    if alc > x*100:
        print(i+1)
        exit()

print(-1)

# 3回WAを出してしまった
# 浮動点小数でWAがでた
# x*100で対応した

# ------------------ Sample Input -------------------
2 15
200 5
350 3

2 10
200 5
350 3

3 1000000
1000 100
1000 100
1000 100

# ----------------- Length of time ------------------
# 15分

# -------------- Editorial / my impression -------------
# 教訓: 浮動点小数の足し算は絶対にしない

# ----------------- Category ------------------
#AtCoder
#ABC-B
#float
#浮動点小数