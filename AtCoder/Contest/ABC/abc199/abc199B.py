# ABC199B -
# URL:
# Date: 2021/04/24

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = [0 for i in range(1001)]
for i in range(n):
    a = A[i]
    b = B[i]
    if a <= b:
        for j in range(a, b+1):
            l[j] += 1

cnt = 0
for i in range(1001):
    if l[i] == n:
        cnt += 1
print(cnt)


# ------------------ Sample Input -------------------
2
3 2
7 5


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
