#
# URL:
# Date: 2021/06/13

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
a.sort()
flag = True
for i in range(n):
    if i+1 != a[i]: flag = False
print('Yes' if flag else 'No')

# ------------------ Sample Input -------------------


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
