# 典型90問018 - Statue of Chokudai
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_r
# Date: 2021/05/11

# ---------- Ideas ----------
# 図示して頑張る

# ------------------- Answer --------------------
#code:python
from math import cos, sin, radians, degrees, atan
T = int(input())
L, X, Y = map(int, input().split())
q = int(input())
r = L/2

for _ in range(q):
    E = int(input())
    t = E % T
    theta1 = radians(360*t/T) # 原点から時計回りに何度進んだところに今いるか
    tan_theta2 = r*(1-cos(theta1)) / ((X**2+(Y+r*sin(theta1))**2)**0.5)
    theta2 = atan(tan_theta2)
    print(degrees(theta2))

# ------------------ Sample Input -------------------
4
2 1 1
4
0
1
2
3

5121
312000000 4123 3314
6
123
12
445
4114
42
1233

# ----------------- Length of time ------------------
# 90分

# -------------- Editorial / my impression -------------
# この問題辛すぎない？
# 俯角の角度を勘違いしてた: ，観覧車の現在地/直大/原点 の角度かと思ったら違った
# 観覧車の現在地/直大/観覧車からy軸に下ろした垂線とy軸の交点 の角度だった

# ----------------- Category ------------------
#AtCoder
#幾何
#三角比
#逆三角関数
#三角関数
#典型90問