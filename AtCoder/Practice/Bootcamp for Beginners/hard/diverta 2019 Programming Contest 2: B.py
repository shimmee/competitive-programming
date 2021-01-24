# diverta 2019 Programming Contest 2: B - Picking Up
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_b
# Date: 2021/01/21

# ---------- Ideas ----------
# 座標をpでソートすると，x軸について昇順になる
# 全座標の総当りの組み合わせで，p=a[i]-a[j]とq=b[i]-b[j]を計算してみる。
# (p, q)の候補のリストを作る
# [p, q]が最も多い組み合わせの個数 (出現回数が最も多い)をmとする
# n-mが答え

# ------------------- Answer --------------------
#code:python
n = int(input())
xy = [[int(i) for i in input().split()] for _ in range(n)]

l = [] # (p, q)の候補
for i in range(n):
    for j in range(i+1, n):
        p = xy[i][0] - xy[j][0]
        q = xy[i][1] - xy[j][1]

        l.append([p, q])

# 各(p,q)の出現回数を数える
cnt_max = 0
for a in l:
    # p!=0 または q!=0 のときのみOK
    if a[0] != 0 or a[1] != 0:
        cnt = 0
        for b in l:
            if a == b or (a[0] == -b[0] and a[1] == -b[1]):
                cnt += 1
        cnt_max = max(cnt_max, cnt)

print(n-cnt_max)
# 18/23WA ひどすぎる
# 順番が逆で(p,q) = (-p, -q)もOKというのを考慮してなかった。これを入れたらAC

# ------------------ Sample Input -------------------
6
1 1
1 2
2 1
2 2
1 3
2 3

4
1 2
1 3
1 4
1 5


2
1 1
2 2

3
1 4
4 6
7 8

4
1 1
1 2
2 1
2 2

# ----------------- Length of time ------------------
# 50分: 18分で提出したけど色々バグってWAになって50分もかかった

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/diverta2019-2/editorial.pdf
# 解説がまどろっこしい。
# 自分が解いた解法で解いてる記事がほとんど。事前にp,qの候補を出さなくても，最初から4重ループで行けた: O(N^4)
# https://note.com/peacockred/n/n6a93934cda29
# https://yamakasa.net/atcoder-diverta-2019-programming-contest-2-b/

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#全探索
#2点の座標の一致
#緑diff
#4重ループ