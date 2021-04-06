# ABC197D - Opposite
# URL: https://atcoder.jp/contests/abc197/tasks/abc197_d
# Date: 2021/03/27

# ---------- Ideas ----------
# 多角形の中心を軸にx0, y0をθ度回転する
# https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python


# ------------------- Answer --------------------
#code:python
import math
n = int(input())
x0, y0 = map(int, input().split())
x2n, y2n = map(int, input().split())

X = (x0+x2n)/2
Y = (y0+y2n)/2

theta = math.radians(180*(n-2)/n)

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


x, y = rotate((X, Y), (x0, y0), math.pi-theta)
print(x, y)


# ------------------ Sample Input -------------------
4
1 1
2 2

6
5 3
7 4


# ----------------- Length of time ------------------
# 50分でAC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc197/editorial
# 簡単だったけど時間かかってしまった
# 他の人も考察で時間がかかったらしい

# ----------------- Category ------------------
#AtCoder
#緑diff
#座標の回転
#多角形
#線形代数
#数問