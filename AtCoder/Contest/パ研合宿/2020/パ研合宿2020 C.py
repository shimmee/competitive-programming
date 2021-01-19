# パ研合宿2020 C - 皆勤賞
# URL: https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_c
# Date: 2021/01/05

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# リストに全部ぶち込んでCounter
# nとvalueが同じ人は皆勤賞でインクリメント

# ------------------- Answer --------------------
#code:python
n = int(input())
l = []
for _ in range(n):
    k = int(input())
    S = input().split()
    l.append(S)

l = [item for sublist in l for item in sublist]
from collections import Counter
ans = 0
for key, value in Counter(l).items():
    if value == n:
        ans += 1
print(ans)


# ------------------ Sample Input -------------------
2
2
kaage penguinman
2
penguinman rho

3
3
a b c
2
a ba
3
a ba abc

# ----------------- Length of time ------------------
# 5分くらい？

# -------------- Editorial / my impression -------------
# 解説通り

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#パ研合宿2020
