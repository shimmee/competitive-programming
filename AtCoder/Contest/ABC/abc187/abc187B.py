# ABC187B - Gentle Pairs
# URL: https://atcoder.jp/contests/abc187/tasks/abc187_b
# Date: 2021/01/02

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
xy = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        x1,x2,y1,y2 = xy[i][0], xy[j][0], xy[i][1],xy[j][1]
        if x2-x1 == 0: continue
        if -1 <= (y2-y1)/(x2-x1) <= 1:
            ans += 1
print(ans)


# ------------------ Sample Input -------------------
3
0 0
1 2
2 1

1
-691 273

10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ABC187
#ABC-B
#AC_with_editorial #解説AC
