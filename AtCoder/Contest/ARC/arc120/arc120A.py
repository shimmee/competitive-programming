# ARC120A
# URL:
# Date: 2021/05/23

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
cum_sum = list(accumulate(accumulate(a)))
cum_max = list(accumulate(a, max))
for i in range(n):
    print(cum_sum[i] + cum_max[i] * (i+1))





cum_max = [0]
for i in range(n):
    ai = cum_sum[i]
    cum_max.append(max(ai, cum_max[-1]))

cum_sum = [0]
cum_max = [0]
for i in range(n):
    ai = a[i]
    cum_max.append(max(ai, cum_max[-1]))
    cum_sum.append(ai)



cum = list(accumulate(max_cum))
cum = list(accumulate(cum))

for i in range(n):
    cum



import heapq
n = int(input())
a = list(map(int, input().split()))

# 累積和
from itertools import accumulate
cum = [0] + list(accumulate(a))

que = []
que = list(map(lambda x: x * (-1), que))  # 各要素を-1倍: 最大値を取り出すために必要な処理
heapq.heapify(que)  # リストのヒープ化

for i in range(n):
    ai = a[i]
    heapq.heappush(que, -ai)
    max_a = heapq.heappop(a) * (-1) # 最大値を取り出す


# ------------------ Sample Input -------------------
3
1 2 3


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい


