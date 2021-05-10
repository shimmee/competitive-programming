# ARC118
# URL:
# Date: 2021/05/09

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
t, n = map(int, input().split())
# 桁数が大きい(16桁以上)の割り算でceilやintをする場合
# math.ceil(a/b) これだと誤差が生じる
def ceilling(a, b):
    return (a+b-1)//b # これを使うべき

print(ceilling(100*n, t)*(100+t)//100 - 1)

# ------------------ Sample Input -------------------
10 1

3 5

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
