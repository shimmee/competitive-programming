# MUJIN プログラミングチャレンジ Programming Challenge: B - ロボットアーム
# URL: https://atcoder.jp/contests/mujin-pc-2016/tasks/mujin_pc_2016_b
# Date: 2021/02/25

# ---------- Ideas ----------
# 最大に行ける領域 = pi*(la+lb+lc)**2
# 「一番長い > 他の長さ2本の合計」のとき行けない部分ができる: 三角不等式
# 行けない部分の円の半径: 最大長さ - (他の2本の合計)

# ------------------- Answer --------------------
#code:python
import math
l = list(map(int, input().split()))
l.sort()

max_circle = math.pi*sum(l)**2
if l[0] + l[1] < l[2]:
    cant_go = math.pi*(l[2]-l[1]-l[0])**2
    print(max_circle - cant_go)
else:print(max_circle)


# ------------------ Sample Input -------------------
16 2 27

# ----------------- Length of time ------------------
# 5分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/mujin2016
# ARC004Bと同じ感じ！
# ロボットアームは三角不等式！！！

# ----------------- Category ------------------
#AtCoder
#三角不等式
#ロボット
#ロボットアーム