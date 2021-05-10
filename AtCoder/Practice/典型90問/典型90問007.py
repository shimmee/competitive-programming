# 典型90問007 - CP Classes
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_g
# Date: 2021/05/09

# ---------- Ideas ----------
# 各生徒について二分探索で近いところを探して，前後の2つのクラスのうち不満が小さいクラスに入れてあげる
# bisect使ってみよう

# ------------------- Answer --------------------
#code:python
import bisect
n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())

for _ in range(q):
    B = int(input())
    idx = bisect.bisect(A, B)
    if idx == 0:
        print(abs(A[idx]-B))
    elif idx == n:
        print(abs(A[idx-1] - B))
    else:
        print(min(abs(A[idx]-B), abs(A[idx-1]-B)))


# ------------------ Sample Input -------------------
4
4000 4400 5000 3200
3
3312
2992
4229


# ----------------- Length of time ------------------
# 9分

# -------------- Editorial / my impression -------------
# bisectの挙動が未だにわからんけどとりあえず出来た
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/007.jpg

# ----------------- Category ------------------
#AtCoder
#bisect
#二分探索
#ソートして二分探索
#ソート
#典型90問