# ARC018B - 格子点と整数
# URL: https://atcoder.jp/contests/arc018/tasks/arc018_2
# Date: 2021/04/14

# ---------- Ideas ----------
# 座標3点から三角形の面積を求める公式はこれ: https://mathwords.net/x1y2hikux2y1
# 割る2の操作があるので，整数かどうか確かめるためには，割る2をせずに，割って2で割り切れるかどうかで判断したい

# ------------------- Answer --------------------
#code:python
n = int(input())
XY = [[int(i) for i in input().split()] for _ in range(n)]
X = [XY[i][0] for i in range(n)]
Y = [XY[i][1] for i in range(n)]

def get_area_double(x1, y1, x2, y2, x3, y3):
    # 本当は1/2しなきゃいけないけど少数バグるから2倍の大きさを出力
    area = abs((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3))
    return area

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            area = get_area_double(X[i], Y[i], X[j], Y[j], X[k], Y[k])
            if area % 2 == 0 and area > 0:
                ans += 1
print(ans)

# ------------------ Sample Input -------------------
8
3 1
4 1
5 9
2 6
5 3
5 8
9 7
9 3


# ----------------- Length of time ------------------
# https://www.slideshare.net/chokudai/arc018
# 割る2して提出してWA出しちゃった:

# -------------- Editorial / my impression -------------
# 9分

# ----------------- Category ------------------
#AtCoder
#三角形の面積
#全探索
#浮動点少数