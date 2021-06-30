# ABC202
# URL:
# Date: 2021/05/22

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

bc = []
for i in range(n):
    bc.append(b[c[i]-1])
from collections import deque, Counter
count = Counter(bc)
ans = 0
for i in range(n):
    ans += count[a[i]]
print(ans)


import sys
sys.setrecursionlimit(1000000)
# ------------------ Sample Input -------------------
3
1 2 2
3 1 2
2 3 2

4
1 1 1 1
1 1 1 1
1 2 3 4


3
2 3 3
1 3 3
1 1 1

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
