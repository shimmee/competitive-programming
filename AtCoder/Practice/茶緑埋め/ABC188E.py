# ABC188E - Peddler
# URL: https://atcoder.jp/contests/abc188/tasks/abc188_e
# Date: 2021/02/26

# ---------- Ideas ----------
# x<yなのでサイクルはない!: 木になっている
# 各木の根がわかれば，そこからBFSで現在の金額[minとmax]を保持しながら推移すればいける
# 同じ場所で買って同じ場所で売れないことに注意
# これで解いてみたら，2つの根からつながっている頂点を2回目に訪れるのが難しそうなので，断念

# ------------------- Solution --------------------
# 全探索? (のちにDPとわかる)で解いてみる
# min_cost[i]: 各頂点iにたどり着くまでに購入可能な金の最小価格
# 全頂点を走査して，2重目のループで頂点iから行ける頂点vに行く
# min_cost[i]で金を買っていたとして，頂点vで売ってみてansを更新
# 頂点vにおける価格が最小価格になる可能性があるもの: A[v], min_cost[i], min_cost[v]，これらで更新

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n, m = map(int, input().split())
inf = float('INF')
A = list(map(int, input().split()))
G = [[] for _ in range(n)]
G2 = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)
    G2[y - 1].append(x - 1)

# G2が空の頂点のみ根になりうる
root = []
for i in range(n):
    if G2[i] == []:
        root.append(i)

# BFSで探索する
ans = -10**20
flag = [[False, inf]]*n
for i in range(n):
    que = deque([[i, A[i]]])
    while que:
        v, min_c = que.popleft()
        for u in G[v]:
            if flag[u][0]: continue # 訪問済みならスキップ
            ans = max(ans, A[u] - min_c) # 今までの最小価格で買ってたとして，ここで売る
            flag[u] = [True, min(min_c, A[u])] # ここが最小価格なら更新
            que.append([u, flag[u][1]])

print(ans)

# 半分WA!!!! テストケースをカンニングする。
# 一度訪問した場所に訪問しないことになっているせいで，損をしている。
# 一度探索した場所をBFSでもう一度探索するのは無駄なので，単純に全探索するのはどうか


n, m = map(int, input().split())
inf = float('INF')
A = list(map(int, input().split()))
G = [[] for _ in range(n)]
G2 = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)

min_cost = [inf]*n
ans = -10**20
for i in range(n):
    if min_cost[i] == inf: # 根のとき
        min_cost[i] = A[i]
    for v in G[i]:
        ans = max(ans, A[v] - min_cost[i])
        min_cost[v] = min(min_cost[v], min(min_cost[i], A[v]))
print(ans)

# AC!!!!
# よくみたらDPで解いてた。全探索だと思ってたらDPだった。



# ------------------ Sample Input -------------------
7 16
223444244 779658349 154763608 113983849 914282513 166910857 594690778
2 3
1 3
5 7
3 7
3 4
1 7
4 7
2 4
1 6
3 5
4 6
2 5
1 4
3 6
4 5
2 6

7 6
293032430 121850839 87623490 55685765 849970388 794174905 5921452
1 6
2 7
2 5
3 6
6 7
4 5

3 1
1 100 1
2 3

5 5
13 8 3 15 18
2 4
1 2
4 5
2 3
1 3

4 3
2 3 1 5
2 4
1 2
1 3


# ----------------- Length of time ------------------
# WAだしまくって，テストケースをカンニングして1時間でAC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc188/editorial
# 気づいたらDPで解いてた
# 計算量がよくわからなかったんだけども，O(N+M)らしい。
# BFSでも解けるっぽい
# 最初嘘解法にハマって辛かったけど，とても面白かった。
#

# ----------------- Category ------------------
#AtCoder
#配るDP
#グラフ
#動的最適化
#O(N+M)
#ヒントAC
#全頂点走査してそこから行ける頂点も探索
