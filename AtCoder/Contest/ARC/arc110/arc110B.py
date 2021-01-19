# ARC110B - Many 110
# URL: https://atcoder.jp/contests/arc110/tasks/arc110_b
# 日付: 2020-12-05

# ---------- 思ったこと / 気づいたこと ----------
# Tが2文字以上なら，最初の2文字でどこからスタート=sかわかる
# 文字列終了の位置もs+N-1でわかる

# ------------------- 解答 --------------------
#code:python
import math
N = int(input())
T = input()
length = 3*(10**10)

# Tが1文字(N==1)のとき
if N == 1:
    if T == '0':
        print(10**10)
        exit()
    elif T == '1':
        print(2*(10**10))
        exit()
    else:
        print(0)
        exit()

# Tが2文字(N==2)のとき
if N == 2:
    if T == '01' or T == '11' or T == '10':
        pass
    else:
        print(0)
        exit()

# そもそもTが110だけで作られてるか確かめる
# 0の1つ前と2つ前は'1'である必要がある
# 1の1つ前か2つ前は'0'である必要がある
flag = True
for i in range(N):
    if i == 0 or i == 1:
        continue

    if T[i] == '0':
        if T[i-1] == '1' and T[i-2] == '1':
            pass
        else:
            flag = False
    if T[i] == '1':
        if (T[i - 1] == '0' and T[i - 2] == '1') or (T[i - 1] == '1' and T[i - 2] == '0'):
            pass
        else:
            flag = False
if not flag:
    print(0)
    exit()

# Nが2以上のとき
n = 0
if N >= 2:
    c = T[:2] # first two characters

    # start position
    if c == '11':
        s = 0
    elif c == '10':
        s = 1
    elif c == '01':
        s = 2

    n = math.ceil((length-s-N+1)/3)
    print(n)



# ------------------ 入力例 -------------------
3
111

4
1011

1
9

2
10

2
98

22
1011011011011011011011


# ----------------- 解答時間 ------------------
# 1時間くらいAC

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/arc110/editorial/383
# 解説みたらもう少し簡単に解かれてた

# ----------------- カテゴリ ------------------
#AtCoder #arc
#等差数列