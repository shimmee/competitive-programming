# ABC022C - Blue Bird
# URL: https://atcoder.jp/contests/abc022/tasks/abc022_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 高橋君の家Aと隣接した家Bから出発すると考えて，AとBをつなぐ道以外を使ってBからAに行く最短距離＋AとBをつなぐ道の距離
# これが最短になるような隣接家を探す
# ダイクストラを使う

# ------------------- 解答 --------------------
#code:python
from heapq import heappush, heappop
n, m = map(int, input().split())
G = [[] for _ in range(n)]

# グラフは隣接リストで行き先と重みをセットに格納する
for i in range(m):
    a, b, w = map(int, input().split())
    G[a-1].append([b-1, w])
    G[b-1].append([a-1, w])

# 自分の家(頂点0)から行ける範囲の家のリスト
direct_house = G[0]

inf = float('INF')
ans = inf

# 他人の家(頂点=house)からスタートして自分の家(頂点=0)を目指す
for house, weight in direct_house:
     # 始点から各頂点までの最短距離をinfで初期化
    dist = [inf]*n
    dist[house] = 0 # 始点の設定

    que = []  # ヒープに入れる空のリスト
    heappush(que, (0, house))

    while que:
        c, v = heappop(que)
        if dist[v] < c:  #
            continue
        for e, w in G[v]:
            if (v == 0 and e == house) or (v == house and e == 0): continue # houseから自分の家の往復は使えない
            if dist[e] > dist[v] + w:  # 距離の更新
                dist[e] = dist[v] + w
                heappush(que, (dist[e], e))

    ans = min(ans, dist[0] + weight)

if ans == inf:
    print(-1)
else:
    print(ans)

# 色んな工夫したけどTLE!!!
# 1時間頑張ったけどギブアップ！
# 自分が解いた方法，計算オーダー的に無理だった。
# 解説: https://www.slideshare.net/chokudai/abc022
# アイデア1: 高橋くんの家と隣接してる辺を全て取り除く
# アイデア2: 隣接の家Xから別の隣接の家Yへの最短ルートを求めて，高橋家からXとYへの距離を足してあげれば，高橋家からグルっと回った経路が出る
# アイデア3: XとYの組み合わせを全通りダイクストラしてたら無駄があまりにも多いので，もう全点対の距離をワーシャルフロイドでもとめる=O(N^3)


n, m = map(int, input().split())
G = [[] for _ in range(n)]
T = [] # 高橋の家と隣接する家を格納するリスト

# ワーシャルフロイド: 全点対間最短経路問題
# dp[k][i][j]: 頂点0, 1, ..., k-1のみを中継頂点として通って良いとした場合の頂点iから頂点jへの最短距離
# kをin-placeに表現すれば，二次元配列で十分
inf = float('INF')
dp = [[inf for _ in range(n)] for _ in range(n)]

# dpの各要素がaからbへの重みを表すので，入力の有向グラフを初期状態として埋め込む
for _ in range(m):
    a, b, w = map(int, input().split())
    if a == 1: # 高橋の家と別の家をつなぐ道だったら，Tに保存
        T.append([b-1, w])
    else: # 高橋の家と隣接してる道以外はGに保存
        dp[a - 1][b - 1] = w
        dp[b - 1][a - 1] = w

# スタートとゴールが同じ場合(i=jのとき)は距離がゼロ
for i in range(n):
    dp[i][i] = 0

# 新たに頂点kを使用しない場合: dp[k][i][j]
# 新たに頂点kを使用する場合: dp[k][i][k] + dp[k][k][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


# 高橋の家と隣接する家を2組選んで，距離を測定
ans = inf
for i in range(len(T)-1):
    for j in range(i+1, len(T)):
        vi = T[i][0]
        vj = T[j][0]

        wi = T[i][1]
        wj = T[j][1]

        dist = dp[vi][vj] + wi + wj
        ans = min(ans, dist)
if ans == inf:
    print(-1)
else:
    print(ans)


# ------------------ 入力例 -------------------
5 7
1 2 2
1 4 1
2 3 7
1 5 12
3 5 2
2 5 3
3 4 5

5 4
1 2 1
1 3 1
1 4 1
1 5 1


10 12
1 4 3
1 9 1
2 5 4
2 6 1
3 7 5
3 10 9
4 7 2
5 6 6
5 8 5
6 8 3
7 9 5
8 10 8

# ----------------- 解答時間 ------------------
# 1時間かけてTLE: 解き方自体は間違ってなかったけど，ダイクストラじゃ無理だった
# 解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc022
# ダイクストラで解いてしまい，無駄な計算が多かった分TLEになってしまった
# 初めてのワーシャルフロイド解けなかった悔しい
# 同じ場所を通らないようにある辺を除いたグラフを考える，というのは常套手段なのかもしれない

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#全点対間最短経路問題
#ワーシャルフロイド法

