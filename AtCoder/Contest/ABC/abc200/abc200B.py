# ABC200
# URL:
# Date: 2021/05/08

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())

for _ in range(k):
    if n % 200 == 0:
        n //= 200
    else:
        n = int(str(n) + '200')
print(n)

# ------------------ Sample Input -------------------
2021 4

40000 2

8691 20

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
