# ABC136D - Gathering Children
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc136/tasks/abc136_d
# Date: 2021/01/11 

# ---------- Ideas ----------
# RLという場所に最終的に皆集まる
# Rにとっては右側にある一番近いL，Lにとっては左側にある一番近いRのあたりにいく
# 距離の偶奇で1マス変わる

# ------------------- Solution -------------------- 
# RとLのインデックスを保存する
# 各Rから一番近い右側のLのインデックス， 各Lから一番近い左側のRのインデックスを得る
# 各文字から移動先までの距離が偶数ならそこ，奇数のとき，LからRならi+1に，RからLならi-1に行く

# ------------------- Answer --------------------
#code:python
from collections import deque
S = input()
n = len(S)

# RとLのインデックスを保存する
R = deque([])
L = deque([])
for i in range(n):
    if S[i] == 'R': R.append(i)
    else: L.append(i)


dist = [-1]*n

# 各Rから一番近い右側のLのインデックス
l = L.popleft()
for i in range(n):
    if S[i] == 'R':
        while l < i:
            l = L.popleft()
        dist[i] = l

# 各Lから一番近い左側のRのインデックス
r = R.pop()
for i in reversed(range(n)):
    if S[i] == 'L':
        while r > i:
            r = R.pop()
        dist[i] = r

# 各文字から移動先までの距離が偶数ならそこ，奇数のとき，LからRならi+1に，RからLならi-1に行く
ans = [0]*n
for i in range(n):
    d = abs(i-dist[i])
    if d % 2 == 0:
        ans[dist[i]] += 1
    else:
        if S[i] == 'L':
            ans[dist[i] + 1] += 1
        else:
            ans[dist[i] - 1] += 1
for i in range(n):
    print(ans[i], end = ' ')




# ------------------ Sample Input -------------------
RRLRL

RRLLLLRLRRLL

RRRLLRLLRRRLLLLL

# ----------------- Length of time ------------------
# 35分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc136/editorial.pdf
# ループ5回も書いて時間かかっちゃった。1回のループで解いてる人いて凄い
# ダブリングという繰り返し二乗法を使う方法でも解けるらしい

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-medium
