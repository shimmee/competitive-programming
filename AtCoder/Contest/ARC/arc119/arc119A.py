# ARC119
# URL:
# Date: 2021/05/16

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from math import log2, ceil
n = int(input())
m = int(log2(n))

ans = 10**20
for b in range(m+1):
    a = n // 2**b
    c = n - a*2**b
    if a >= 0 and b >= 0 and c >= 0 and n == a*2**b + c:
        ans = min(ans, a + b + c)
print(ans)



# ------------------ Sample Input -------------------
998244353

1000000007

1

998984374864432412

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
