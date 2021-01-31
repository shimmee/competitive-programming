# ABC190B -
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_b
# Date: 2021/01/30

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, s, d = map(int, input().split())
flag = False
for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        flag = True
if flag: print('Yes')
else: print('No')

# ------------------ Sample Input -------------------
4 9 9
5 5
15 5
5 15
15 15


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ABC-B