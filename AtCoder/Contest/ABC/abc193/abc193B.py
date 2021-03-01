#
# URL:
# Date: 2021/02/27

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
ans = 10**20

for _ in range(n):
    now = 0
    A, P, X = map(int, input().split())
    zaiko = X - A
    if zaiko > 0:
        ans = min(ans, P)

print(ans if ans != 10**20 else -1)



# ------------------ Sample Input -------------------
3
3 9 5
4 8 5
5 7 5


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
