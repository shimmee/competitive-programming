# ABC047B - すぬけ君の塗り絵 2 イージー
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc047/tasks/abc047_b
# 日付: 2020/12/31

# ---------- 思ったこと / 気づいたこと ----------
# 白く残ってる頂点の値を管理して，Queryが与えられる事に狭めていく

# ------------------- 解答 --------------------
#code:python
w, h, n = map(int, input().split())
x1, x2, y1, y2 = 0, w, 0, h

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and x >= x1: x1 = min(x, x2)
    elif a == 2 and x <= x2: x2 = max(x, x1)
    elif a == 3 and y >= y1: y1 = min(y, y2)
    elif a == 4 and y <= y2: y2 = max(y, y1)

print((x2-x1)*(y2-y1))

# ------------------ 入力例 -------------------
5 4 2
2 1 1
3 3 4

5 4 3
2 1 1
3 3 4
1 4 2

10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3

# ----------------- 解答時間 ------------------
# 14分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/arc/063/editorial.pdf
# 茶色後半をスムーズに溶けた！嬉しい！
# 最後にマイナスになった面積を0になおす方法だとコーナーケースでWAになった
# 各クエリの処理中に，x1>x2やy1>y2とならないように処理する必要があった。


# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium