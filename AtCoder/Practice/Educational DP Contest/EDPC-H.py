# Educational DP Contest: H - Grid 1
# URL: https://atcoder.jp/contests/dp/tasks/dp_h
# 日付: 2020/12/26

# ---------- 思ったこと / 気づいたこと ----------
# 右or下にいくだけなので，2方向の移動だけ考えればいい
# グリッドが小さかったら？というのを考えて(部分問題)，それをふくらませるかんじ

# ------------------- 方針 --------------------
# dp[y]x]: マス(x,y)に行くまでの通り
# dp[y][x] = dp[y-1][x] + dp[y][x-1]
# 初期値はスタートのマスが1

# ------------------- 解答 --------------------
#code:python
mod = 10**9+7
h, w = map(int, input().split())
a = [input() for _ in range(h)]

dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for y in range(h):
    for x in range(w):
        if a[y][x] == '.': # 白マスのときのみ移動可能
            if y-1 >= 0:
                dp[y][x] += dp[y - 1][x]
            if x-1 >= 0:
                dp[y][x] += dp[y][x - 1]
        dp[y][x] %= mod
print(dp[h-1][w-1])

# ------------------ 入力例 -------------------
3 4
...#
.#..
....

5 2
..
#.
..
.#
..

5 5
..#..
.....
#...#
.....
..#..

20 20
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................

# ----------------- 解答時間 ------------------
# 6分

# -------------- 解説 / 感想 / 反省 -------------
# 簡単だった！

# ----------------- カテゴリ ------------------
#EDPC
#動的計画法
#DP
#グリッドDP
#経路の数