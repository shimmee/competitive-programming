# 典型90問070 - Plant Planning（★4）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_br
# Date: 2021/06/17

# ---------- Ideas ----------
# まさにmean absolute errorなので，中央値で最小値になる
# 奇数と偶数の場合わけする


# ------------------- Answer --------------------
#code:python
n = int(input())
XY = [[int(i) for i in input().split()] for _ in range(n)]
X = sorted([XY[i][0] for i in range(n)])
Y = sorted([XY[i][1] for i in range(n)])
if n % 2 == 1:
    x = X[n//2]
    y = Y[n//2]
else:
    x = (X[n // 2 - 1] + X[n // 2]) / 2
    y = (Y[n // 2 - 1] + Y[n // 2]) / 2

dist_x = sum([abs(X[i] - x) for i in range(n)])
dist_y = sum([abs(Y[i] - y) for i in range(n)])
print(int(dist_x + dist_y))

# ------------------ Sample Input -------------------
2
-1 2
1 1

2
1 0
0 1

5
2 5
2 5
-3 4
-4 -8
6 -2

4
1000000000 1000000000
-1000000000 1000000000
-1000000000 -1000000000
1000000000 -1000000000

4
1 1
2 2
3 3
4 4

# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# x,y独立に考えるのが典型考察でした

# ----------------- Category ------------------
#AtCoder
#x,y独立に考える
#中央値
#MAE
#典型90問