# CODE FESTIVAL 2015 あさぷろ Middle: B - ヘイホー君と削除
# URL: https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_d
# Date: 2021/03/16

# ---------- Ideas ----------
# 一番長い平方文字列を探せばよい
# 平方文字列の長さは必ず偶数
# 1回しか出現してない文字は絶対に使えない: たぶんこの処理をしても問題の本質は変わらない
# DPか？
# 半分に切って左右を揃える，みたいなこともできない。右半分だけで完成させるケースがありうるから。

# ------------------- Solution --------------------
# 暇な時に1時間くらい考えてやっとアイデアにたどり着いた
# 文字列をsとtをくっつけたものと見なして，sとtを一致させるような操作をしたら，s+tは平方文字列になる
# 2つの文字列を一致させるような操作の最小回数はレーベンシュタイン距離としてDPで計算できる
# N<=100で分け方は99通りなので，sとtの分け方をすべて試して，最小の操作回数を得ればよさそう
# dp[i][j]: sのi文字目までとtのj文字目までを一致させるのに必要な操作回数
# 一度マッチさせた文字は使えないので，使用可能な文字のカウンターが必要


# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()

inf = float('INF')
ans = inf
for k in range(1, n):
    s = S[:k]
    t = S[k:]

    dp = [[inf for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    dp[0][0] = 0
    # dpテーブルの初期化
    for i in range(len(s)):
        for j in range(len(t)):
            if i == 0:
                dp[i][j+1] = dp[i][j] + 1
            if j == 0:
                dp[i+1][j] = dp[i][j] + 1

    # dpテーブルの更新
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) - 1
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + 1

    ans = min(ans, dp[len(s)][len(t)])
print(ans)

# サンプル4つめが合いません。Give upです。
# ここまで2時間よく頑張った...
# レーベンシュタイン距離ではなく，最長共通部分列問題だった。
# sとtに分けて，sとtに共通する最長の部分列を見つける問題だった
# dp[i+1][j+1] :=Sのi文字目までとTのj文字目まででのLCSの長さ

n = int(input())
S = input()

inf = float('INF')
ans = inf
for k in range(n+1):
    s = S[:k]
    t = S[k:]

    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

    # dpテーブルの更新
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    # 共通部分の長さがdp[len(s)][len(t)]なので，削るべき長さはn-2*dp[len(s)][len(t)]
    ans = min(ans, n-2*dp[len(s)][len(t)])
print(ans)


# ------------------ Sample Input -------------------
8
abacbabc

8
abababab

26
codefestivaltwozeroonefive

# ----------------- Length of time ------------------
# 2時間かけて解説AC

# -------------- Editorial / my impression -------------
# https://at274.hatenablog.com/entry/2020/06/06/001432
# 編集距離だと勘違いして2時間溶かした
# 最長共通部分列問題(Longest Common Subsequence: LCS)だった
# dpテーブルの持ち方自体は編集距離と同じだけど，初期値は0だし，遷移の仕方も違った。
# s[i]==t[j]のとき，斜めに遷移するのが重要なポイント
# これは復習が必要

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#最長共通部分列問題
#LCS
#DP
#動的計画法
#二次元DP
