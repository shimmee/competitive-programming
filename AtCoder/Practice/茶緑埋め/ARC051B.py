# ARC051B - 互除法
# URL: https://atcoder.jp/contests/arc051/tasks/arc051_b
# Date: 2021/03/02

# ---------- Ideas ----------
# 実験してわかったが，フィボナッチの隣り合う2項を入れれば良さそう

# ------------------- Answer --------------------
#code:python
fib = [0, 1]
for i in range(42):
    fib.append(fib[i] + fib[i + 1])

k = int(input())
print(fib[k + 2], fib[k + 1])

# ここは実験
# def gcd(a, b):
#     if b == 0: return a
#     r = a % b
#     print('here')
#
#     return gcd(b, r)
#
# gcd(314159265, 358979323)
# gcd(13, 8)
#
# 2, 1
# 1 0
# 2 1
# 3 2
# 5 3
# 8 5

# ------------------ Sample Input -------------------
1

3

12


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/arc/051/editorial.pdf
# 乱数を使うというのも部分点を取る方法らしい。変なの。
# 再帰の復習になってよかった。

# ----------------- Category ------------------
#AtCoder
#gcd
#ユークリッドの互除法
#フィボナッチ数列
#