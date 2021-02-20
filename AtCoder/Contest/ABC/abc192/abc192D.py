# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192): D - Base n
# URL: https://atcoder.jp/contests/abc192/tasks/abc192_d
# Date: 2021/02/20

# ---------- Ideas ----------
# d+1進数からk進数までOKで，それ以降はダメ，そんなkを探す
# kは最大でもmまで，つまり10^18まで。線形探索じゃ間に合わないので，二分探索

# ------------------- Solution --------------------
# XをN進数から10進数に変換する関数を用意
# d = Xの最大の数値
# d+1を10進数に変換した時にmより大きかったらだめ，
# Xが一桁の時，d=Xとなり，d > mならダメでprint(0)，d <= mならprint(1)
# Xが2桁以上のとき，左がOKな二分探索で右に探していく

# 本番，Xが一桁のときのコーナーケースが間に合わなかった

# ------------------- Answer --------------------
#code:python
def Base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(str(X)[-i]) * (n ** (i - 1))
    return out  # int out


X = int(input())
m = int(input())
d = max([int(i) for i in str(X)])

if int(Base_n_to_10(X, d+1)) > m:
    print(0); exit()

if len(str(X)) == 1: # X=dのとき: 一桁のとき
    if d > m: print(0)
    else: print(1)
    exit()


# 二分探索
ok = d + 1  # 絶対okの範囲
ng = 10**20  # 絶対にngの範囲
while (abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    X_n = int(Base_n_to_10(X, mid))
    if X_n <= m:
        ok = mid
    else:
        ng = mid
print(ok - d)



# ------------------ Sample Input -------------------
1
1

897
100

999
1

10
1

100000000000000000000000000000000000000000000000000000000000
1000000000000000000

999
1500


# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# 惜しかった。これが解けてたらperf1500くらいいってた。くやじい
# もともとはサンプルにXが一桁の入力があったらしいけど，evima氏の指示により消されたらしい。

# ----------------- Category ------------------
#AtCoder
#ABC-D
#二分探索
#n進数
