# ABC200D - Happy Birthday! 2
# URL: https://atcoder.jp/contests/abc200/tasks/abc200_d
# Date: 2021/05/08

# ---------- Ideas ----------
# A の要素を200で割る
# 長さが違う(x!=y) か， 同じ長さでも，どこかしらの要素が異なる

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
a = list(map(int, input().split()))
rem = [i % 200 for i in a]

# 同じ余りが2つ以上あれば，それを1つずつ出力して終わり
c = Counter(rem)
flag = False
for key, value in c.items():
    if value >= 2:
        flag = True
        break
if flag:
    l = []
    for i in range(n):
        if a[i] % 200 == key:
            l.append(i+1)
    print('Yes')
    print(1, l[0])
    print(1, l[1])

# なければ，部分和問題になる
# dp[i][j]: i番目までの整数を選んでjにできる場合の数
# 経路復元

dp = [[0 for _ in range(200)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(200):
        if j >= rem[i]:
            dp[i + 1][j] = dp[i][j - rem[i]]
        else:
            dp[i + 1][j] = dp[i][200 + j - rem[i]]
        dp[i + 1][j] += dp[i][j]


# 2つのルートがない場合
flag = False
part_sum = 0
for i in range(n):
    for j in range(200):
        if dp[i][j] >= 2:
            print(j, j % 200)
            part_sum = j
            flag = True
if not flag:
    print('No')

##################################################
##################################################
##################################################
# 本番間に合いませんでした
# dpは枝刈りしてOK: 通り数が2以上になった時点で止める

from collections import deque, Counter
n = int(input())
a = list(map(int, input().split()))
rem = [i % 200 for i in a]

# 同じ余りが2つ以上あれば，それを1つずつ出力して終わり
c = Counter(rem)
flag = False
for key, value in c.items():
    if value >= 2:
        flag = True
        break
if flag:
    l = []
    for i in range(n):
        if a[i] % 200 == key:
            l.append(i+1)
    print('Yes')
    print(1, l[0])
    print(1, l[1])
    exit()

# なければ，部分和問題になる
# dp[i][j]: i番目までの整数を選んでjにできる場合の数
# 経路復元

dp = [[0 for _ in range(200)] for _ in range(n+1)]
dp[0][0] = 1
break_flag = False
route = [[[] for _ in range(200)] for _ in range(n+1)]

for i in range(n):
    for j in range(200):
        if j >= rem[i]:
            dp[i + 1][j] = dp[i][j - rem[i]]
            if dp[i][j - rem[i]] >= 1:
                route[i + 1][j].append([j - rem[i], rem[i]])
        else:
            dp[i + 1][j] = dp[i][200 + j - rem[i]]
            if dp[i][200 + j - rem[i]] >= 1:
                route[i + 1][j].append([200 + j - rem[i], rem[i]])
        dp[i + 1][j] += dp[i][j]
        if dp[i][j] >= 1:
            route[i + 1][j].append([j, None])
        if dp[i + 1][j] >= 2:
            break_flag = True
            break
    if break_flag:
        break
else:
    print('No')
    exit()


print('Yes')
j_now, used = route[i + 1][j][0]
i_now = i
l1 = [used]
while i_now != 0:
    j_now, used = route[i_now][j_now][0]
    l1.append(used)
    i_now -= 1

B = []
for p in l1:
    if p in rem:
        B.append(rem.index(p) + 1)
print(len(B), *sorted(B))


j_now, used = route[i + 1][j][1]
i_now = i
l2 = [used]
while i_now != 0:
    j_now, used = route[i_now][j_now][0]
    l2.append(used)
    i_now -= 1

C = []
for p in l2:
    if p in rem:
        C.append(rem.index(p) + 1)
print(len(C), *sorted(C))

# WAです
##################################################
##################################################
##################################################
# 想定解法の鳩の巣原理 bit全探索でやってみます

n = int(input())
a = list(map(int, input().split()))
m = min(8, n)

rem_comb = [[] for _ in range(200)]
import itertools
all_pattern = itertools.product([0, 1], repeat=m)
for pattern in all_pattern:
    if sum(pattern) == 0: # 空集合はダメ
        continue

    # bitが立ってるインデックスの要素を足していく
    summed = 0
    for i in range(m):
        if pattern[i] == 1:
            summed = (summed + a[i]) % 200
    rem_comb[summed].append(pattern)

    if len(rem_comb[summed]) >= 2: # 2つのパターンが揃ったなら出力
        B = [j + 1 for j in range(m) if rem_comb[summed][0][j] == 1]
        C = [j + 1 for j in range(m) if rem_comb[summed][1][j] == 1]

        print('Yes')
        print(len(B), *B)
        print(len(C), *C)
        exit()
print('No')


# ------------------ Sample Input -------------------
5
1 3 10 11 100

5
180 186 189 191 218

6
2013 1012 2765 2021 508 6971

2
123 523

2
1 200
# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# 本番ではDPの経路復元で解こうとして無理だった
# そのあとずっとトライして自力で書いたけどWAが取れなくて諦めた
# 解説の鳩の巣原理からのbit全探索でスラスラ書けた

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#鳩の巣原理
#bit全探索
#DP
#DPの経路復元
#動的計画法