# AtCoder Petrozavodsk Contest 001: B - Two Arrays
# URL: https://atcoder.jp/contests/apc001/tasks/apc001_b
# Date: 2021/02/28

# ---------- Ideas ----------
# こういうのは基本”できる”ので，できない場合を考える
# aのトータル > bのトータル のときは無理
# aとbはソートしちゃだめ
# a > bとなる要素の数が半分以上あったら無理 -> うそ
# Bのトータル - Aのトータル: 最大で可能な操作回数
# a < bとなる個数 >= Bのトータル - Aのトータル


# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# aのトータル > bのトータル のときは無理
if sum(A) > sum(B):
    print('No')
    exit()

cnt = 0
for i in range(n):
    if A[i] > B[i]:
        cnt += 1

# a > bとなる要素の数が半分以上あったら無理
if n/2 < cnt:
    print('No')
else:
    print('Yes')

# 28ケース中3ケースWA: コーナーケースか？
# a > bとなる要素の数が半分以上あったら無理 -> これは嘘
# (2,2,1), (1,1,6)は行ける
# aをbに近づけるために必要な分とbをaに近づけるために必要な分: cnt_a, cnt_b
# cnt_a >= cnt_b*2のときは行ける

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# aのトータル > bのトータル のときは無理
if sum(A) > sum(B):
    print('No')
    exit()

cnt_a = 0 #
cnt_b = 0
for i in range(n):
    if A[i] < B[i]:
        cnt_a += B[i] - A[i]
    elif A[i] > B[i]:
        cnt_b += A[i] - B[i]

if cnt_a < cnt_b*2:
    print('No')
else:
    print('Yes')

# WA2つが取れない！！！
# 解説見た
# cnt_bは1回，cnt_aは2回ずつ行う必要があるので，これが操作可能回数(bのトータル-aのトータル)より小さければOK

import math
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if A[i] < B[i]:
        cnt += (B[i] - A[i])//2
    elif A[i] > B[i]:
        cnt -= A[i] - B[i]

if cnt >= 0 :
    print('Yes')
else:
    print('No')


# ------------------ Sample Input -------------------
3
2 1 1
1 2 2


3
1 2 3
5 2 2

4
2 2 1 1
1 1 2 2

5
3 1 4 1 5
2 7 1 8 2

5
2 7 1 8 2
3 1 4 1 5

# ----------------- Length of time ------------------
# 1.5hかけてWAが取れなくて解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/apc001/editorial.pdf
# とても惜しいところまで行ったけど，最後が詰められなかった
# 自信のないまま嘘貪欲を何度も提出してWAを出した
# 惜しい嘘貪欲は2WAとかになって，嘘なのかコーナーなのかよくわからん


# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#数列
#操作:Yes/No判定問題
#操作を好きな回数だけ行える
#SをTにすることが目的の操作の問題
#必要条件を列挙したら十分条件になる
#決めてから整合性を確認する
#端から順に決まって行くGreedy
#Greedy
#緑diff
#AGC-like
#嘘貪欲にハマりやすい