# ABC201 -
# URL:
# Date: 2021/05/15

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from itertools import permutations
s = list(map(int, input().split()))
pattern = list(permutations(s))

for p in pattern:
    if p[2]-p[1] == p[1]-p[0]:
        print('Yes')
        exit()
print('No')

# ------------------ Sample Input -------------------
5 1 3


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
