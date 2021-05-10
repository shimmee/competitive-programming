# 典型90問026
# URL: https://github.com/E869120/kyopro_educational_90/blob/main/sample/026.txt
# Date: 2021/04/27

# ---------- Ideas ----------
# オイラーツアー貼り付ければなんとかなりそう

# ------------------- Answer --------------------
#code:python


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
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

tour = euler_tour(G, 0)
seen = [False]*n
flag = True
red = []
for i in range(len(tour)):
    if len(red) == n//2:
        break

    if i < len(tour)-1 and tour[i] == tour[i+1]:
        red.append(tour[i]+1)
        flag = False
        continue
    if seen[tour[i]]: # 帰りがけに見かけたとき
        if flag:
            flag2 = True
            for v in G[tour[i]]:
                if v in red: flag2 = False
            if flag2:
                red.append(tour[i]+1)
                flag = False
        else:
            flag = True
    seen[tour[i]] = True

print(*(red[:(n//2)]))


# ------------------ Sample Input -------------------
6
1 2
2 3
3 4
4 5
3 6



6
1 3
2 4
3 5
2 5
3 6

6
1 2
2 3
3 4
3 5
3 6



7
3 7
1 3
2 4
3 5
2 5
3 6

4
1 2
2 3
2 4

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
