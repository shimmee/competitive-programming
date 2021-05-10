# ARC118
# URL:
# Date: 2021/05/09

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

n = int(input())
l = []
for i in range(1, 20000):
    l.append(i * 6)
    l.append(i * 10)
    l.append(i * 15)

l2 = []
for i in l:
    if i <= 10000:
        l2.append(i)
ans = list(set(l2))[:n]
print(*ans)

# ------------------ Sample Input -------------------
3

4

10

20

2500
# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
