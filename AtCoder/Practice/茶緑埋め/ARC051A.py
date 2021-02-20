# ARC051A - 塗り絵
# URL: https://atcoder.jp/contests/arc051/tasks/arc051_a
# Date: 2021/02/18

# ---------- Ideas ----------
# 四角 ⊃ 円: 赤は存在しない
# -> 円の中心が四角の中にあって，円の東西南北の点が四角より内側なら

# 四角 ⊂ 円: 青は存在しない
# 四角形の四隅がすべてcircleの中にあれば，青は存在しない。1つでも外ならOK


# ------------------- Answer --------------------
#code:python
x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

def corner_in_circle(x, y):
    return (x-x1)**2+(y-y1)**2 <= r**2

flag1 = True if x2 <= x1-r else False
flag2 = True if x3 >= x1+r else False
flag3 = True if y2 <= y1-r else False
flag4 = True if y3 >= y1+r else False

flag5 = corner_in_circle(x2, y2)
flag6 = corner_in_circle(x2, y3)
flag7 = corner_in_circle(x3, y2)
flag8 = corner_in_circle(x3, y3)

# 赤の判定
if flag1 and flag2 and flag3 and flag4:
    print('NO')
else:
    print('YES')

# 青の判定
if flag5 and flag6 and flag7 and flag8:
    print('NO')
else:
    print('YES')


# ------------------ Sample Input -------------------
0 1 1
-2 0 4 3


0 0 5
-4 -4 4 4


-1 -1 2
2 3 4 5

0 0 5
-2 -2 2 1

# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/arc/051/editorial.pdf
# 無駄な条件をつけてたけどAC
# 図形が内包するかどうかみたいな問題は座系の座標の端っこの大小関係でうまく書ける

# ----------------- Category ------------------
#AtCoder
#図形の内包条件
#四角形と円
#図形
