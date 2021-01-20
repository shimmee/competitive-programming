# ABC048B - Between a and b ...
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc048/tasks/abc048_b
# Date: 2021/01/12


# ------------------- Solution --------------------
# bまでの商からa-1までの商を引く

# ------------------- Answer --------------------
#code:python
a, b, x = map(int, input().split())
print(b//x - (a-1)//x)

# ------------------ Sample Input -------------------
4 8 2

0 5 1

9 9 2

1 1000000000000000000 3


# ----------------- Length of time ------------------
# 2分でAC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc064/editorial.pdf
# コーナーケースも処理する必要もなくて簡単すぎた
# 2016年に緑diffだけど今なら灰色だと思う

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#緑diff
#ABC-B