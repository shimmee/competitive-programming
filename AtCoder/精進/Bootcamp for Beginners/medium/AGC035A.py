# AGC035A - XOR Circle
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc035/tasks/agc035_a
# Date: 2021/01/09

# ---------- Ideas ----------
# XoRとは書いてるけど，単純に足し算だと理解しても良いかも? ー＞ だめです


# ------------------- Solution --------------------
# 解説みた
# a^a=0は必ず成り立つ性質
# 連続してb,a,cという数が並んでいるとき，真ん中aは両隣b,cのxorに等しいのでa=b^c
# これをa^a=0に代入するとa^b^c=0
# これを満たす状態は以下の3つのどれか
# 1. 全ての要素が3
# 2. n個の要素のうち2/3が同じで，残り1/3が全部0
# 3. n個がa,b,cの数字だけで構成されていて，a^b^c=0で，かつ1/3個ずつある

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

# 1. 全ての要素が3
if all(i==0 for i in a): print('Yes'); exit()
if n % 3 == 0:
    from collections import Counter
    counter = Counter(a)

    # 2. n個の要素のうち2/3が同じで，残り1/3が全部0
    if len(counter) == 2 and counter[0] == n//3:
        print('Yes'); exit()

    # 3. n個がa,b,cの数字だけで構成されていて，a^b^c=0で，かつ1/3個ずつある
    elif len(counter) == 3:
        keys = list(counter.keys())
        values = list(counter.values())

        if all(i == n//3 for i in values) and (keys[0] ^ keys[1] ^ keys[2] == 0):
            print('Yes'); exit()
print('No')
# ------------------ Sample Input -------------------
4
0 0 0 0

3
1 2 3

4
1 2 4 8

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc035/editorial.pdf
# ムズい。Xorの性質を知らなかったので，解説見てよかった

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#AC_with_editorial #解説AC
#wanna_review #medium復習
#復習したい
#排他的論理和
#XOR