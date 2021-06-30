# ABC204
# URL:
# Date: 2021/06/06

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

from heapq import heappush, heappop
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b, c, d = map(int, input().split())
    if a == b: continue
    a -= 1
    b -= 1
    G[a].append([b, c, d])
    G[b].append([a, c, d])

s = 0
inf = float('INF')
dist = [inf] * n
dist[s] = 0

que = []
heappush(que, (0, s))

while que:
    w, a = heappop(que)
    if dist[a] < w:
        continue
    for b, c, d in G[a]:
        cost = inf
        for dt in range(-10, 10):
            p = int(d**0.5) - w + dt # 待ち時間
            if p+1 > 0:
                cost = min(cost, p + c + d//(p+1))
        cost = min(cost, c + d//(w+1)) # 何も待たない
        if dist[b] > dist[a] + cost: # 距離の更新
            dist[b] = dist[a] + cost
            heappush(que, (dist[b], b))

print(dist[n-1] if dist[n-1] != inf else -1)



# ------------------ Sample Input -------------------
2 1
1 2 2 3

2 3
1 2 2 3
1 2 2 1
1 1 1 1

4 2
1 2 3 4
3 4 5 6


6 9
1 1 0 0
1 3 1 2
1 5 2 3
5 2 16 5
2 6 1 10
3 4 3 4
3 5 3 10
5 6 1 100
4 2 0 110


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
