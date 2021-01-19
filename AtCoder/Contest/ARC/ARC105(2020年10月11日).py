##############################################################
# 大会名: AtCoder Regular Contest 105
# 時間: 2020-10-11(日) 22:30 ~ 2020-10-12(月) 00:10 (100分)
##############################################################
def getN(): return int(input())
def getLI(): return list(map(int,input().split()))

##############################################################
# 1問目
# タイトル: A - Fourtune Cookies
# URL: https://atcoder.jp/contests/arc105/tasks/arc105_a
##############################################################

# bit全探索: N=4なのでどう書いてもよい

import numpy as np
def getLI(): return list(map(int,input().split()))
cookie = np.array(getLI())

for i in range(4**2):
    bit = np.array([i >> j & 1 for j in range(4)])
    if (cookie * bit).sum() == (cookie * (bit^1)).sum():
        print('Yes')
        exit()
print('No')



##############################################################
# 2問目
# タイトル: B - MAX-=min
# URL: https://atcoder.jp/contests/arc105/tasks/arc105_a
##############################################################
import numpy as np
def getN(): return int(input())
def getLI(): return list(map(int,input().split()))

# 方針
# aの最小値を見つけて，a mod 最小値 を計算する。つまり，aの各要素を最小値で割ったときの余りを計算する。
# 割り切れる場合は余りを最小値とする。
# これを全部同じ値になるまで繰り返す

N = getN()
a = np.array(getLI())

while True:
    minimum = min(a)
    if sum(a == minimum) == N:
        print(minimum)
        break
    a = a % min(a)
    a = np.where(a==0, minimum, a)




##############################################################
# 4問目
# タイトル: D - Let's Play Nim
# URL: https://atcoder.jp/contests/arc105/tasks/arc105_d
##############################################################


all_input=[]
while True:
    try:
        all_input.append(list(map(int, input().split())))
    except:
        break;

T = all_input[0]
all_input.pop(0)
for i in range(T[0]):
    if all_input[2*i][0] % 2 == 0:
        print('First')
    else:
        print('Second')


3
1
10
2
1 2
21
476523737 103976339 266993 706803678 802362985 892644371 953855359 196462821 817301757 409460796 773943961 488763959 405483423 616934516 710762957 239829390 55474813 818352359 312280585 185800870 255245162