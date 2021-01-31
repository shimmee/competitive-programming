# ABC190C - Bowls and Dishes  /
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_c
# Date: 2021/01/30

# ---------- Ideas ----------
# bit全探索！


# ------------------- Answer --------------------
#code:python

n, m = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(m)]
K = int(input())
cd = [[int(i) for i in input().split()] for _ in range(K)]

ans = 0
import itertools
all_pattern = itertools.product([0, 1], repeat=K) # パターン=0の人はcに置く，1の人はdにおく
for pattern in all_pattern:
    flag = [False]*n
    cnt = 0
    for i in range(K):
        c, d = cd[i]
        if pattern[i] == 0:
            flag[c-1] = True
        else:
            flag[d-1] = True

    for j in range(m):
        a, b = ab[j]
        if flag[a-1] and flag[b-1]:
            cnt += 1
    ans = max(ans, cnt)
print(ans)


# ------------------ Sample Input -------------------
4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3


# ----------------- Length of time ------------------
# 本番で1発AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc190/editorial
# ぱぱっととけました

# ----------------- Category ------------------
#AtCoder
#ABC-C
#bit全探索