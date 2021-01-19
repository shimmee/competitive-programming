# ARC111 A - Simple Math 2
# URL: https://atcoder.jp/contests/arc111/tasks/arc111_a
# Date: 2021/01/09

# ---------- Ideas ----------
# 赤坂にアドバイスもらってぎりぎり通した

# ------------------- Solution --------------------
# 10**nをm**2で割ったあまりをrとする
# rをmで割ったときの商が答え

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
r = pow(10, n, m**2)
print(r // m)


# ------------------ Sample Input -------------------
1 2

1000000000000000000 9997

# ----------------- Length of time ------------------
# 1時間

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc111/editorial/491

# ----------------- Category ------------------
#AtCoder
#ARC111
#ガウス記号
#高速なべき乗計算
