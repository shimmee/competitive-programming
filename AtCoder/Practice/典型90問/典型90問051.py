# 典型90問051 - Typical Shop（★5）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ay
# Date: 2021/05/27

# ---------- Ideas ----------
# N<=40だから半分全列挙！
# 半分にしてから組み合わせ全探索する
# それぞれのグループから選ぶ個数はループで決める: k


# ------------------- Answer --------------------
#code:python
from itertools import combinations
import bisect
n, k, p = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if k == 1:
    ans = 0
    for i in range(n):
        if A[i] <= p:
            ans += 1
    print(ans)
    exit()

A1 = A[:(n//2)]
A2 = A[(n//2):]

ans = 0
for j in range(k+1):
    k1 = j
    k2 = k-k1

    all_pattern1 = list(combinations(range(len(A1)), k1))
    all_pattern2 = list(combinations(range(len(A2)), k2))

    total1 = []
    for pattern in all_pattern1:
        cnt = 0
        for i in pattern:
            cnt += A1[i]
        total1.append(cnt)

    total2 = []
    for pattern in all_pattern2:
        cnt = 0
        for i in pattern:
            cnt += A2[i]
        total2.append(cnt)

    total1.sort()
    total2.sort()

    for a in total1:
        idx = bisect.bisect_right(total2, p-a)
        ans += idx
print(ans)





# ------------------ Sample Input -------------------
5 2 10
3 8 7 5 11

5 1 10
7 7 7 7 7

40 20 100
1 3 1 3 4 1 3 5 5 3 3 4 1 5 4 4 3 1 3 4 1 3 2 4 4 1 5 2 5 3 1 3 3 3 5 5 5 2 3 5
# ----------------- Length of time ------------------
# 30分くらい？

# -------------- Editorial / my impression -------------
# 今まで解いた半分全列挙はbit全探索だったけど，今回のは組み合わせ全探索だったから少し戸惑った

# ----------------- Category ------------------
#AtCoder
#組み合わせ全探索
#半分全列挙
#二分探索
#典型90問
