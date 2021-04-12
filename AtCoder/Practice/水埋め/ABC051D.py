# ABC051D - Candidates of No Shortest Paths
# URL: https://atcoder.jp/contests/abc051/tasks/abc051_d
# Date: 2021/04/08

# ------------------- Solution --------------------
# ワーシャルフロイドで最短経路求めてから，経路復元
# このページの最後の方法: http://zeosutt.hatenablog.com/entry/2015/05/05/045943
# すべての点同士の最短経路が求まったら，任意の2つの点同士の最短経路を復元して，入力で与えられた辺を通るかどうか確認する

# ------------------- Answer --------------------
#code:python
from copy import deepcopy
n, m = map(int, input().split())
inf = float('INF')
ab = [[] for _ in range(n)]
dp = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)
    dp[a - 1][b - 1] = c
    dp[b - 1][a - 1] = c

# スタートとゴールが同じ場合(i=jのとき)は距離がゼロ
for i in range(n):
    dp[i][i] = 0

dp_raw = deepcopy(dp)

# ワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 通過した経路のbool
passed = [[True]*n for _ in range(n)]
for a in range(n):
    for b in ab[a]:
        passed[a][b] = False
        passed[b][a] = False

# 経路復元: 通過したらpassedの辺をTrueにする
for s in range(n): # スタート
    for g in range(n): # ゴール
        cur = s
        while cur != g:
            for i in range(n):
                if i != cur and dp_raw[cur][i] + dp[i][g] == dp[cur][g]:
                    passed[i][cur] = True
                    passed[cur][i] = True
                    cur = i
                    break

# 使われてない辺を数える
ans = 0
for i in range(n):
    for j in range(n):
        if not passed[i][j]:
            ans += 1
print(ans//2)


# 1時間くらいかかったけど3ケースWA
# 解説みたらダイクストラでも解けるっぽい
# 単一始点とみなして，ダイクストラを行い，それをn頂点分行う
# 経路復元: https://algo-logic.info/dijkstra/

from heapq import heappush, heappop
n, m = map(int, input().split())
inf = float('INF')
G = [[] for _ in range(n)]
inf = float('INF')

for _ in range(m):
    a,b,c = map(int, input().split())
    G[a - 1].append([b - 1, c])
    G[b - 1].append([a - 1, c])

# 通過した経路のbool: 通過してたらTrue
# 入力の辺だけFalseにして初期化
passed = [[True]*n for _ in range(n)]
for v in range(n):
    for e, w in G[v]:
        passed[v][e] = False
        passed[e][v] = False

# 始点から各頂点までの最短距離をinfで初期化
for s in range(n):
    dist = [inf]*n
    dist[s] = 0 # 始点の設定
    prev = [-1]*n # どこを通ったか記録するリスト (直前の頂点を入れる)

    que = [] # ヒープに入れる空のリスト
    heappush(que, (0, s))

    # ダイクストラ
    while que:
        c, v = heappop(que)
        if dist[v] < c: #
            continue
        for e, w in G[v]:
            if dist[e] > dist[v] + w: # 距離の更新
                dist[e] = dist[v] + w
                prev[e] = v
                heappush(que, (dist[e], e))

    # 経路復元: スタートsから他の点gへの経路
    # ゴールgからprevを経由してsまで遡る
    for g in range(n):
        path = [] # 通った経路: gからsまで
        cur = g
        while cur != -1:
            path.append(cur)
            cur = prev[cur]

        # 通った経路を確認する
        for i in range(len(path)-1):
            a = path[i]
            b = path[i+1]

            passed[a][b] = True
            passed[b][a] = True

# 使われてない辺を数える
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if not passed[i][j]:
            ans += 1
print(ans)

# AC!!

# ------------------ Sample Input -------------------

3 3
1 2 1
1 3 1
2 3 3

3 2
1 2 1
2 3 1

# ----------------- Length of time ------------------
# ほぼいけてたけど解説AC?

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc051/editorial.pdf
# ワーシャルフロイドでWAが出た理由が未だにわからない
# どちらにしても，ワーシャルフロイドとダイクストラの経路復元の勉強になったから良かった
# けんちょんさn: https://drken1215.hatenablog.com/entry/2019/02/15/141000

# ----------------- Category ------------------
#AtCoder
#ABC-D
#最適解に含まれる可能性がない要素を挙げる
#グラフ問題
#必要条件を列挙したら十分条件になる
#最短路問題
#Floyd-Warshall法
#前処理
#Dijkstra法
#復元
#経路復元
#ワーシャルフロイド
#ダイクストラ
#前処理:Floyd-Warshall法
#グラフの考えるべき辺数を減らす
#水色diff


