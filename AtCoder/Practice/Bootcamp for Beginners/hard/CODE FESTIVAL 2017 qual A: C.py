# CODE FESTIVAL 2017 qual A: C - Palindromic Matrix
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_c
# Date: 2021/01/25

# ---------- Ideas ----------
# 全ての文字の出現回数をカウントする

# ------------------- Solution --------------------
# H*Wが偶*偶: 出現回数が全て4の倍数ならYes
# H*Wが偶*奇: 奇数があったらだめ，4の倍数ではなくて2の倍数の個数が
# H*Wが奇*奇: 出現回数が1つだけ奇数，この奇数をoddとする
# 4の倍数でなくて2の倍数であるものがp個以上，(H+W-1-odd)//2個以下
# odd=3,7,11,...のときp=1, odd=1,5,9,...のときp=0

# ------------------- Answer --------------------
code:python
    from collections import Counter
    H, W = map(int, input().split())
    A = ''
    for _ in range(H):
        A += input()
    counter = Counter(A)

    if H % 2 == 0 and W % 2 == 0: # 偶*偶
        flag = True
        for key, value in counter.items():
            if value % 4 != 0:
                flag = False
    elif H % 2 == 1 and W % 2 == 1: # 奇*奇
        odd_cnt = 0
        odd = 0
        mul2 = 0
        for key, value in counter.items():
            if value % 4 == 0:
                pass
            elif value % 2 == 0:
                mul2 += 1
            if value % 2 == 1: # 出現回数が奇数
                odd_cnt += 1
                odd = value

        # 奇数が1つでかつ
        if odd_cnt == 1:
            p = 0 if odd % 4 == 1 else 1

            # 解説ACした後に判明したんだけど，ここの処理が間違ってました。(H+W-2)//2以下でした!!!
            if p <= mul2 <= (H+W-1-odd)//2: # mul2がp個以上，(H+W-1-odd)//2以下
                flag = True
            else:
                flag = False
        else:
            flag = False
    else: # 偶*奇
        m = H//2 if H % 2 == 0 else W//2
        mul2 = 0
        flag= True
        for key, value in counter.items():
            if value % 4 == 0:
                pass
            elif value % 2 == 0:
                mul2 += 1
            else: # 奇数があったらダメ
                flag = False
        if not (0 <= mul2 <= m):
            flag = False

    if flag: print('Yes')
    else: print('No')

    # 1000 WAが4つ。おしい
    # 1020 WAが2つ
    # 1039 WAが1つ


    # 解説AC: https://www.hamayanhamayan.com/entry/2017/09/24/012523
    # 奇数*奇数の場合はど真ん中は4で割ると1余る数になる必要(1つ必要)がある。
    # あとは、4で割ると2余る数が使われるのが(H-1)/2+(W-1)/2以下であればいい。

    from collections import Counter
    H, W = map(int, input().split())
    A = ''
    for _ in range(H):
        A += input()
    counter = Counter(A)

    if H % 2 == 0 and W % 2 == 0: # 偶*偶
        flag = True
        for key, value in counter.items():
            if value % 4 != 0:
                flag = False
    elif H % 2 == 1 and W % 2 == 1: # 奇*奇
        mul2 = 0
        odd_cnt = 0
        for key, value in counter.items():
            if value % 4 == 2:
                mul2 += 1
            elif value % 2 == 1: # 出現回数が奇数
                odd_cnt += 1
        # 奇数が1つでかつ
        if odd_cnt == 1 and mul2 <= (H-1)/2+(W-1)/2:
            flag = True
        else:
            flag = False
    else: # 偶*奇
        m = H//2 if H % 2 == 0 else W//2
        mul2 = 0
        flag= True
        for key, value in counter.items():
            if value % 4 == 2:
                mul2 += 1
            elif value % 2 == 1: # 奇数があったらダメ
                flag = False
        if not (0 <= mul2 <= m):
            flag = False

    if flag: print('Yes')
    else: print('No')

# ------------------ Sample Input -------------------
3 4
aabb
aabb
aacc

2 2
aa
bb

5 1
t
w
e
e
t

2 5
abxba
abyba

1 1
z


# ----------------- Length of time ------------------
# 2時間かけて1WAとれずに解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/code-festival-2017-quala/editorial.pdf
# 奇数*奇数のときに，「4で割って2余る数」の出現回数の上限の処理が間違ってた
# (H+W-1-odd)//2でやってたら，ただしくは(H+W-2)//2だった
# 復習はしたくない

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#回文
#Counter
#文字の出現回数
#偶奇に着目
