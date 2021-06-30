# 典型90問067 - Base 8 to 9（★2）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bo
# Date: 2021/06/14

# ---------- Ideas ----------
# 8進数 -> 10進数
# 10進数 -> 9進数
# 8を5に変換して8進数とみなす
# これをk回繰り返す

# ------------------- Answer --------------------
#code:python
import sys
sys.setrecursionlimit(1000000)

def Base_n_to_10(X: str, n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out #int out

def Base_10_to_n(X: int, n):
    if X//n:
        return Base_10_to_n(X//n, n)+str(X%n)
    return str(X%n)
base8, k = map(int, input().split())

for _ in range(k):
    base10 = Base_n_to_10(str(base8), 8)
    base9 = Base_10_to_n(base10, 9)
    base8 = base9.replace('8', '5')
print(base8)

# ------------------ Sample Input -------------------
21 1

1330 1

2311640221315 15

0 10

1152921504606846976 5
# ----------------- Length of time ------------------
# 10分?

# -------------- Editorial / my impression -------------
# やるだけだった

# ----------------- Category ------------------
#AtCoder
#base変換
#進数変換
#典型90問