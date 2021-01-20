# AGC043A - Range Flip Find Route
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc043/tasks/agc043_a
# Date: 2021/01/11 

# ---------- Ideas ---------- 
# n<=100なのでO(n^4)で解きそう=1億ループ
# 基本はBFS
# 右or下にしか進めないので左や上に行くパターンは考えなくていい
# 直感的には全探索で解く感じの問題っぽい
# 白を黒にした方がいい場合というのはあるのか？ -> ありそう

# 反転する長方形を選ぼうとすると，左上と右下の座標を選ぶ必要があって，それだけでO(N^4)になる
# というか反転が複数回起こるのであれば長方形を何度も選ぶことになるので，絶対に駄目

# あるマスに行くために必要な反転回数をdpで更新していく?
# 全探索しながら貰うDP

# ------------------- Solution -------------------- 
# 一つ前が白で，自分が黒の時には反転の回数が増える
# それ以外の場合は一つ前までの操作回数と同じ
# 左から来る場合と上から来る場合で場合分けする

# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
G = [input() for _ in range(h)]

inf = float('INF')
dp = [[inf]*w for _ in range(h)] # 座標(x,y)にくるまでに反転する必要のある回数
if G[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for y in range(h):
    for x in range(w):
        if x == y == 0: continue

        # 左から来るとき
        if x > 0:
            if G[y][x - 1] == '.' and G[y][x] == '#':
                dp[y][x] = min(dp[y][x], dp[y][x - 1] + 1)
            else:
                dp[y][x] = min(dp[y][x], dp[y][x - 1])

        # 上から来るとき
        if y > 0:
            if G[y - 1][x] == '.' and G[y][x] == '#':
                dp[y][x] = min(dp[y][x], dp[y - 1][x] + 1)
            else:
                dp[y][x] = min(dp[y][x], dp[y - 1][x])
print(dp[h-1][w-1])


# ------------------ Sample Input -------------------
3 3
.##
.#.
##.

2 2
#.
.#

5 5
.#.#.
#.#.#
.#.#.
#.#.#
.#.#.


# ----------------- Length of time ------------------
# 40分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc043/editorial.pdf
# ガッツリ目のDPを初見で解けて嬉しい
# 全探索を諦めてDPに気づけたことが何より素晴らしい
#


# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-medium
#動的計画法
#DP
#grid
#マスの反転
#最小回数
#最小コスト
#緑diff

