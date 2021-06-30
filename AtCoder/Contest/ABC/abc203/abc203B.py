# ABC203
# URL:
# Date: 2021/05/30

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
N, K = map(int, input().split())
ans = 0
for n in range(1, N+1):
    for k in range(1, K+1):
        ans += int(str(n) + '0' + str(k))
print(ans)

# ------------------ Sample Input -------------------
1 2


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい

