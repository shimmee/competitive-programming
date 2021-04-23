# CODE FESTIVAL 2014 Easy C - 身体バランス
# URL: https://atcoder.jp/contests/code-festival-2014-morning-easy/tasks/code_festival_morning_easy_c
# Date: 2021/04/19

# ---------- Ideas ----------
# sからu, uからtへの最短距離が同じになるような組があればよくて
# n <= 1000なのでワーシャルフロイドがギリギリ間に合うかも -> 無理でした
# sから他の点へのダイクストラ
# 全点uからtへのダイクストラ
# s->uとu->tが同じになるようなuがあればOK

# ------------------- Answer --------------------
#code:python
inf = float('INF')
n, m = map(int, input().split())
s, t = map(int, input().split())
s -= 1
t -= 1

# dp[k][i][j]: 頂点0, 1, ..., k-1のみを中継頂点として通って良いとした場合の頂点iから頂点jへの最短距離
# kをin-placeに表現すれば，二次元配列で十分
dp = [[inf for _ in range(n)] for _ in range(n)]

# dpの各要素がaからbへの重みを表すので，入力の有向グラフを初期状態として埋め込む
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = w
    dp[b][a] = w

# スタートとゴールが同じ場合(i=jのとき)は距離がゼロ
for i in range(n):
    dp[i][i] = 0

# 新たに頂点kを使用しない場合: dp[k][i][j]
# 新たに頂点kを使用する場合: dp[k][i][k] + dp[k][k][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


for u in range(n):
    if dp[s][u] == dp[u][t]:
        print(u+1)
        exit()
else:
    print(-1)

# ワーシャルフロイドは10億計算でした
# ダイクストラする
# sから他の点へのダイクストラ
# 全点からtへのダイクストラ

from heapq import heappush, heappop
inf = float('INF')
n, m = map(int, input().split())
s, t = map(int, input().split())
s -= 1
t -= 1

if s==t:
    print(-1)
    exit()

G = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    G[a - 1].append([b - 1, w])
    G[b - 1].append([a - 1, w])

if G[s] == t and len(G[s]) == 1:
    print(-1)
    exit()

dist_s = [inf] * n
dist_s[s] = 0  # 始点の設定

que = []  # ヒープに入れる空のリスト
heappush(que, (0, s))

while que:
    c, v = heappop(que)
    if dist_s[v] < c:  #
        continue
    for e, w in G[v]:
        if dist_s[e] > dist_s[v] + w:  # 距離の更新
            dist_s[e] = dist_s[v] + w
            heappush(que, (dist_s[e], e))

dist_u = []
for u in range(n):
    dist = [inf] * n
    dist[u] = 0  # 始点の設定

    que = []  # ヒープに入れる空のリスト
    heappush(que, (0, u))

    while que:
        c, v = heappop(que)
        if dist[v] < c:
            if v == t: # uからtへの最短距離が確定しているので，breakしてOK: 枝刈り
                break
            else:
                continue
        for e, w in G[v]:
            if dist[e] > dist[v] + w:  # 距離の更新
                dist[e] = dist[v] + w
                heappush(que, (dist[e], e))
    dist_u.append(dist)


for u in range(n):
    if dist_s[u] == dist_u[u][t] and dist_s[u] != inf:
        print(u+1)
        exit()
else:
    print(-1)

# ------------------ Sample Input -------------------
3 3
1 2
1 3 3
3 2 3
1 2 1

4 4
1 3
1 2 2
1 4 3
2 4 3
3 4 5

# ----------------- Length of time ------------------
# 33分

# -------------- Editorial / my impression -------------
# 解説なかった
# 最初ワーシャルフロイドして死んだ
# 間に合うかと思ったら10億ループだった
# ダイクストラで書いても結局1ケースTLEになったので，u->sのダイクストラの中で，すでにsへの最短距離が確定してる場合に枝刈りをした
# 他の点からスタートするこの類のダイクストラはよくでるから覚えておくべし
# 典型90問と同じような問題！

# 無向グラフの場合，ほか頂点からtへの最短距離は，tからのほか頂点の最短距離と同じなので，全点uからダイクストラする必要がなかった！！！！

# ----------------- Category ------------------
#AtCoder
#枝刈り
#ダイクストラ
#djikstra
#最短路問題
#2頂点からダイクストラ
#2回ダイクストラ