# ARC054A - 動く歩道
# URL: https://atcoder.jp/contests/arc054/tasks/arc054_a
# Date: 2021/02/18

# ---------- Ideas ----------
# 時計回りのときの時間 = 時計回りのときの距離 // 時計回りのときのスピード
# 反時計回りのときの時間 = 反時計回りのときの距離 // 反時計回りのときのスピード


# ------------------- Answer --------------------
#code:python
L, X, Y, S, D = map(int, input().split())

clock_dist = D - S if S <= D else D + L - S
clock_speed = X + Y
clock_time = clock_dist/clock_speed

anti_dist = S + L - D if S <= D else S - D
anti_speed = Y - X
anti_time = anti_dist/anti_speed if anti_speed > 0 else 10**20

print(min(clock_time, anti_time))

# ------------------ Sample Input -------------------
6 3 1 5 3

6 2 3 1 5


# ----------------- Length of time ------------------
# 17分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/arc/054/editorial.pdf
# 時計の問題は頭がこんがらがるぜ
# 解答は長くなったけど，とてもきれいに書けたと思う

# ----------------- Category ------------------
#AtCoder
#時計問題
#場合分け
#速さ・時間・道のり