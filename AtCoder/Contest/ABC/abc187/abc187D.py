# ABC187D - Choose Me
# URL: https://atcoder.jp/contests/abc187/tasks/abc187_d
# Date: 2021/01/02

# ---------- Ideas ----------
# 貪欲に解く

# ------------------- Solution --------------------
# 差が一番大きいところから？
# 高橋が投票に行った街の高橋の票 - 行ってない街の青木の票>0
# 高橋が演説 -> 全員高橋に
# 演説しない -> 青木派だけが青木に投票

# 高橋は演説した街の総和を大きく，してない街の青木の票を小さくしたい

# ------------------- Answer --------------------
#code:python
import numpy as np
n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]
a = np.array([l[0] for l in ab])
t = np.array([l[1] for l in ab])
wa = np.array([l[0]+l[1] for l in ab])
sorter = np.lexsort((-t, a, -wa))

ab_sort = []
for name in zip(a[sorter], t[sorter], wa[sorter]):
    ab_sort.append(name)

from itertools import accumulate

# 高橋が演説した場合の高橋の票
cum_t = [0]+list(accumulate([l[0] + l[1] for l in ab_sort]))

# 演説なしの場合の青木の票
cum_a = [0]+list(accumulate([l[0] for l in ab_sort]))

# 演説ありの青木の票
cum_a = [cum_a[-1] - i for i in cum_a]

for i in range(n+1):
    if cum_t[i] > cum_a[i]:
        print(i)
        exit()

# 9ケースWA 嘘解法




# https://atcoder.jp/contests/abc187/editorial/486
# 2*A+Bでソートする必要があった

n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    ab[i].append((2*ab[i][0]+ab[i][1]))
ab_sort =  sorted(ab, key=lambda x: x[2], reverse=True)

total = -sum([i[0] for i in ab_sort])
for i in range(n):
    total += ab_sort[i][2]
    if total > 0:
        print(i+1)
        exit()



# 自分のもともとの解法も2*A+BでソートすればAC

n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    ab[i].append((2*ab[i][0]+ab[i][1]))
ab_sort = sorted(ab, key=lambda x: x[2], reverse=True)

from itertools import accumulate

# 高橋が演説した場合の高橋の票
cum_t = [0]+list(accumulate([l[0] + l[1] for l in ab_sort]))

# 演説なしの場合の青木の票
cum_a = [0]+list(accumulate([l[0] for l in ab_sort]))

# 演説ありの青木の票
cum_a = [cum_a[-1] - i for i in cum_a]

for i in range(n+1):
    if cum_t[i] > cum_a[i]:
        print(i)
        exit()




# ------------------ Sample Input -------------------
4
2 1
2 2
5 1
1 3

5
2 1
2 1
2 1
2 1
2 1

1
273 691

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------

# 事前の考察が足りないまま進めてしまって，ソートするキーが不明確なまま手探りでやった結果，1時間以上解いたのにWA
# 考察は時間がかかってもいいからおこなうべき

# ----------------- Category ------------------
#AtCoder
#ABC187
#ABC-D
#AC_with_editorial #解説AC
#貪欲法
#greedy
#wanna_review
#復習したい
