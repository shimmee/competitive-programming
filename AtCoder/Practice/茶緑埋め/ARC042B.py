# ARC042B - アリの高橋くん
# URL: https://atcoder.jp/contests/arc042/tasks/arc042_b
# Date: 2021/02/18

# ---------- Ideas ----------
# 全ての辺と高橋くんのいる点との距離のうち最短のものを出力すればいい
# 点と直線の距離: https://mathtrain.jp/tentotyokusen
# x1=x2のときには注意

# ------------------- Answer --------------------
#code:python
tx, ty = map(int, input().split())
n = int(input())
xy = [[int(i) for i in input().split()] for _ in range(n)]

ans = 10**10
for i in range(n):
    x1, y1 = xy[i-1]
    x2, y2 = xy[i]

    if x1 == x2:
        a = 1
        b = 0
        c = -x1
    else:
        a = (y2-y1)/(x2-x1)
        b = -1
        c = y1-a*x1

    d = abs(a*tx+b*ty+c)/(a**2+b**2)**0.5 # 公式
    ans = min(ans, d)
print(ans)
# ------------------ Sample Input -------------------
34 6
7
-43 -65
-23 -99
54 -68
65 92
16 83
-18 43
-39 2


# ----------------- Length of time ------------------
# 13分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc042
# 緑上だったが昔の問題なので簡単だった。ググりゲーだった。
# 反時計回りに順番に与えられていなかったら大変だった

# ----------------- Category ------------------
#AtCoder
#座標
#点と直線の距離
#最短距離