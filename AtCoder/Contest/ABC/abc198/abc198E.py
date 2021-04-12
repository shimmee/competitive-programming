# ABC198E - Unique Color
# URL: https://atcoder.jp/contests/abc198/tasks/abc198_e
# Date: 2021/04/11

# ---------- Ideas ----------
# BFSで行けそう？ -> 本番無理だった
# ある頂点までに見てきたすべての色を管理するとなると10**5頂点ぞれぞれにsetを持たなきゃいけなくて
# ABC146D - Coloring Edges on Treeと同じようなTLEになってしまう

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
c = list(map(int, input().split()))
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

used = {c[0]}
seen = [False]*n
seen[0] = True
que = deque([0])
ans = [0]

while que:
    v = que.popleft()
    for u in G[v]:
        if not seen[u]:
            if not c[u] in used:
                ans.append(u)
                used.add(c[u])
            seen[u] = True
            que.append(u)
print(ans)

# BFSでは解けなさそう
####################################
# DFSで解ける
# 行きがけに色をカウント、帰りがけに色をマイナスカウントするDFS
# らしいけど2時間ググってよくわからん
# Euler tour (オイラーツアー)という根付き木をDFSして行きがけと帰りがけのときに通った頂点順にリストを作るアルゴリズムを使えそう

def euler_tour(G, root=0):
    # dfsで根付き木の頂点からオイラーツアーを行う
    # Qiita: https://qiita.com/ophhdn/items/48710bfab29d1fdc4577
    # Atcoder: https://atcoder.jp/contests/abc198/submissions/21656391
    # wiki: https://en.wikipedia.org/wiki/Euler_tour_technique

    # 初めて頂点に訪れるとき: eulerに追加，stackにも戻してその頂点の子を見に行く
    # すでに訪問済みのとき: eulerに追加，stackに戻さず，次のstackの頂点を見る

    from collections import deque
    n = len(G) # 頂点数
    euler = [] # ツアーの結果を保存するリスト: 頂点がスタックされる時 (行きがけ)とスタックから出される時 (帰りがけ)にeulerにその頂点を入れる
    stack = deque([root])
    visited = [False] * n # 訪問済み頂点

    while stack:
        v = stack.pop()
        euler += [v]
        if visited[v]:
            continue
        stack += [v]

        for u in G[v]: # vから行ける頂点uに行く: uがvの子なら未訪問，uがvの親なら訪問済み
            if visited[u]: # 訪問済みのとき，uはvの親であるので，
                continue
            else: # 未訪問のとき，uはvの子なのでstackを積んでさらに深く見に行く
                stack += [u]
        visited[v] = True
    return euler

n = int(input())
C = list(map(int, input().split()))
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

path = euler_tour(G, root=0)
used = [0]*(max(C) + 1)
ans = []
seen = [False] * n

for v in path:
    if seen[v]:
        used[C[v]] -= 1
    else:
        seen[v] = True
        if used[C[v]] == 0:
            ans.append(v+1)
        used[C[v]] += 1
print(*sorted(ans), sep = '\n')

# ------------------ Sample Input -------------------
10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10

6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5


# ----------------- Length of time ------------------
# 解説AC3時間。。。

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc198/editorial
# euler tour後の探索の際，usedをsetで管理しようとしたらWAになった謎
# DFSが苦手なのでこれは本番解けませんでした
# スタックを使うDFSはなんとか使えそう...?
# この回答がとても参考になった: https://atcoder.jp/contests/abc198/submissions/21656391
# これも: https://r-n-note.blogspot.com/2020/07/blog-post.html

# ----------------- Category ------------------
#AtCoder
#木に色を塗る問題
#頂点に色を塗る問題
#オイラーツアー
#euler_tour
#根付き木
#スタック
#深さ優先探索
#DFS
#coloring_tree
#木構造
#木問題





#
# from collections import deque, Counter
#
# n = int(input())
# C = list(map(int, input().split()))
# G = [[] for _ in range(n)]
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     G[a - 1].append(b - 1)
#     G[b - 1].append(a - 1)
#
# # stackを初期化
# stack = deque([0])
# used = {C[0]}
# seen = [True] + [False] * (n - 1)
# ans = [1]
#
# while stack:
#     v = stack[-1]
#     if not G[v]:
#         stack.pop()
#         if C[v] in used:
#             used.remove(C[v])
#     else:
#         u = G[v].pop()
#         if not seen[u]:
#             stack.append(u)
#             seen[u] = True
#
#             if not C[u] in used:
#                 ans.append(u + 1)
#                 used.add(C[u])
#
# print(*sorted(ans), sep='\n')