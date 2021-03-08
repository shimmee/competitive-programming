# ABC194A - I Scream
# URL: https://atcoder.jp/contests/abc194/tasks/abc194_a
# Date: 2021/03/06

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# c: 乳固形分
# b: 乳脂肪

# ------------------- Answer --------------------
#code:python
a, b = map(int, input().split())

c = a+b
if c >= 15 and b >= 8: print(1)
elif c >= 10 and b >= 3: print(2)
elif c >= 3: print(3)
else: print(4)


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
