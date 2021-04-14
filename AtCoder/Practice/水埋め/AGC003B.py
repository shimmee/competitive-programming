# AGC003B - Simplified mahjong
# URL: https://atcoder.jp/contests/agc003/tasks/agc003_b
# Date: 2021/04/14

# ---------- Ideas ----------
# 1から順に貪欲に

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
A = [int(input()) for _ in range(n)]
B = [0]*n
ans = 0
for i in range(n-1):

    # i枚目でできるペア
    q, r = divmod(A[i], 2)
    ans += q
    A[i] -= q*2

    # i枚目の余りとi+1枚目でできるペア
    if A[i+1] >= 1 and r >= 1:
        ans += 1
        A[i] -= 1
        A[i+1] -= 1

ans += A[-1] // 2
print(ans)


ans = 0
for i in range(n):
    ans += A[i] // 2
    B[i] = A[i] % 2

for i in range(n-1):
    if B[i] >= 1 and B[i+1] >= 1:
        ans += 1
        B[i] -= 1
        B[i+1] -= 1
print(ans)

# ------------------ Sample Input -------------------
4
4
0
3
2


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
