# ABC127D - Integer Cards
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc127/tasks/abc127_d
# Date: 2021/01/12

# ---------- Ideas ----------
# 値Cより小さいAがあれば，小さいAからできるだけ多く，B枚まで変える
# データ構造で殴る系の問題かも
# N <= 10**5なので，おそらくO(M)かO(M*logN)で解く

# m回の操作後，少なくともCをb*m回使っていいわけになる。
# 最初の入力例だと，(3,3,5)が選べるCのやつで，これに加えてa=(5,1,4)があるから，
# この2つの配列から大きい数字をn個取ればいい

# ------------------- Solution --------------------
# Aを降順にソート, dequeで管理
# BCをCで降順にソート，dequeで管理
# AとBCからpopして，大きい方をどんどん空のリストに追加していく。
# A>=Cの場合は1つ追加，A<Cならb個分追加する

# ------------------- Answer --------------------
#code:python
from collections import deque
n, m = map(int, input().split())
A = list(map(int, input().split()))
A = deque(sorted(A, reverse=True))

BC = [[int(i) for i in input().split()] for _ in range(m)]
BC = deque(sorted(BC, key=lambda x: x[1], reverse=True))

a = A.popleft()
b, c = BC.popleft()

l = []
while len(l) < n:
    if a >= c:
        l.append(a)
        if len(A) > 0:
            a = A.popleft()
        else:
            a = -1
    else:
        l += [c for _ in range(b)]
        if len(BC) > 0:
            b, c = BC.popleft()
        else:
            b = -1
            c = 0

print(sum(l[:n]))



# ------------------ Sample Input -------------------
3 2
5 1 4
2 3
1 5

10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4

3 2
100 100 100
3 99
3 99

11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000

# ----------------- Length of time ------------------
# 24分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc127/editorial.pdf
# CをB個並べたリストを作ればいい，と思いついたのが素晴らしかった
# [b1,b1,b1,..., b1, b2,b2,...,b2]と並べるのではなく[[b1,c1], [b2,c2], ...]みたいに持つことをランレングス圧縮というらしい
# けんちょんさん解説: https://drken1215.hatenablog.com/entry/2019/06/15/021000

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ソート
#greedy
#緑diff
#ABC-D
#ランレングス圧縮
