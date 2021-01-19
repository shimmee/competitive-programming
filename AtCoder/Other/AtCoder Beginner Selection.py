########################################################################################
# AtCoder Beginner Selection: 最初に解くべき10問
# https://atcoder.jp/contests/abs
########################################################################################


##############################################################
# 1問目
# タイトル: ABC086A - Product
# URL: https://atcoder.jp/contests/abs/tasks/abc086_a
# 日時: 2020/10/**
##############################################################

from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')

##############################################################
# 2問目
# タイトル: ABC081A - Placing Marbles
# URL: https://atcoder.jp/contests/abs/tasks/abc081_a
# 日時: 2020/10/**
##############################################################

from sys import stdin
s = stdin.readline().rstrip()
print(int(s[0]) + int(s[1]) + int(s[2]))


##############################################################
# 3問目
# タイトル: ABC081B - Shift only
# URL: https://atcoder.jp/contests/abs/tasks/abc081_b
# 日時: 2020/10/**
##############################################################

from sys import stdin
import numpy as np

N = stdin.readline().rstrip()
A = np.array([int(x) for x in stdin.readline().rstrip().split()])

time = 0
while sum(A % 2) == 0:
    A = A / 2
    time += 1
print(time)

##############################################################
# 4問目
# タイトル: ABC087B - Coins
# URL: https://atcoder.jp/contests/abs/tasks/abc087_b
# 日時: 2020/10/**
##############################################################

from sys import stdin
A = int(stdin.readline().rstrip())
B = int(stdin.readline().rstrip())
C = int(stdin.readline().rstrip())
X = int(stdin.readline().rstrip())
time = 0
for a in range(0, A + 1):
    for b in range(0, B + 1):
        for c in range(0, C + 1):
            total = 500*a + 100*b + 50*c
            if total == X: time += 1
print(time)


##############################################################
# 5問目
# タイトル: ABC083B - Some Sums
# URL:https://atcoder.jp/contests/abs/tasks/abc083_b
# 日時: 2020/10/**
##############################################################

from sys import stdin
import numpy as np
N, A, B = [int(x) for x in stdin.readline().rstrip().split()]
sum_of_n = 0
for n in range(1, N+1):
    digit_sum = np.array(list(str(n))).astype(int).sum()
    if digit_sum >= A and digit_sum <= B:
        sum_of_n = sum_of_n + n
print(sum_of_n)



##############################################################
# 6問目
# タイトル: ABC088B - Card Game for Two
# URL: https://atcoder.jp/contests/abs/tasks/abc088_b
# 日時: 2020/10/**
##############################################################

import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
A.sort()
A = A[::-1]
alice_index = [i for i in range(N) if i%2==0]
bob_index = [i for i in range(N) if i%2==1]
gap = A[alice_index].sum() - A[bob_index].sum()
print(gap)


##############################################################
# 7問目
# タイトル: ABC085B - Kagami Mochi
# URL:
# 日時: 2020/10/**
##############################################################
n = int(input())
d = [int(input()) for i in range(n)]
print(len(set(d)))


##############################################################
# 8問目
# タイトル: ABC085C - Otoshidama
# URL: https://atcoder.jp/contests/abs/tasks/abc085_c
# 日時: 2020/10/**
##############################################################

from sys import stdin

N, Y = [int(x) for x in stdin.readline().rstrip().split()]

max_10000 = Y // 10000
max_5000 = Y // 5000

res = None
for n_10000 in range(0, min(N, max_10000) + 1):
    for n_5000 in range(0, min(N, max_5000) + 1):
        n_1000 = N - (n_10000 + n_5000)
        if n_1000 < 0: break
        total = 10000 * n_10000 + 5000 * n_5000 + 1000 * n_1000
        # if total > Y: break
        if total == Y:
            res = [n_10000, n_5000, n_1000]
            break

if res is None:
    print('-1 -1 -1')
elif res is not None:
    print(f'{res[0]} {res[1]} {res[2]}')



##############################################################
# 9問目
# タイトル: ABC049C - 白昼夢
# URL: https://atcoder.jp/contests/abs/tasks/arc065_a
# 日時: 2020/10/**
##############################################################

S = input()
S_original = None
while S_original != S:
    S_original = S
    if S[-5:] == 'erase':
        S = S[:-5]
    elif S[-5:] == 'dream':
        S = S[:-5]
    elif S[-6:] == 'eraser':
        S = S[:-6]
    elif S[-7:] == 'dreamer':
        S = S[:-7]

    if S == '':
        print('YES')
        exit()
print('NO')


##############################################################
# 10問目
# タイトル: ABC086C - Traveling
# URL: https://atcoder.jp/contests/abs/tasks/arc089_a
# 日時: 2020/10/**
##############################################################