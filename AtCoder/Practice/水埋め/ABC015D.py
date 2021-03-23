# ABC015D - 高橋くんの苦悩
# URL: https://atcoder.jp/contests/abc015/tasks/abc015_4
# Date: 2021/03/17

# ---------- Ideas ----------
# ナップザックDPっぽいけどなんか違う
# N <= 50なので，
# スクラッチで描いてみよう
# 3次元DPか？ いや，2次元でいける
# dp[i][j]: 幅がjまででi枚選んだときの最大価値
# 3重ループで書くが，普通に書くと一度使ったa,bをまた使ってしまうのが問題


# ------------------- Answer --------------------
#code:python
w = int(input())
n, k = map(int, input().split())
abc = []
for i in range(n):
    a, b = map(int, input().split())
    abc.append([a,b,i])


dp = [[0 for _ in range(w+1)] for _ in range(k+1)]
used = [[set() for _ in range(w+1)] for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, w+1):
        value = 0
        using = None
        flag = False
        for a, b, c in abc:
            if j-a >= 0 and (not c in used[i-1][j-a]):
                if value < dp[i-1][j-a] + b:
                    value = dp[i-1][j-a] + b
                    using = c
                    pre_using = used[i-1][j-a]
                    flag = True
        if flag:
            used[i][j].update(pre_using)
            used[i][j].update([using])
            dp[i][j] = max(dp[i][j], value)
print(max(map(max, dp)))

# 11ケースMLE!!! 珍しい。ほかは36ケースAC
# 10000*50*50の配列を持ってるからこうなってるっぽい
# 解説みた: 3次元DPで解くか，2次元DPなら「同じスクショを2回以上使わないための工夫」が必要
# 今回は使用済みスクショをsetで管理しようとしたから，MLEになってた
# とても惜しいところまでいってた
# 解説の工夫はループの向きを逆にすることらしい

w = int(input())
n, k = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]

dp = [[0 for _ in range(w+1)] for _ in range(k+1)]
for a, b in ab:
    for i in reversed(range(k+1)):
        for j in range(w+1):
            if i >= 1 and j-a >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-a] + b)
print(dp[k][w])

# これでAC
# なんで逆にすればうまくいくのかよくわからんから，3次元dpで描いてみる
# dp[i][j][k]: i番目までのスクショのうち，幅がjまでで，k枚選んだときの最大価値
# i番目を使わない時は，i-1番目までと全く同じなので dp[i-1][j][k]
# i番目を使うときは，i-1番目のk-1枚目の，j-a幅からの推移になるのでdp[i-1][j-a][k-1]
# これじゃだめかも?
# 下で頑張ったけど結局バグってだめだったので復習したい

W = int(input())
N, K = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[[0 for _ in range(K+1)] for _ in range(W+1)] for _ in range(N+1)]

for i in range(N): # i枚目まで使用可能
    a, b = ab[i-1]
    for j in range(1, W+1): # 幅jまで
        for k in range(K): # k枚使用する
            if j-a >= a:
                dp[i+1][j][k] = max(dp[i][j][k], dp[i][j-a][k+1] + b)
            else:
                dp[i+1][j][k] = dp[i][j][k]
print(dp[N][W][K])




# ------------------ Sample Input -------------------
10
3 2
4 20
3 40
6 100

10
5 4
9 10
3 7
3 1
2 6
4 5



22
5 3
5 40
8 50
3 60
4 70
6 80


# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# ナップサックDPの亜種だった
# 2次元dpで逆から回すというアイデアが思いつかなかった
# 解説見ても3次元dpを結局書ききれなかったので，復習したい

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#逆からdp
#3次元dp
#ナップサックdp
#動的計画法