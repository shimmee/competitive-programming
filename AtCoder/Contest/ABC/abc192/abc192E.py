# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192): E - Train
# URL: https://atcoder.jp/contests/abc192/tasks/abc192_e
# Date: 2021/02/20

# ---------- Ideas ----------
# ダイクストラに待ち時間の要素をいれる
# 各頂点において今何時か = dist
# 次のKの倍数まであと何分掛かるか = 次の出発時間 ceil(dist/k) * k - dist

# ------------------- Answer --------------------
code:python
    import math
    from heapq import heappush, heappop

    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1
    G = [[] for _ in range(n)]

    # グラフは隣接リストで行き先と重みをセットに格納する
    for i in range(m):
        a, b, t, k = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append([b, t, k])
        G[b].append([a, t, k])

    # 始点から各頂点までの最短距離をinfで初期化: 時間も表す
    inf = float('INF')
    dist = [inf]*n
    dist[x] = 0 # 始点の設定

    que = [] # ヒープに入れる空のリスト
    heappush(que, (0, x))

    while que:
        c, a = heappop(que)
        if dist[a] < c:
            continue
        for b, t, k in G[a]:
            # kの倍数が最初にdist[a]を超える
            q = math.ceil(dist[a]/k)
            wait = q*k - dist[a]
            if dist[b] > dist[a] + t + wait: # 距離の更新
                dist[b] = dist[a] + t + wait
                heappush(que, (dist[b], b))

    print(dist[y] if dist[y] != inf else -1)



# ------------------ Sample Input -------------------
9 14 6 7
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
2 3 8 4
6 2 6 4
3 8 3 2
7 9 5 2
8 4 1 9
7 1 6 9
3 9 9 3
7 5 1 5
8 2 9 7
4 9 4 4


3 2 1 3
1 2 2 3
2 3 3 4

3 2 3 1
1 2 2 3
2 3 3 4

# ----------------- Length of time ------------------
# 本番30分でAC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc192/editorial
# これ解けたおかげでパフォ1388出せた!!
# 待ち時間がある系は電車の問題でいくつか解いたことがあったから，慣れたものだった。

# ----------------- Category ------------------
#AtCoder
#ABC-E
#ダイクストラ
#電車
#djkstra
#最短経路問題
#待ち時間