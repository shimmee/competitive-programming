# ABC199D -
# URL:
# Date: 2021/04/24

# ---------- Ideas ----------
# 連結成分のスタート地点: 3

# 1個しかつながってなくて，親が3 -> 2
# 1個しかつながってなくて，親が2 -> 2
# 1個しかつながってなくて，親が1 -> 2

# 2個つながってて親だけ判明，親が3 -> 2
# 2個つながってて親だけ判明，親が2 -> 2
# 2個つながってて親だけ判明，親が1 -> 2

# 2個つながってて両方判明，(1,3), (3,1) -> 2
# 2個つながってて両方判明，(2,3), (3,2) -> 1
# 2個つながってて両方判明，() -> 2

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

from collections import deque, Counter
n, m = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

cnt = [-1]*n
for s in range(n):
    if cnt[s] != -1:
        continue

    v_group = set([s])
    que = deque([s])
    while que:
        v = que.popleft()
        for u in G[v]:
            if u not :
                cnt[u] = min(cnt[v] - 1, )



    cnt[s] = 3

    while que:
        v = que.popleft()
        for u in G[v]:
            if cnt[u] == -1:
                cnt[u] = min(cnt[v] - 1, )


from scipy.special import comb
# a = comb(n, r)
a = comb(n, r, exact=True)


# 2色固定
cnt = 0
for i in range(1, 21):
    cnt += comb(20, i) * 2**i


# ------------------ Sample Input -------------------
3 3
1 2
2 3
3 1


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
