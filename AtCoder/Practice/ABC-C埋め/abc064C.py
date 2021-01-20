# ABC064C - Colorful Leaderboard
# URL: https://atcoder.jp/contests/abc064/tasks/abc064_c
# 日付: 2020/12/15

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 8色が現れたかどうかのflagと3200以上の人間のカウンターを用意
# ループでif文回して，8色にTrueするのとカウンターをインクリメント
# 全部3200の場合が困るので最小値はmin(1, flagのTrueの数)
# 最大値はflagのTrueの数+カウンターの数

# ------------------- 解答 --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

color = [False]*8
higher = 0

for a in A:
    if 1 <= a <= 399: color[0] = True
    elif 400 <= a <= 799: color[1] = True
    elif 800 <= a <= 1199: color[2] = True
    elif 1200 <= a <= 1599: color[3] = True
    elif 1600 <= a <= 1999: color[4] = True
    elif 2000 <= a <= 2399: color[5] = True
    elif 2400 <= a <= 2799: color[6] = True
    elif 2800 <= a <= 3199: color[7] = True
    elif 3200 <= a: higher += 1

minimum = max(1, sum(color))
maximum = sum(color) + higher
print(minimum, maximum)

# ------------------ 入力例 -------------------
10
1 400 800 1200 1600 2000 3300 3300

3
3300 3300 3300

4
2100 2500 2700 2700

5
1100 1900 2800 3200 3200

20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990

# ----------------- 解答時間 ------------------
# 13分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc064/editorial.pdf
# 「3200以上は好きな色に変えられる=8色のうちのどれか」だと思ってたら，本当に何でも良かった。
# ここを勘違いしてWAだした

# ----------------- カテゴリ ------------------
#AtCoder #abc
#flagを上手く使う

