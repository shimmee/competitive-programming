# ARC042A - 掲示板
# URL: https://atcoder.jp/contests/arc042/tasks/arc042_a
# Date: 2021/02/13

# ---------- Ideas ----------
# 1からnまでのリストを作る: dequeにする
# m個の入力をappendleftする: 最新のものから左に現れる
# 同じ数字が何度も出ているが，左から最新のものだけ出力する。flag使って上手いこと

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n, m = map(int, input().split())
thread = deque([i for i in range(1, n+1)])
for _ in range(m):
    a = int(input())
    thread.appendleft(a)

flag = [False]*(n+1)
for a in thread:
    if not flag[a]:
        print(a)
        flag[a] = True

# ACだけど！
# 最初にm個入力しておいて，最後から順番に出力すればいいという説もある
n, m = map(int, input().split())
thread = [i for i in range(1, n+1)][::-1] + [int(input()) for _ in range(m)]
thread = thread[::-1]
flag = [False]*(n+1)
for a in thread:
    if not flag[a]:
        print(a)
        flag[a] = True

# ------------------ Sample Input -------------------
10 10
3
1
4
1
5
9
2
6
5
3

# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc042
# ただのソートだった

# ----------------- Category ------------------
#AtCoder
#ソート
#flagを上手く使う