# ABC204
# URL:
# Date: 2021/06/06

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] > 10:
        ans += a[i]-10
print(ans)

# ------------------ Sample Input -------------------
3
6 17 28


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
