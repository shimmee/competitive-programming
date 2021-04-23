# 典型90問022 -
# URL: https://github.com/E869120/kyopro_educational_90/blob/main/sample/022.txt
# Date: 2021/04/22

# ---------- Ideas ----------
# 3辺のgcdの大きさが正方形の1辺になる


# ------------------- Answer --------------------
#code:python

from math import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

S = list(map(int, input().split()))
d = gcd_list(S)
print(sum([s//d - 1 for s in S]))



# ------------------ Sample Input -------------------
2 2 3
2 2 4
1000000000000000000 999999999999999999 999999999999999998

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
