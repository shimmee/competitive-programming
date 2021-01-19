# Educational DP Contest: I-Coins
# URL: https://atcoder.jp/contests/dp/tasks/dp_i
# 日付: 2020/12/25

# ---------- 思ったこと / 気づいたこと ----------
# dpテーブルの持ち方がわからず，ヒントをみた: https://www.creativ.xyz/dp-practice/
# dp[i][j]: i番目までのコインのうち，表になるコインがj枚の確率

# ------------------- 方針 --------------------
# dp[i][j] = (i-1)枚で表が(j-1)枚の状態からi枚目が表になる確率 + (i-1)枚で表がj枚の状態からi枚目が裏になる確率
# つまり，あるjに対して表が1枚少ない状態からi枚目を表で出すか，表が十分揃ってる状態でi枚目を裏で出すか

# ------------------- 解答 --------------------
#code:python
n = int(input())
p = list(map(float, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1 # 初期値: 0枚使って0枚表にする確率は1としておく

for i in range(n):
    for j in range(n+1):
        if j == 0: # i枚目で表が0枚になる確率は，i-1枚目まで全部裏でi枚目も裏
            dp[i+1][j] = dp[i][j]*(1-p[i])
        else:
            dp[i + 1][j] = dp[i][j-1]*p[i] + dp[i][j] * (1 - p[i])
print(sum(dp[n][(n+1)//2:]))


# ------------------ 入力例 -------------------
3
0.30 0.60 0.80

1
0.50

5
0.42 0.01 0.42 0.99 0.42

# ----------------- 解答時間 ------------------
# 60分以上

# -------------- 解説 / 感想 / 反省 -------------
# 最初は一次元の配列dp[i]=(i枚目のコインまで投げたとき、表が出たコインの数の方が多い確率)で考えてたけど上手く行かなかった
# 「表の枚数の情報が必要だ」ということに気づければ，配列を二次元でもつ発想に至るっぽい

# ----------------- カテゴリ ------------------
#EDPC
#動的計画法
#DP
#ヒントAC #復習したい