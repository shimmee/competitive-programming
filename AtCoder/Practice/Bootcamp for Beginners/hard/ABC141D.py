# ABC141D - Powerful Discount Tickets
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc141/tasks/abc141_d
# Date: 2021/01/12

# ---------- Ideas ----------
# M枚の割引券はつねに最高額のものに使ったほうがいい。貪欲に。
# 割引券は使い切ったほうがいい
# Aから最高額を取り出して1回割り引く -> Aに戻す -> 最高額を調べる，を繰り返す？

# ソートして最高額をdequeで取り出したとしても，それを入れるのに時間がかかる: O(MN)
# ヒープを使う？
# ヒープなら最大値の取り出しをO(1)，要素の追加をO(logN)で行えるので，トータルO(NlogN)でできるはず

# ------------------- Solution --------------------
# リストをヒープ化する
# m回のループを回し，aから最大値xを取り出す
# xを半額にしてyする
# yをaに戻す
# これを繰り返せば，最大の商品だけ常に割り引ける

# ------------------- Answer --------------------
#code:python

import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x:x*(-1), a)) #各要素を-1倍: 最大値を取り出すために必要な処理
heapq.heapify(a) # リストのヒープ化

for i in range(m):
    x = heapq.heappop(a) * (-1) # 最大値を取り出す
    y = x // 2 # 割引券で半額にする
    heapq.heappush(a, -y) # 割り引いた商品をリストに戻す
print(-sum(a))

# ------------------ Sample Input -------------------
3 3
2 13 8

4 4
1 9 3 5

1 100000
1000000000

10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000

# ----------------- Length of time ------------------
# 20分AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc141/editorial.pdf
# 初めてヒープ使った。
# データ構造で殴れそうだな？というところまで思いついて，けんちょん本の内容で殴れそうなものを自力で思い出した
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#O(NlogN)
#優先度付きキュー
#ヒープ
#heapq
#PriorityQueue
#ABC-D
#貪欲法
#greedy