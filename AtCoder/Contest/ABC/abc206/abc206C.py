# ABC206
# URL:
# Date: 2021/06/19

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
a = list(map(int, input().split()))
counter = Counter(a)

cnt = 0
for key, value in counter.items():
    cnt += value*(value-1)//2

print(n*(n-1)//2-cnt)


# ------------------ Sample Input -------------------
3
1 7 1

20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
