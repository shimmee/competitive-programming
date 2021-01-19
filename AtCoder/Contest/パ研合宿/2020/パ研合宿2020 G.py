# パ研合宿2020 G - 同意書
# URL: https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_g
# Date: 2021/01/05

# ---------- Ideas ----------
# bit全探索

# ------------------- Solution --------------------
# n=14なので全パターン試す
# 各パターンにおいて，m個の発言に矛盾しないかflagで確認
# 矛盾しなければmaxを保存

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
lrx = [[int(i) for i in input().split()] for _ in range(m)]

ans = -1
import itertools
all_pattern = itertools.product([0, 1], repeat=n)
for pattern in all_pattern:
    flag = True
    for l,r,x in lrx:
        if sum(list(pattern)[l-1:r]) != x:
            flag = False
    if flag:
        ans = max(ans, sum(pattern))
print(ans)

# ------------------ Sample Input -------------------
3 2
1 2 1
1 1 0

4 2
1 3 0
1 2 1

5 2
1 3 2
3 4 2


# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#パ研合宿2020
#bit全探索