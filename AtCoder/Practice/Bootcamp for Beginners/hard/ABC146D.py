# ABC146D - Coloring Edges on Tree
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc146/tasks/abc146_d
# Date: 2021/01/31

# ---------- Ideas ----------
# 構築問題! ドミノに似てるね
# 使用する色の数の最小値Kは，最も多くの頂点と繋がっている頂点の辺の数
# 色はBFSで塗っていく: 辺の順番はどうするんだ？
# 入力された辺の順番で出力する必要があるので，入力の時点で順番をキープする


# ------------------- Answer --------------------
#code:python
n = int(input())
graph = []
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph.append([a-1, b-1])
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

K = max([len(i) for i in G])
print(K)

option = set([i for i in range(1, K+1)]) # 使える色の種類
used = [set() for _ in range(n)] # 各頂点における使用済み色を格納する集合
color = [] # 各辺を塗ったらこれ

for i in range(n-1): # 辺を順番に塗っていく
    a, b = graph[i]
    c = (option - (used[a] | used[b])).pop() # 頂点aとbから伸びる辺で使われてない色
    color.append(c)

    used[a].add(c) # 使われたことにする
    used[b].add(c)
for i in color:
    print(i)

# 2ケースTLE, 3ケースRE
# おそらくoptionの操作の部分がO(N^2)になってる
# BFSみたいに解くしかなさそう
# 入力の順番もGに入れる

# けんちょんさんより: 新たな頂点について、その隣接辺たちに色を塗ろうとするとき
# その隣接辺たちのうち、すでに色が塗られてしまっているのは一本だけ
# つまり親の色だけ避ければOK
# こちらを参考: https://zenn.dev/knk_kei/articles/abc-146-d-coloring-edges-on-tree

from collections import deque
n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a - 1].append([i, b - 1]) # 入力順もキープ
    G[b - 1].append([i, a - 1])

que = deque([])
que.append(0)
edge = [-1]*(n-1) # 各辺の色を塗るリスト
parent = [-1] * n # 親の色

while que:
    color = 1 # 現在使用可能な色
    a = que.popleft() # この子が親になる
    ng_color = parent[a] # 親の色は使えない
    for idx, b in G[a]: # idxは入力順
        if edge[idx] == -1: # まだ見てない辺のみ見ていく
            if color == ng_color: # 親と同じ色だったら次の色
                color += 1
            parent[b] = color
            edge[idx] = color
            color += 1
            que.append(b)

# 張っている辺の数がもっとも多い頂点の辺の数がK
K = max([len(i) for i in G])
print(K)
for i in edge:
    print(i)

# ------------------ Sample Input -------------------
3
1 2
2 3

8
1 2
2 3
2 4
2 5
4 7
5 6
6 8

6
1 2
1 3
1 4
1 5
1 6


# ----------------- Length of time ------------------
# 1.5時間 解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc146/editorial.pdf
# Kを求めるのは簡単に思いついた
# 入力順のまま各辺を実際に塗ると，塗った色を管理する必要がでてTLEになってしまった
# 根付き木として考えて「親と違う色を付ける必要がある」という考察に至れなかった。
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/04/26/172200
# 入力の順番をキープして出力するのが大変だった
# 色々学べる問題だった。復習したい



# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#彩色問題
#構築問題
#木
#辺彩色
#彩色数
#緑diff
#グラフ
#ABC-D
#BFS
#色に関する問題
#入力の順番をキープして出力