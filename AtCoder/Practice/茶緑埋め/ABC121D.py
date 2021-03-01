# ABC121D - XOR World
# URL: https://atcoder.jp/contests/abc121/tasks/abc121_d
# Date: 2021/02/26

# ---------- Ideas ----------
# XORの性質「0≦aのとき、4a, 4a+1, 4a+2, 4a+3のxor和は0」が使えそう
# AとBの間が広い時，間の部分はほとんど相殺されて0になる
# AとBを4で割って，AとBの前後の相殺できない部分を計算するダメ

# ------------------- Answer --------------------
#code:python
A, B = map(int, input().split())

ans = 0
if B-A < 100: # 少なかったら全部計算
    for i in range(A, B + 1):
        ans ^= i
    print(ans)
else:
    ra = A % 4
    rb = B % 4

    for a in range(A, A+(4-ra)): # Aの相殺できない部分
        ans ^= a
    for b in range(B-rb, B + 1): # Bの相殺できない部分
        ans ^= b
    print(ans)

# ACしたけど
# 模範解答と全然違った

# AからBまでの排他的論理和f(A,B)は
# 0からBまでの排他的論理和と0からA-1までの排他的論理和の排他的論理和で表せる。つまり
# f(A,B) = f(0, B) ^ f(0, A-1) なので，一般にf(0, X)が求められれば良い
# 任意の偶数nに対して n^(n+1)=1となる: これはbitの一番下の桁だけが異なる。よって，
# Xが奇数のとき，f(0,3) = f(0,1) ^ f(2,3) = 1^1 = 0
# Xが偶数のとき，f(0,4) = f(0,1) ^ f(2,3) ^ 4 = 1^1^4 = 4
# 4で割った余りで決まる

def f(X: int): # f(0,X) を求める関数
    if X % 4 == 0: return X
    elif X % 4 == 1: return 1
    elif X % 4 == 2: return 1^X
    elif X % 4 == 3: return 0

A, B = map(int, input().split())
print(f(B)^f(A-1))



# ------------------ Sample Input -------------------
2 4

123 456

123456789012 123456789012

# ----------------- Length of time ------------------
# 13分AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc121/editorial.pdf
# 自分の解答でも，想定解法でも，どっちにしても4で割った余りを使う問題になった！
# とても勉強になった！
# 排他的論理和が割と好きになった！

# ----------------- Category ------------------
#AtCoder
#ABC-D
#XOR
#排他的論理和
#XORの性質
#制約条件:K以下
#整数問題
#パリティ
#スタートを0としてよい
#緑diff
#4で割った余り
#偶奇に注目