# 典型90問013 - Passing
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_m
# Date: 2021/05/10

# ---------- Ideas ----------
# 1からkまでの距離，Nからkまでの距離をそれぞれダイクストラで求める
# 2回ダイクストラする

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
        start頂点からgoal頂点までの経路復元を行う関数
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
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a - 1].append([b - 1, c])
    G[b - 1].append([a - 1, c])

model_from_0 = djikstra(n, G, 0)
model_from_n = djikstra(n, G, n-1)

dist_from_0 = model_from_0.run_djikstra()
dist_from_n = model_from_n.run_djikstra()

for k in range(n):
    print(dist_from_0[k] + dist_from_n[k])

# ------------------ Sample Input -------------------
7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3


# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# 反対からダイクストラするというアイデアは初めて得た
# とても学びの大きい問題
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/013.jpg

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#djikstra
#ダイクストラ
#最短経路問題
#2回ダイクストラする
