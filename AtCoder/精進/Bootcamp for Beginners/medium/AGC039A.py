# AGC039A - Connection and Disconnection
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc039/tasks/agc039_a
# Date: 2021/01/06

# ---------- Ideas ----------
# 連続するp文字があったら，連続しないように塗り替えるのはp//2回 ・・・☆
# itertoolsで連続するやつを数えられるので使う

# ------------------- Solution --------------------
# 場合分け
# 全部同じ文字のとき，n文字がk回続くのでn*k//2が答え
# 先頭とケツが異なる時，中で連続する文字の☆を求めればいい
# 先頭とケツが同じとき，頭とケツ以外の連続する文字の☆ + 頭とケツの結合か連続するk-1回文の☆ + 先頭の頭の☆ + 最後尾のケツの☆

# ------------------- Answer --------------------
#code:python
S = input()
k = int(input())
n = len(S)

# 連続した文字数をカウントする
import itertools
gr = itertools.groupby(S)
l = []
for key, group in gr:
    l.append(len(list(group)))
m = len(l)

# 全部同じ文字のとき
if m == 1:
    print(n*k // 2); exit()

ans = 0
if S[0] != S[-1]: # Sの先頭と最後が違う時
    for i in l:
        ans += (i // 2)*k

else: # Sの先頭と最後が同じ時
    # 頭とケツ以外
    for i in range(m):
        if i != 0 and i != m-1:
            ans += (l[i] // 2)*k

    # 最初の頭と最後のケツ
    ans += l[0] // 2
    ans += l[-1] // 2

    # 頭とケツの結合: k-1回
    ans += ((l[0]+l[-1]) // 2) * (k-1)
print(ans)




# ------------------ Sample Input -------------------
a
3

ab
100

issii
2

qq
81

cooooooooonteeeeeeeeeest
999993333

# ----------------- Length of time ------------------
# 32 min

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc039/editorial.pdf
# 解説通りに溶けた
# itertoolsがすごすぎる

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#コーナーケース
#itertools.groupby