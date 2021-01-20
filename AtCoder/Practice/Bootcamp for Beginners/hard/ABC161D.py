# ABC161D - Lunlun Number
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc161/tasks/abc161_d
# Date: 2021/01/19

# ---------- Ideas ----------
# 755と全く同じ問題！
# DFSで再帰でも解けるし，BFSっぽくqueue使ったfor文でも解ける!

# ------------------- Solution --------------------
# 1から9の整数のリストだけ用意して，1桁ずつ増やしていく
# 各数字の1桁目を見て，ケツに加える候補(option)を加えて，リストに戻す
# 最後にk番目に小さい数を出力する

# ------------------- Answer --------------------
#code:python
n = int(input())
option = [[0, 1], [0,1,2], [1,2,3], [2,3,4], [3,4,5],
          [4,5,6], [5,6,7], [6,7,8], [7,8,9], [8,9]]

l = [i for i in range(1,10)]
l2 = l[:]
while l[-1] < 3234566667:
    l3 = []
    for a in l2:
        last = int(str(a)[-1])
        for i in option[last]:
            l3.append(int(str(a)+str(i)))
    l += l3
    l2 = l3[:]

l.sort()
print(l[n-1])


# ヒープキューを使って，最小値をpopしてきて，ルンルンに変換してキューに突っ込む，というのがいいらしい
# https://satoooh.com/entry/6417/
k = int(input())
option = [[0, 1], [0,1,2], [1,2,3], [2,3,4], [3,4,5],
          [4,5,6], [5,6,7], [6,7,8], [7,8,9], [8,9]]
from heapq import heappush, heapify, heappop
a = [i for i in range(1,10)]
heapify(a)  # リストのヒープ化

for i in range(k-1):
    x = heappop(a)
    for i in option[int(str(x)[-1])]:
        heappush(a, int(str(x) + str(i)))
print(a[0]) # k回目に取り出す最小値が先頭に来ている。


# ------------------ Sample Input -------------------
15

1

13

100000

# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc161/editorial.pdf
# 今回は文字列で処理したが，10倍して0or-1or1を足す，という処理の方が美しくかけるようだ: 要復習
# ヒープでk回目に取り出すものがk番目に小さい数，というのは今までにない発想だった

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#wanna_review #hard復習 #復習したい
#整数を「10倍してaを足す」で捉え
#緑diff
#ABC-D
#dfs
#再帰関数
#priority_queue
#ヒープ
#heap
#優先度付きキュー