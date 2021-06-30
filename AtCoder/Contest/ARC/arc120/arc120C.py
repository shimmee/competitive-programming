# ARC120A
# URL:
# Date: 2021/05/23

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

n = int(input())
a = list(map(int, input().split()))
from itertools import accumulate
cum_sum = list(accumulate(a))
cum_max = [0]
for i in range(n):
    ai = cum_sum[i]
    cum_max.append(max(ai, cum_max[-1]))

cum_sum = [0]
cum_max = [0]
for i in range(n):
    ai = a[i]
    cum_max.append(max(ai, cum_max[-1]))
    cum_sum.append(ai)



# ------------------ Sample Input -------------------
3
1 2 3


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい

