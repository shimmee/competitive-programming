# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192):
# URL: https://atcoder.jp/contests/abc192/tasks/abc192_c
# Date: 2021/02/20

# ---------- Ideas ----------
# k回シミュレーションするだけ

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
a = n
for _ in range(k):
    a_max = int(''.join(sorted(str(a), reverse=True)))
    a_min = int(''.join(sorted(str(a))))
    a = a_max - a_min
print(a)


# ------------------ Sample Input -------------------
314 2
302 2


# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# 何も難しくない

# ----------------- Category ------------------
#AtCoder
#ABC-C