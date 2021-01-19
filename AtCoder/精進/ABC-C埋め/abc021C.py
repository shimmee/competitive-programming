# ABC021C - 正直者の高橋くん
# URL: https://atcoder.jp/contests/abc021/tasks/abc021_c
# 日付: 2020/12/16

# ---------- 思ったこと / 気づいたこと ----------
# 最短経路を求めながら，同時に経路の個数を求める必要がある
# ダイクストラで書いてみたらダメだったので，幅優先探索に切り替え
# けんちょんさんの方法を参考に: https://drken1215.hatenablog.com/entry/2018/02/09/003200

# ------------------- 方針 --------------------
# 各頂点への最短経路の個数をカウントするリストcntを作る
# 以下のようにBFSに2つの点を加える
# 1. 現在の頂点から訪れる次の頂点がすでに訪問済みのとき，
# dist[次] == dist[今] + 1 なら，それは新たな最短ルートということになるので，cnt[次]にcnt[今]をインクリメント
# 2. 現在の頂点から訪れる次の頂点が初めての訪問先の場合
# 次の頂点に行くまでの最短経路の個数は今の頂点と同じ個数なので，cnt[次]=cnt[今]


# ------------------- 解答 --------------------
#code:python
from collections import deque
mod = 10**9+7
# 入力
n = int(input())
s, g = map(int, input().split())
m = int(input())
G = [[] for _ in range(n+1)]

# グラフは隣接リストで行き先と重みをセットに格納する
for i in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

# dist(始点から各頂点までの距離)とque(回るべき頂点のリスト)を用意
dist = [-1]*(n+1) # −1だったら訪れていないというフラッグにもなる
que = deque([])
cnt = [0]*(n+1)

# スタート地点sのdistとqueを初期化
dist[s] = 0
que.append(s)
cnt[s] = 1

while que:
    from_ = que.popleft()
    for to_ in G[from_]: # 街from_から辿り着ける街to_をループで回す
        if dist[to_] != -1: # もしすでに訪れたことがある場所で
            if dist[to_] == dist[from_] + 1: # かつfrom_から1歩で来れるのであれば，新しいルートになるので，経路個数をインクリメント
                cnt[to_] += cnt[from_]
        else: # 初めて訪れる場所なら
            dist[to_] = dist[from_] + 1 #
            que.append(to_)
            cnt[to_] = cnt[from_] # 初めて訪れるときは，出発街までの経路数と同じ
print(cnt[g] % mod)

# ------------------ 入力例 -------------------

7
1 5
9
1 2
1 3
1 4
2 5
3 5
4 5
3 4
5 6
6 7

7
1 7
8
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6

7
1 7
9
1 2
1 3
4 2
4 3
4 5
4 6
7 5
7 6
4 7

# ----------------- 解答時間 ------------------
# 2時間くらい?

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc021
# 最初に最短経路を求めてから，次に経路数を求める方法が解説で挙げられている

# ----------------- カテゴリ ------------------
#AtCoder #abc
#復習したい
#幅優先探索
#最短経路の個数
#BFS




# 最初に書いたダイクストラ
# ダイクストラで経路数も求めるやつ: https://qiita.com/ta-ka/items/a023a11efe17ab097433
# mod = 10**9+7
# # 入力
# n = int(input())
# s, g = map(int, input().split())
# s, g = s-1, g-1
# m = int(input())
# G = [[] for _ in range(n)]
#
# # グラフは隣接リストで行き先と重みをセットに格納する
# for i in range(m):
#     x, y = map(int, input().split())
#     G[x - 1].append([y - 1, 1])
#     G[y - 1].append([x - 1, 1])
#
# # 始点から各頂点までの最短距離をinfで初期化
# inf = float('INF')
# dist = [inf]*n
# dist[s] = s # 始点の設定
#
# # 各頂点が使用済みかどうかのリスト: すでに最短路が求められていることが確定している頂点の集合S
# used = [False]*n
# cnt = [0]*n
# cnt[0] = 1
#
# for _ in range(n):
#     # ステップ2: 使用済みでない頂点のうちdistが最小の頂点を探す
#     min_dist = inf
#     min_v = -1
#     for v in range(n):
#         if (not used[v]) and dist[v] < min_dist:
#             min_dist = dist[v]
#             min_v = v
#
#     # もしそのような頂点が見つからなければ終了
#     if min_v == -1: break
#
#     # min_vを使用済みとする
#     used[min_v] = True
#
#     # ステップ3: 頂点min_vの推移先eを全て巡る
#     for ew in G[min_v]:
#         e = ew[0]  # 行き先
#         w = ew[1]  # 重み
#         if dist[e] > dist[min_v]+ w:
#             dist[e] = dist[min_v] + w
#             cnt[e] = cnt[min_v] # コストが更新された場合は，直前の頂点への最短経路数で上書き
#         elif dist[e] == dist[min_v] + w:
#             cnt[e] += cnt[min_v]  # コストが一致する場合はこれまでの最短経路数を足し合わせ
#             cnt[e] %= mod
# print(cnt[g]%mod)
#
# # WAが出た
