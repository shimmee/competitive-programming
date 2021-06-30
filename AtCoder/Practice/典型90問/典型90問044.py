# 典型90問044
# URL:
# Date: 2021/05/18

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n, Q = map(int, input().split())
A = deque(list(map(int, input().split())))

for _ in range(Q):
    t, x, y = list(map(int, input().split()))
    x, y = x-1, y-1
    if t == 1:
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        x = A.pop()
        A.appendleft(x)
    elif t == 3:
        print(A[x])

from collections import deque
n, Q = map(int, input().split())
A = deque(list(map(int, input().split())))

for _ in range(Q):
    t, x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    if t == 1:
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        A.rotate(1)
    elif t == 3:
        print(A[x])

# ------------------ Sample Input -------------------
8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0

9 6
16 7 10 2 9 18 15 20 5
2 0 0
1 1 4
2 0 0
1 8 5
2 0 0
3 6 0


11 18
23 92 85 34 21 63 12 9 81 44 96
3 10 0
3 5 0
1 3 4
2 0 0
1 4 11
3 11 0
1 3 5
2 0 0
2 0 0
3 9 0
2 0 0
3 6 0
3 10 0
1 6 11
2 0 0
3 10 0
3 4 0
3 5 0
# ----------------- Length of time ------------------
# 5分

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#deque
#キュー