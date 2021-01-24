# 全国統一プログラミング王決定戦予選 C - Different Strokes
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c
# Date: 2021/01/23

# ---------- Ideas ----------
# ABC187D - Choose Meと同じだ！！！！！！！！
# ソートして上から食べていく。
# 何でソートするかが一番重要
# 「高橋が食べた時の高橋と青木の差」「青木が食べたときの高橋と青木の差」の2つの差が大きいものから食べたい
# これはまさにa+b

# ------------------- Solution --------------------
# 得点の差が開くようにお互い食べる
# a+bでソートして，お互い高い順に食べていく

# ------------------- Answer --------------------
#code:python
from collections import deque
n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b, a+b])
ab = deque(sorted(ab, key=lambda x: x[2], reverse=True))

taka = 0
aoki = 0
for j in range(n):
    a,b,c = ab.popleft()
    if j % 2 == 0: # 高橋のターン
        taka += a
    else:
        aoki += b
print(taka-aoki)

# 整理整頓する: a+bのコラムはつくらなくても大丈夫
n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]
ab = sorted(ab, key=lambda x: x[0]+x[1], reverse=True)

taka, aoki = 0, 0
for i in range(n):
    if i % 2 == 0: # 高橋のターン
        taka += ab[i][0]
    else:
        aoki += ab[i][1]
print(taka-aoki)

# ------------------ Sample Input -------------------
3
10 10
20 20
30 30

3
20 10
20 20
20 30

6
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000


# ----------------- Length of time ------------------
# 25分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/nikkei2019-qual/editorial.pdf
# 解説通り解けた。
# 今回の解説も類題のABC187Dと全く同じ感じ。復習した甲斐があった


# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ソート
#ゲーム
#貪欲
#greedy



# 高橋は2*a+b，青木はa+2*bでソートするべきだと勘違いして書いたコード
# from collections import deque
# n = int(input())
# ab = []
# for i in range(n):
#     a, b = map(int, input().split())
#     ab.append([i, a, b, 2*a+b, a+2*b])
# ab_taka = deque(sorted(ab, key=lambda x: x[3], reverse=True))
# ab_aoki = deque(sorted(ab, key=lambda x: x[4], reverse=True))
#
# taka = 0
# aoki = 0
# done = set([])
# for j in range(n):
#     if j % 2 == 0: # 高橋のターン
#         while True:
#             i,a,b,c,d = ab_taka.popleft()
#             if not i in done:
#                 taka += a
#                 done.add(i)
#                 break
#     else:
#         while True:
#             i,a,b,c,d = ab_taka.popleft()
#             if not i in done:
#                 aoki += b
#                 done.add(i)
#                 break
# print(taka-aoki)

# サンプル通ったが半分WA
