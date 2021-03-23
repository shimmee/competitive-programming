# ABC141E - Who Says a Pun?
# URL: https://atcoder.jp/contests/abc141/tasks/abc141_e
# Date: 2021/03/17

# ---------- Ideas ----------
# ヘイホー君と削除に似てる
# ヘイホーくんはN<=100だったからO(N^3)で解けたけど，これはN < 5000だから，O(N^2)で解くっぽい
# 普通のLCSはSのi文字目とTのj文字目が一致してたら+1して更新するが，
# 今回はSとTが全く同じ文字列なので，普通にLCSやると全部が一致してしまう。
# i<=jの場合にはスキップする処理が必要


# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()[::-1]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
flag = False
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i+1 == j and dp[i-1][j-1] > 0:
            flag = True

        if not flag:
            if S[i-1] == S[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        else:
            if S[i-1] == S[j-1]:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1]

print(max(map(max, dp)))

# 5AC 60ケースWA: ひどいぜ
# たぶん解法が間違ってるぜ
# 解説見た: Z-Algorithmってやつかローリングハッシュで解けるらしい。両方知らん
# けんちょんさんは5つの方法載せてて，DPでも解けるらしい: https://drken1215.hatenablog.com/entry/2019/09/16/014600
# けんちょんさんのDP解がこれ
# dp[i][j]: Sをiからと，Sをjから始めた時に，一致する最大の接頭辞の長さ
# S[i] != S[j] なら dp[i][j] = 0
# そうでないなら dp[i][j] = dp[i+1][j+1] + 1
# テーブルを埋めた後，制約に違反しないように，dp[i][j] < j-i+1となる場合のみansを更新

n = int(input())
S = input()

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in reversed(range(n)):
    for j in reversed(range(n)):
        if S[i] == S[j]:
            dp[i][j] = dp[i+1][j+1] + 1
ans = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] < j-i+1:
            print(i, j)
            ans = max(ans, dp[i][j])
print(ans)

# 最後の部分「制約に違反しないように，dp[i][j] < j-i+1となる場合のみansを更新」がよくわからん

# ------------------ Sample Input -------------------
6
aabbaa

5
ababa

2
xy

13
strangeorange


# ----------------- Length of time ------------------
# 1時間かけて解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc141/editorial.pdf
# 解説見た: Z-Algorithmってやつかローリングハッシュで解けるらしい。両方知らん
# けんちょんさんや動画解説，他の解説ブログはみんなDPで解いてた
# i=0,j=0から埋めていくのではなく，i=n,j=nの後ろから手前に埋めていく
# どうやって思いつくんだろう

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#DP
#動的計画法
#文字列操作
#最長共通部分列問題
#逆からdp