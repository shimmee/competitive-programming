# ARC037B - バウムテスト
# URL: https://atcoder.jp/contests/arc037/tasks/arc037_b
# Date: 2021/02/22

# ---------- Ideas ----------
# 連結成分の個数のうち，木でないものの個数
# 各頂点をスタートするループを書く: 訪問済みならcontinue
# BFSで頂点をめぐりながら，「訪問済みでかつ，親とは異なる」であったら閉路であるという判定
# 参考: https://www.geeksforgeeks.org/detect-cycle-in-an-undirected-graph-using-bfs/
# queにappendするときに親の情報を一緒に持たせる



# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

from collections import deque, Counter
que = deque([])
seen = [False]*n

ans = 0
for i in range(n):
    if seen[i]: continue
    else:
        flag = True # 閉路がないよのflag
        que.append([i, None])
        while que:
            a, parent = que.popleft()
            seen[a] = True
            for b in G[a]:
                if not seen[b]:
                    que.append([b, a]) # bの親をaとする
                    seen[b] = True
                elif seen[b] and b != parent: # 訪問済みでかつ親とは異なれば閉路
                    flag = False
        if flag: ans += 1
print(ans)


# ACしたけど
# 閉路検出はDFSの方がメジャーらしい
# 久しぶりにDFSをスクラッチで書いてみよう

import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

seen = [False]*n
def dfs(a, parent):
    global flag
    seen[a] = True
    for b in G[a]:
        if seen[b]:
            if parent != b:
                flag = False
            continue
        dfs(b, a)
ans = 0
for a in range(n):
    if seen[a]: continue
    flag = True
    dfs(a, None)
    if flag: ans += 1
print(ans)


# ------------------ Sample Input -------------------
8 7
1 2
2 3
2 4
5 6
6 7
6 8
7 8

10 10
1 2
1 5
2 3
3 4
4 5
2 7
3 6
6 7
6 9
8 10

5 5
1 2
1 3
2 3
1 4
4 5

# ----------------- Length of time ------------------
# 25分

# -------------- Editorial / my impression -------------
# 親の情報を持つというアイデアはググって得た。
# BFSをスクラッチで書いてACした。
# DFSでも書いてみたけど，再帰書いた分だけBFSより長くなった。global flagをしてなくてバグった。

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#閉路検出
#閉路の発見
#サイクルの検出
#木の判定
#木の判別
#グラフ
#tree