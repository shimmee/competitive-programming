# ABC159D - Banned K
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc159/tasks/abc159_d
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------


# ------------------- 方針 --------------------
# まず全部のぼーるを使ったときの場合の数を求める
# 各ボールの数字が取り除かれたときの処理を事前計算

# ------------------- 解答 --------------------
#code:python
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

from collections import Counter
n = int(input())
A = list(map(int, input().split()))

dict = Counter(A)
cnt = 0
for key, value in dict.items():
    if value >= 2:
        cnt += combinations_count(value, 2)

adjust = {}
for key, value in dict.items():
    remove = 0
    add = 0
    if value >= 2: remove = combinations_count(value, 2)
    if value-1 >= 2: add = combinations_count(value-1, 2)
    adjust[key] = -remove + add


for i in range(n):
    print(cnt + adjust[A[i]])

# TLEになった
# Nのループの中で階乗計算してた
# 事前計算に直してAC

# 解説: https://img.atcoder.jp/abc159/editorial.pdf
# 全部nC2なのでcombinationの関数なんて使わずにn*(n+1)//2で済む
# きれいな解答: https://atcoder.jp/contests/abc159/submissions/18928607

from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
s = sum(i * (i - 1) // 2 for i in c.values()) # 全部のぼーるを使ったときの場合の数を求める
for i in a:
    print(s - c[i] + 1)



# ------------------ 入力例 -------------------
5
1 1 2 1 2

4
1 2 3 4

5
3 3 3 3 3


8
1 2 1 4 2 1 4 1



# ----------------- 解答時間 ------------------
# 20分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc159/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#事前計算
#medium復習
#ABC-D