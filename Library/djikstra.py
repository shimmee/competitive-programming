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

    def route_restoration(self, goal):
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