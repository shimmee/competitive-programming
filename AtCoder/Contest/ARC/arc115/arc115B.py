#
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
C = [[int(i) for i in input().split()] for _ in range(n)]

row_sum = [sum(C[i]) for i in range(n)]
col_sum = [sum([C[i][j] for i in range(n)]) for j in range(n)]
row_remainder = [row_sum[i]%n for i in range(n)]
col_remainder = [col_sum[i]%n for i in range(n)]

r = row_sum[0] % n
all(row_sum[i]%n == r and col_sum[i]%n == r for i in range(n))

if not all(row_sum[i]%n == r and col_sum[i]%n == r for i in range(n)): # すべて同じ余りでない
    print('No')
    exit()

A = [row_sum[i] // n for i in range(n)]
A = [a - min(A) for a in A]
A_sum = sum(A)
B = [(col_sum[i]-A_sum) // n for i in range(n)]

flag = True
for i in range(n):
    for j in range(n):
        if C[i][j] != A[i] + B[j]:
            flag = False

if flag:
    print('Yes')
    print(*A)
    print(*B)
else:
    print('No')



# ------------------ Sample Input -------------------
3
4 3 5
2 1 3
3 2 4

3
4 3 5
2 2 3
3 2 4

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
