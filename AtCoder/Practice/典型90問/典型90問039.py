# 典型90問039 - Tree Distance
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_am
# Date: 2021/05/12

# ---------- Ideas ----------
# 一直線に繋がってるのが距離の合計が大きくなる
# 木に分岐が増えることで，距離の合計が小さくなっていく
# 一直線であれば，(n+1)C3 = (n-1)n(n+1)//6が距離の合計であり，ここから分岐で減った分(実績)を引いて答えが出せそう
# 1つの頂点から他の全ての頂点がくっついてる，というグラフが最も距離合計が小さい状況
# 一直線なら木の直径は頂点数と同じnになるが，分岐が増えることで木の直径が短くなる
# 木の直径が短くなった分，木の幹に実がついているような感じで，幹の横に頂点が生えてる
# この横に生えてる個数kを数える: k = 全部の頂点数 - 木の直径
# k個の実の実績を計算して，一直線距離合計から引いてあげればいい

# 上の議論はセンスはいいものの，厳密性を欠いていて，適当にやるとWAになっちゃう

# ------------------- Answer --------------------
#code:python
def bfs(G, s):
    dist = [-1] * n
    dist[s] = 0
    que = deque([s])

    while que:
        v = que.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    return dist

# n個の頂点が一直線だった場合の解 (任意の頂点ペアの距離の合計)
def total(n):
    return((n+1)*n*(n-1)//6)

#
def an(n):
    return(n*(n+1)//2)

from collections import deque, Counter
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

dist1 = bfs(G, 0)
start = dist1.index(max(dist1))
dist2 = bfs(G, start)
max_dist = max(dist2) + 1 # 木の直径
k = n-max_dist # 分岐した結果，木の幹にくっついている頂点の個数
print(total(n) - k * an(k))

# WAでした！！！！！！！！！
# ググったらO(N)解法出てきた。これでやってみよう
# この方法でやってみよう: https://codereview.stackexchange.com/questions/135915/sum-of-all-paths-between-all-pairs-of-nodes-in-a-tree
# ステップ1: 1本しか辺の出てない頂点sを探す
# ステップ2: ansに(sの寄与度)*(n-sの寄与度) をインクリメントする
# ステップ3: sから繋がっている唯一の頂点gについて，sの寄与度(count_vertex)をgに移す
# ステップ4: グラフからgとsを消す

from collections import deque, Counter
n = int(input())
G = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].add(b)
    G[b].add(a)

count_edge = [0]*n # 各頂点から出てる辺の数
single_vertex = deque([]) # 1辺しか繋がってない頂点の集合
for i in range(n):
    count_edge[i] = len(G[i])
    if len(G[i]) == 1:
        single_vertex.append(i)

ans = 0
count_vertex = [1]*n # 各頂点に統合された頂点の数 (寄与度)

while len(single_vertex) >= 2:
    # 1辺しか接してない頂点sを探す
    s = single_vertex.popleft()

    # sから繋がっている唯一の頂点g
    g = list(G[s])[0]

    # ansにインクリメント
    ans += count_vertex[s] * (n-count_vertex[s])

    # sのカウントをgに移す，統合する
    count_vertex[g] += count_vertex[s]

    # 頂点gからsが減った分の数を調整する。
    count_edge[g] -= 1

    # もしgからの辺の数が1になってたらsingle vertexに追加する
    if count_edge[g] == 1:
        single_vertex.append(g)

    # sとgの辺をグラフから消す
    G[s].remove(g)
    G[g].remove(s)
print(ans)

# ACした！！！！！！！！



# NetworkXにもあるけど，O(N^2)っぽくて遅い
import networkx as nx
n = int(input())
G = nx.Graph()
G.add_edges_from([tuple(map(int, input().split())) for _ in range(n-1)])
print(int(nx.algorithms.wiener.wiener_index(G)))

# ------------------ Sample Input -------------------
2
1 2

4
1 2
1 3
1 4

12
1 2
3 1
4 2
2 5
3 6
3 7
8 4
4 9
10 5
11 7
7 12

# ----------------- Length of time ------------------
# ググってググって2時間くらいかかった？

# -------------- Editorial / my impression -------------
# Wiener Indexと呼ばれるものらしい。化学の分野では重要らしい
# 無向グラフの任意の2点の距離の合計
# ググってACした解法と，E8くんの公式解法は同じだった。木DPらしい。
# 一般に「得点Aiをいくつか足した和で表される総得点Siが沢山あって、
# ありうる全ての場合についてSiを足し合わせたいときに、Aiが何回足されるかを考えるテクニック」
# これを主客転倒と呼ぶらしい

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#主客転倒
#木DP
#グラフ問題
#数え上げ
#wiener_index
#無向グラフ
#総当り
#典型90問