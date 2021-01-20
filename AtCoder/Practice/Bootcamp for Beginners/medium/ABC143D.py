# ABC143D - Triangles
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc143/tasks/abc143_d
# Date: 2021/01/07

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# aとbをループでとって，条件を満たすcを二分探索かな: O(N^2 logN)
# a <= b <= cとすると重複を数えなくて住む

# ------------------- Answer --------------------
#code:python

n = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(n):
    for j in range(i+1, n):
        a = L[i]
        b = L[j]

        # |a-b| < cとなるインデックスを探す: 右側がOK
        ok = n-1
        ng = -1
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            c = L[mid]
            if abs(a-b) < c: ok = mid
            else: ng = mid
        left = ok

        # c < a+bとなるインデックスを探す: 左側がOK
        ok = 0
        ng = n
        while (abs(ng - ok) > 1):
            mid = (ok + ng) // 2
            c = L[mid]
            if c < a + b: ok = mid
            else: ng = mid
        right = ok

        ans += max(0, right - max(j, left))

print(ans)

# 皆うまいことbisectで書いてる
# https://atcoder.jp/contests/abc143/submissions/18989535
# a <= b <= cのとき，aとbを固定したら，c < a + bとなるcを探せばいいだけになるので，二分探索2回はいらない
n = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(n):
    for j in range(i+1, n):
        a = L[i]
        b = L[j]

        # c < a+bとなるインデックスを探す: 左側がOK
        ok = 0
        ng = n
        while (abs(ng - ok) > 1):
            mid = (ok + ng) // 2
            c = L[mid]
            if c < a + b: ok = mid
            else: ng = mid
        right = ok

        ans += max(0, right - j)

print(ans)

# さらにいうと，bisectで書ける。インデックスが1つずれる？ので処理する

import bisect
n = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = L[i]
        b = L[j]

        # c < a+bとなるインデックスを探す: 左側がOK
        right = bisect.bisect_left(L, a+b)
        if j < right - 1:
            ans += max(0, right - j - 1)

print(ans)
# ------------------ Sample Input -------------------
4
3 4 2 1

3
1 1000 1


7
218 786 704 233 645 728 389

# ----------------- Length of time ------------------
# 64 min

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc143/editorial.pdf
# 思いついてから解けるまでが時間かかった
# 第1の壁: bisectのインデックスが謎 -> 諦めて二分探索スクラッチで書いた
# 第2の壁: a,b,cの重複をどう削るか -> a <= b <= cと仮定
# 教育的に良い問題だったので，また復習したい


# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#三角不等式
#bisect
#binary_search
#二分探索
#wanna_review #medium復習