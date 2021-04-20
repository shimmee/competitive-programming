# ARC117B -
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n = int(input())
A = sorted(list(map(int, input().split())), reverse = True)
A += [0]
ans = 1
for i in range(n):
    ans = ans * (A[i]-A[i+1]+1) % mod
print(ans % mod)

# ------------------ Sample Input -------------------
2
1 2

6
5 3 4 1 5 2

7
314 159 265 358 979 323 846


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
