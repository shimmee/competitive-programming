# 典型90問043 - Maze Challenge with Lack of Sleep
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_aq
# Date: 2021/05/17

# ---------- Ideas ----------
# 方向が変わる = (x1, y1)から(X, Y)への方向と逆方向の(x2, y2)が移動可能マスなのであれば，
# (X, Y)へは曲がらずに来られるはず。
# 直前の座標だけではなくて，2つ前の座標も含めてBFSする

# ------------------- Answer --------------------
#code:python
from collections import deque
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
G = [input() for _ in range(h)]

inf = float('INF')
dydx = [[0, 1], [1, 0], [0, -1], [-1, 0]]
turn = [[inf for _ in range(w)] for _ in range(h)]
turn[sy][sx] = 0
pre2 = [[set() for _ in range(w)] for _ in range(h)]
que = deque([])
que.append([sy, sx, -1, -1])  # 1つ前の座標と2つ前の座標

while que:
    y1, x1, y2, x2 = que.popleft()
    for dy, dx in dydx:
        Y = y1 + dy
        X = x1 + dx
        if 0 <= Y < h and 0 <= X < w and G[Y][X] == '.':
            # if Y == 0 and X == 3: print(Y, X, y1, x1, y2, x2)
            if y2 != -1 and x2 != -1 and turn[y1][x1] < turn[y2][x2]:
                continue

            if (not (y1, x1, y2, x2) in pre2[Y][X]) and [Y, X] != [y2, x2]:
                que.append([Y, X, y1, x1])
                pre2[Y][X].add((y1, x1, y2, x2))
                # 2つ前のマスからxかyのどちらかの座標が異なっていると 方向が変わってる
                if y2 == x2 == -1:  # スタート地点の例外処理
                    turn[Y][X] = min(turn[Y][X], turn[y1][x1])
                elif Y != y2 and X != x2:  # 曲がってる条件
                    turn[Y][X] = min(turn[Y][X], turn[y1][x1] + 1)
                else:  # 曲がってなければ直前と同じ
                    turn[Y][X] = min(turn[Y][X], turn[y1][x1])

print(turn[gy][gx])

# ヒントもらった: https://stackoverflow.com/questions/32675862/moving-in-grid-with-minimum-direction-change
# 各マスをグラフの頂点と見立てて，頂点の中にmini頂点として上下，左右の2つもつ
# 隣り合うマス同士に重み付きの辺を貼る: マス同士が上下同士のmini頂点で繋げられるなら重み0, 上下と左右の組み合わせなら重み1
# これの重み付き無向グラフを作ったらダイクストラでやる


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

dydx = [[0, 1], [1, 0], [0, -1], [-1, 0]]
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
grid = [input() for _ in range(h)]

G = [[] for _ in range(h*w*2)]
for y in range(h):
    for x in range(w):
        if grid[y][x] == '#': continue
        id_from_h = (w * y + x) * 2
        id_from_v = (w * y + x) * 2 + 1

        for dy, dx in dydx:
            Y = y + dy
            X = x + dx
            if 0 <= Y < h and 0 <= X < w and grid[Y][X] == '.':
                id_to_h = (w * Y + X) * 2
                id_to_v = (w * Y + X) * 2 + 1

                # id_from_hから左右に進む: 隣接マスのh頂点には重み0，v頂点には重み1で到達
                if [dy, dx] in [[0, 1], [0, -1]]:
                    G[id_from_h].append([id_to_h, 0])
                    G[id_from_h].append([id_to_v, 1])
                else:
                    G[id_from_v].append([id_to_h, 1])
                    G[id_from_v].append([id_to_v, 0])

print(0)
sid_h = (w * sy + sx) * 2
sid_v = (w * sy + sx) * 2 + 1
model_h = djikstra(h*w*2, G, sid_h)
model_v = djikstra(h*w*2, G, sid_v)
res_h = model_h.run_djikstra()
res_v = model_v.run_djikstra()

gid_h = (w * gy + gx) * 2
gid_v = (w * gy + gx) * 2 + 1

print(min([res_h[gid_h], res_h[gid_v], res_v[gid_h], res_v[gid_v]]))

# Pythonではダイクストラ間に合わないやつでした。
# というかグラフ作成する時点でTLEになってた。
# 解説みたら01-BFSというアルゴリズムが必要らしい
# 01-BFS: 辺のコストが0か1の場合のアルゴリズムでO(H+W)で解ける
#

# 01-BFS
from collections import deque
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
G = [input() for _ in range(h)]

inf = float('INF')
dydx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 各マスにおいて4方向それぞれの曲がった回数
turn = [[[inf]*4 for _ in range(w)] for _ in range(h)]
turn[sy][sx] = [0]*4
que = deque([])
for i in range(4):
    que.append([sy, sx, i])

while que:
    y, x, k = que.popleft() # 現在(y, x)にいてk方向を向いている

    dy, dx = dydx[k]
    Y = y + dy
    X = x + dx
    for i in range(4): # 到着マス(y, x)での向き
        if 0 <= Y < h and 0 <= X < w and G[Y][X] == '.' and turn[Y][X][i] == inf:
            if i == k: # 向きが同じときは重み0で先頭にキュー加える
                turn[Y][X][i] = turn[y][x][k]
                que.appendleft([Y, X, i])
            else: # 向きが異なるときは重み1で末尾にキュー加える
                turn[Y][X][i] = turn[y][x][k] + 1
                que.append([Y, X, i])

print(min(turn[gy][gx]))


# これだと3WAになります。なにがだめなのでしょう？
# 答え: https://twitter.com/marroncastle917/status/1394819429523857412


from collections import deque
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
G = [input() for _ in range(h)]

inf = float('INF')
dydx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 各マスにおいて2方向それぞれの曲がった回数
turn = [[[inf]*4 for _ in range(w)] for _ in range(h)]
turn[sy][sx] = [0]*4
que = deque([])
for i in range(4):
    que.append([sy, sx, i])

while que:
    y, x, k = que.popleft() # 現在(y, x)にいてk方向を向いている
    cost = turn[y][x][k]

    # マスの中で方向転換
    for i in range(4):
        if turn[y][x][i] < cost + 1: continue
        turn[y][x][i] = min(turn[y][x][i], cost+1)
        que.append([y, x, i])

    # 今向いてる方向に1マス進む
    dy, dx = dydx[k]
    Y = y + dy
    X = x + dx
    if 0 <= Y < h and 0 <= X < w and G[Y][X] == '.' and turn[Y][X][k] == inf:
        turn[Y][X][k] = turn[y][x][k]
        que.appendleft([Y, X, k])

print(min(turn[gy][gx]))


# ------------------ Sample Input ------------------



3 3
1 1
3 3
..#
#.#
#..

6 6
1 1
6 6
..#.#.
#.....
..#.#.
......
.###.#
......

4 4
1 1
4 4
...#
....
..#.
....



3 3
2 1
2 3
#.#
...
#.#


4 6
2 1
1 5
...#..
.#.##.
.#....
...##.


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#BFS
#幅優先探索
#grid
#gridを曲がる回数
#01-BFS
#幅優先探索
#最短路問題
#最短距離
#BFS