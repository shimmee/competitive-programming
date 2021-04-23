# ABC191E - Come Back Quickly
# URL: https://atcoder.jp/contests/abc191/tasks/abc191_e
# Date: 2021/04/20

# ---------- Ideas ----------
# 多重辺があるので，入力の時点で除く?
# 自己辺があるので，とりあえず自己辺もグラフ入力に入れておく
# 各街をスタートとするダイクストラを行い，距離の行列を作る
# スタートとゴールの組み合わせをループで調べて，最小距離を出力

# 入力の際の自己ループと多重辺の扱いに注意

# ------------------- Answer --------------------
#code:python
class djikstra():
    def __init__(self, n, graph, start):
        """
        ヒープを用いたダイクストラ法: 計算量はO((V+E)logV)
        :param graph: 隣接リスト
        :param start: 0-indexでのスタートの頂点
        :return: スタートから各頂点への距離リスト
        """
        self.n = n
        self.graph = graph
        self.start = start
        self.prev = [-1]*n # 経路復元用のリスト (直前の頂点を入れる)


    def run_djikstra(self):

        from heapq import heappush, heappop
        inf = float('INF')
        dist = [inf] * self.n
        dist[self.start] = 0

        que = []
        heappush(que, (0, self.start))

        while que:
            c, v = heappop(que)  # まだ未確定の頂点から最短距離が分かっていて最も距離が短い頂点を探して確定する
            if dist[v] < c:  # 距離が確定しているならcontinue
                continue
            for u, w in self.graph[v]:  # vから辿れる頂点を全て巡る
                if dist[u] > dist[v] + w:  # 距離が短くなる場合は更新
                    dist[u] = dist[v] + w
                    self.prev[u] = v # 経路復元用に保存
                    heappush(que, (dist[u], u))  # 更新されたらキューに値を追加
        return dist

    def restore_route(self, goal):
        """
        参考: https://algo-logic.info/dijkstra/
        :param goal: 0-indexでのゴールの頂点
        :return:
        """
        if self.prev == [-1]*self.n:
            print('Run run_djikstra() first')
            return
        else:
            path = []  # 通った経路: gからsまで
            cur = goal
            while cur != -1:
                path.append(cur)
                cur = self.prev[cur]

            return path[::-1]

n, m = map(int, input().split())
G = [[] for _ in range(n)]
inf = float('INF')
selfloop = [inf]*n
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    # 自己ループの処理
    if a == b:
        selfloop[a] = min(selfloop[a], c)

    # 多重辺の処理: もし同じ辺がすでにあって，新しい道のほうが短ければ上書きする
    for i in range(len(G[a])):
        u, w = G[a][i]
        if u == b:
            if c <= w:
                G[a][i] = [u, c]
            break
    else:
        G[a].append([b, c])

# 全点出発のダイクストラ
dist = []
for i in range(n):
    model = djikstra(n, G, i)
    dist.append(model.run_djikstra())

# スタートとゴールの組み合わせ
for s in range(n):
    ans = selfloop[s] # 初期値は自己ループの長さ
    for g in range(n):
        if s == g: continue
        ans = min(ans, dist[s][g] + dist[g][s])
    print(ans if ans != inf else -1)

# ------------------ Sample Input -------------------
4 4
1 2 5
2 3 10
3 1 15
4 3 20

4 7
1 2 10
2 3 30
1 4 15
3 4 25
3 4 20
4 3 20
4 3 30

# ----------------- Length of time ------------------
# 37分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc191/editorial
# ついにダイクストラのライブラリを用意しました。経路復元つき！
# スタート地点以外から出発するダイクストラにだいぶ慣れてきた
# 身体バランスに似てる

# ----------------- Category ------------------
#AtCoder
#全点からダイクストラする
#最短路問題
#最短経路問題
#ダイクストラ
#複数回ダイクストラ
#djikstra
#ABC-E
#水色diff