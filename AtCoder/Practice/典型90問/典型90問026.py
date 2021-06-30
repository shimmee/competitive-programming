# 典型90問026 - Independent Set on a Tree
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_z
# Date: 2021/05/13

# ---------- Ideas ----------
# 二部グラフの塗り方: https://qiita.com/hukuhuku11111a1/items/6b0c1a83d1434b7890e8
# 木は必ず二部グラフになる
# BFSの要領で，親と繋がる全ての子を探索していって，親と違う色を塗っていけばいい
# colorという配列を用意。0と1で色を塗る。
# colorという配列を用意。-1で初期化して，0と1で色を塗る。

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
m = n-1
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# BFSの要領で塗っていく: 親と違う色で塗るだけ
color = [-1 for i in range(n)]
color[0] = 1
que = deque([0])
while que:
    v = que.popleft()
    for u in G[v]:
        if color[u] == -1: # 塗られていないなら，別の色で塗る
            color[u] = 1 - color[v]
            que.append(u)

if sum(color) >= n//2:
    # 色1の方が多ければ色1が塗られてる頂点をn/2個出力
    ans = [i + 1 for i in range(n) if color[i] == 1]
    print(*ans[:n//2])
else:
    # 色0の方が多ければ色0が塗られてる頂点をn/2個出力
    ans = [i + 1 for i in range(n) if color[i] == 0]
    print(*ans[:n // 2])

# ------------------ Sample Input -------------------
4
1 2
2 3
2 4

6
1 3
2 4
3 5
2 5
3 6

# ----------------- Length of time ------------------
# 数日かかった？
# 解説AC

# -------------- Editorial / my impression -------------
# オイラーツアーで解こうと思ったら解けなかった苦い思い出がある
# BFSで簡単にかけてとても嬉しい。 本当にただのBFS。
# 二部グラフは初めてしった。
# 2色で交互に塗る = 二部グラフ
# 木は二部グラフだから必ず2色で塗れる
# 二部グラフの判定は今回書いたコードに「すでに塗られているのに親と同じだったら二部グラフじゃない」という判定をつければいいだけ
# 参考: https://qiita.com/hukuhuku11111a1/items/6b0c1a83d1434b7890e8
# とても楽しかった


# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#二部グラフ
#木
#グラフ
#木に色を塗る問題
#BFS
#幅優先探索
#典型90問



# 最初に書いた適当なオイラーツアー
# def euler_tour(G, root=0):
#     # dfsで根付き木の頂点からオイラーツアーを行う
#     # Qiita: https://qiita.com/ophhdn/items/48710bfab29d1fdc4577
#     # Atcoder: https://atcoder.jp/contests/abc198/submissions/21656391
#     # wiki: https://en.wikipedia.org/wiki/Euler_tour_technique
#
#     # 初めて頂点に訪れるとき: eulerに追加，stackにも戻してその頂点の子を見に行く
#     # すでに訪問済みのとき: eulerに追加，stackに戻さず，次のstackの頂点を見る
#
#     from collections import deque
#     n = len(G) # 頂点数
#     euler = [] # ツアーの結果を保存するリスト: 頂点がスタックされる時 (行きがけ)とスタックから出される時 (帰りがけ)にeulerにその頂点を入れる
#     stack = deque([root])
#     visited = [False] * n # 訪問済み頂点
#
#     while stack:
#         v = stack.pop()
#         euler += [v]
#         if visited[v]:
#             continue
#         stack += [v]
#
#         for u in G[v]: # vから行ける頂点uに行く: uがvの子なら未訪問，uがvの親なら訪問済み
#             if visited[u]: # 訪問済みのとき，uはvの親であるので，
#                 continue
#             else: # 未訪問のとき，uはvの子なのでstackを積んでさらに深く見に行く
#                 stack += [u]
#         visited[v] = True
#     return euler
#
#
# n = int(input())
# G = [[] for _ in range(n)]
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     G[a - 1].append(b - 1)
#     G[b - 1].append(a - 1)
#
# tour = euler_tour(G, 0)
# seen = [False]*n
# flag = True
# red = []
# for i in range(len(tour)):
#     if len(red) == n//2:
#         break
#
#     if i < len(tour)-1 and tour[i] == tour[i+1]:
#         red.append(tour[i]+1)
#         flag = False
#         continue
#     if seen[tour[i]]: # 帰りがけに見かけたとき
#         if flag:
#             flag2 = True
#             for v in G[tour[i]]:
#                 if v in red: flag2 = False
#             if flag2:
#                 red.append(tour[i]+1)
#                 flag = False
#         else:
#             flag = True
#     seen[tour[i]] = True
#
# print(*(red[:(n//2)]))