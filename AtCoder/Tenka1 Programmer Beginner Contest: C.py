# Tenka1 Programmer Beginner Contest: C - Align
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_c
# Date: 2021/01/28

# ---------- Ideas ----------
# 真ん中に大きいのを入れて，その左右に小さいのを1つずつ，またその左右に大きいのを1つずつ，という感じでミルフィーユする
# 最初に小さいのを入れて，大きいので挟む，小さいので挟む，というパターンもあるので，
# 両方試して大きい方を出力
# dequeがあると書きやすい

# appendleft, appendとpopleft，popを繰り返す


# ------------------- Answer --------------------
#code:python
from collections import deque
n = int(input())
A = sorted([int(input()) for _ in range(n)])

a = deque(A)
l = deque([])
l.append(a.popleft())
i = 0
while a:
    if i % 2 == 0: # 大きい数字をlの左端と右端にいれる
        l.appendleft(a.pop())
        if not a: break
        l.append(a.pop())
    else: # 小さい数字をlの左端と右端にいれる
        l.appendleft(a.popleft())
        if not a: break
        l.append(a.popleft())
    i += 1

ans1 = 0
for i in range(n-1):
    ans1 += abs(l[i]-l[i+1])


a = deque(A)
l = deque([])
l.append(a.pop())
i = 0
while a:
    if i % 2 == 1: # 大きい数字をlの左端と右端にいれる
        l.appendleft(a.pop())
        if not a: break
        l.append(a.pop())
    else: # 小さい数字をlの左端と右端にいれる
        l.appendleft(a.popleft())
        if not a: break
        l.append(a.popleft())
    i += 1

ans2 = 0
for i in range(n-1):
    ans2 += abs(l[i]-l[i+1])
print(max(ans1, ans2))

# ------------------ Sample Input -------------------
5
6
8
1
2
3

6
3
1
4
1
5
9

# ----------------- Length of time ------------------
# 30分，解説のヒントを少しだけみた

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/tenka1-2018/editorial.pdf

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#2つ試して良い方を出力
#deque
#キュー
#貪欲
#greedy
#数列の並び替え
#数列
#差が大きくなるようにする