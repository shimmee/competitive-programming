# ABC190D - Staircase Sequences
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_d
# Date: 2021/01/30

# ---------- Ideas ----------
# 解説AC
# 本番で解けなかった

# ------------------- Solution --------------------
# O(√N)で約数を列挙し，2*n=x*yとなるx，yのうち，偶奇or奇遇となるものの個数が答え

# ------------------- Answer --------------------
#code:python
n = int(input())
ans = 0
for x in range(1, int((2*n)**0.5)+1):
    y = 2*n/x
    if y == int(y):
        if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
            ans += 1
print(ans*2)


# ------------------ Sample Input -------------------
12

1

963761198400


# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc190/editorial
# 整数問題で10**12があったら√nで約数列挙が鉄板らしい

# ----------------- Category ------------------
#AtCoder
#ABC-D
#約数列挙
#等差数列の和
#10^12
#O(√N)
#復習したい
#偶奇に注目
#解説AC