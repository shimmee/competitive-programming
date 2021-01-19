# パ研合宿2020 J - Output-only
# URL: https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_j
# Date: 2021/01/05

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# 奇数mと偶数nで以下のように定めたa,b,cで三平方の定理を満たす
# a=|m**2−n**2| 、b=2*m*n、c=m**2+n**2
# a<=b<=cと，gcdの条件に注意

# ------------------- Answer --------------------
# code:python
def gcd_list(numbers):
    return reduce(gcd, numbers)
from math import gcd
from functools import reduce

l = []
flag = False
c_list = set()
for m in range(1, 1200, 2):
    for n in range(2, 1200, 2):
        a = abs(m ** 2 - n ** 2)
        b = 2 * m * n
        c = m ** 2 + n ** 2

        if a <= b <= c and gcd_list([a,b,c]) == 1 and not c in c_list:
            l.append([a,b,c])
            c_list.add(c)
        if len(l) == 10**5:
            flag = True
            break
    if flag: break


for abc in l:
    print(f'{abc[0]} {abc[1]} {abc[2]}')


# ------------------ Sample Input -------------------


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#パ研合宿2020
#三平方の定理