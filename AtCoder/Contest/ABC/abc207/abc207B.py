# ABC207
# URL:
# Date: 2021/06/26

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

a, b, c, d = map(int, input().split())
for i in range(10**6):
    if a + b*i <= c*i*d:
        print(i)
        exit()
        break
print(-1)

# ------------------ Sample Input -------------------
5 2 3 2

6 9 2 3


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
