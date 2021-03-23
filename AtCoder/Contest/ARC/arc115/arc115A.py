#
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
odd = 0
even = 0
for _ in range(n):
    s = sum([int(i) for i in input()])
    if s % 2 == 1: odd += 1
    else: even += 1
print(even*odd)




# ------------------ Sample Input -------------------
3 2
00
01
10

7 5
10101
00001
00110
11110
00100
11111
10000

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
