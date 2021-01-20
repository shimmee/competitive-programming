# Educational DP Contest: F - LCS
# URL: https://atcoder.jp/contests/dp/tasks/dp_f
# 日付: 2020/12/26

# ---------- 思ったこと / 気づいたこと ----------
# O(|s|*|t|)で解くんだろう3000**2

# ------------------- 方針 --------------------
# まずは最長共通部分列(LCS)の長さをDPで得て，そのあと経路復元する
# dp[i][j]: sのi文字目までとtのj文字目までのLCS
# s==tのとき，dp[i][j]はdp[i-1][j-1]の状態から一致文字が1文字増えるので，dp[i-1][j-1]+1
# s!=tのとき，上から左からのmax

# 経路復元: https://www.creativ.xyz/dp-practice/

# ------------------- 解答 --------------------
#code:python
s = input()
t = input()
n = len(s)
m = len(t)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):

        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

# 経路復元は逆をたどる
# i=|S|,j=|T|として開始する。「答えの文字列」は最初、空文字列とする。
# dp[i][j]の値がdp[i−1][j]と一致する場合、Sのi文字目は使用しないので、iの値を1減らす。
# dp[i][j]の値がdp[i][j−1]と一致する場合、Tのj文字目は使用しないので、jの値を1減らす。
# dp[i][j]の値がdp[i−1][j−1]+1と一致する場合、Sのi文字目がTのj文字目と一致するので、その文字を「答えの文字列」に追加し、i,jを1減らす。
# これをi,jのどちらかが0になるまで続ける。
# そうして得られた「答えの文字列」を反転させたものが、求める LCS である。

ans = ''
i = n
j = m
flag = False
while i > 0:
    if i <= 0 or j <= 0:
        flag = True
    while j > 0:
        if i <= 0 or j <= 0:
            flag = True
            break
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        elif dp[i][j] == dp[i-1][j-1]+1:
            ans += s[i-1]
            i -= 1
            j -= 1
    if flag: break
print(ans[::-1])

# ------------------ 入力例 -------------------
abcd
becd

axyb
abyxb

aa
xayaz

abracadabra
avadakedavra

# ----------------- 解答時間 ------------------
# 1時間？

# -------------- 解説 / 感想 / 反省 -------------
# https://kyopro-friends.hatenablog.com/entry/2019/01/12/231000
# 長さを求めるだけの問題ならなんとかなりそうだけど，経路復元が難しい

# ----------------- カテゴリ ------------------
#EDPC
#動的計画法
#DP
#ヒントAC #復習したい
#最長共通部分列
#LCS
#経路復元