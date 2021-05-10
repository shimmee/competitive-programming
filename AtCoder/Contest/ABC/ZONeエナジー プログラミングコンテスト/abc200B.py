# ZONeエナジー プログラミングコンテスト B
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n, D, H = map(int, input().split())
dh = [[int(i) for i in input().split()] for _ in range(n)]

ans = 10**10
for i in range(n):
    di, hi = dh[i]
    tan = (H-hi)/(D-di)
    height = di * tan

    flag = True
    for j in range(n):
        dj, hj = dh[j]
        if di <= dj:
            x = di * tan
            if hi >= hj: continue

            y = abs(dj-di)*tan
            hl = hi + y
            if hj >= hl: flag = False
        else:
            x = H - D * tan
            y = H - (D - dj) * tan
            if hj > y:
                flag = False

    if flag:
        ans = min(ans, hi-height)
print(max(ans, 0))

# ------------------ Sample Input -------------------
5 896 483
228 59
529 310
339 60
78 266
659 391

1 10 10
3 5



1 10 10
3 2

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
