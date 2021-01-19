# ABC020C - 壁抜け
# URL: https://atcoder.jp/contests/abc020/tasks/abc020_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
# 境界を見つける問題なので二分探索！！
# 重みのある単一始点の最短経路問題なのでダイクストラ！
# グリッドが最大で10*10なので，ダイクストラで余裕でいける
# 今回の入力が二次元なのに対し，普通のダイクストラは1次元の頂点を扱うので厄介

# ------------------- 方針 --------------------
# 入力フィールドからスタートとゴールの座標を探して，白マスに置き換える
# 入力フィールドの各マスにidを降って，そのidを頂点のidとする
# 黒マスのcostを引数としたダイクストラ関数を作成する
# 関数の中身では，まずフィールドを隣接リストに変換する
# 隣接リストをつかってダイクストラを行い，ゴールまでの最短距離を計算
# 出力して，二分探索でcostがT以下になる最大のcostを探す

# ------------------- 解答 --------------------
#code:python
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
H, W, T = map(int, input().split())
field = [input() for _ in range(H)]
n = H*W # グラフの頂点の個数

# 一次元配列を二次元に変換する関数: 頂点のidとする
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]
field_id = convert_1d_to_2d([i for i in range(H*W)], W)

# スタートとゴールの座標を探して，白マスに変換
for y in range(H):
    for x in range(W):
        if field[y][x] == 'S':
            s = field_id[y][x]
            field[y] =  field[y].replace('S', '.')
        if field[y][x] == 'G':
            g = field_id[y][x]
            field[y] = field[y].replace('G', '.')

def dijkstra(cost):
    # グラフを隣接リストに変換
    G = [[] for _ in range(n)]
    for y in range(H):
        for x in range(W):
            for dy, dx in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < H and 0 <= X < W:
                    if field[Y][X] == '.':
                        G[field_id[y][x]].append([field_id[Y][X], 1])
                    if field[Y][X] == '#':
                        G[field_id[y][x]].append([field_id[Y][X], cost])

    # 始点から各頂点までの最短距離をinfで初期化
    inf = float('INF')
    dist = [inf]*n
    dist[s] = 0 # 始点の設定

    # 各頂点が使用済みかどうかのリスト: すでに最短路が求められていることが確定している頂点の集合S
    used = [False]*n

    for _ in range(n):
        # ステップ2: 使用済みでない頂点のうちdistが最小の頂点を探す
        min_dist = inf
        min_v = -1
        for v in range(n):
            if (not used[v]) and dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v

        # もしそのような頂点が見つからなければ終了
        if min_v == -1: break

        # min_vを使用済みとする
        used[min_v] = True

        # ステップ3: 頂点vの推移先を全て巡る
        for ew in G[min_v]:
            e = ew[0]  # 行き先
            w = ew[1]  # 重み
            if dist[e] > dist[min_v]+ w:
                dist[e] = dist[min_v] + w
    return dist[g]

# 二分探索
ok = 0 # 絶対にOKの数
ng = 10**10 # 絶対にngの数
while (abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    dist = dijkstra(mid) # costがmidにおける最短距離
    if T >= dist: # 最短距離がT以下ならOK
        ok = mid
    else: ng = mid
print(ok)

# ------------------ 入力例 -------------------
2 3 10
S##
.#G

3 4 7
S##G
.##.
..#.

4 4 1000000000
S###
####
####
###G

# ----------------- 解答時間 ------------------
# 50分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc020
# 解説通り！
# 二分探索とダイクストラの教育的な問題！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#ダイクストラ法
#dijkstra
#二分探索
