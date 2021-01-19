# ABC099 C - Strange Bank
# URL: https://atcoder.jp/contests/abc099/tasks/abc099_c
# 日付: 2020/11/20

# ---------- 思ったこと / 気づいたこと ----------
# DPやん。コインの典型問題

# ------------------- 方針 --------------------
# 100000円以下なので，コインのパターンを列挙する
# coinのリストを使ってDP書く (昔のコードのコピペ)

# ------------------- 解答 --------------------
#code:python
n = int(input())
inf = float('INF')

coin = [1]
six = [6**i for i in range(1, 7)]
nine = [9**i for i in range(1, 6)]

coin = coin + six + nine
coin.sort()
m = len(coin)

dp = [[inf for j in range(n+1)] for i in range(m+1)]
# dp[i][j]: コインをi枚目までつかって，j円を払う時に必要な最低枚数
dp[0][0] = 0

for i in range(m):
    for j in range(n+1):
        # i枚目のコインを使う時
        if j-coin[i] >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-coin[i]] + 1)

        # i枚目のコインを使わない時
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
print(dp[m][n])

# これでAC!
# 「コインを何枚でもつかえる」や「部分和問題で何度でも数を使っていい」場合は1次元でいい
n = int(input())
inf = float('INF')

coin = [1] + [6**i for i in range(1, 7)] + [9**i for i in range(1, 6)]
coin.sort()
m = len(coin)

dp = [inf]*(n+1)
dp[0] = 0

for i in range(1, n+1): # i円を使いたい
    for j in range(m): # j枚目のコイン
        # j枚目のコインを使う時
        if i-coin[j] >= 0:
            dp[i] = min(dp[i], dp[i-coin[j]]+1)
print(dp[n])

# ------------------ 入力例 -------------------
10
127
44852


# ----------------- 解答時間 ------------------
# 8分！！

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc099/editorial.pdf
# 典型問題なので昔のコードをコピペできた
# 2次元のdpテーブル作ったけど，実は1次元でいい。
# 「コインを何枚でもつかえる」や「部分和問題で何度でも数を使っていい」場合は1次元でいい

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#動的計画法 #DP
