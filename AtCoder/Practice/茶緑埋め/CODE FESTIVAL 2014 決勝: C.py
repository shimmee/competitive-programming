# CODE FESTIVAL 2014 決勝: C - N進数
# URL: https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_c
# Date: 2021/02/18

# ---------- Ideas ----------
# 問題文が難解過ぎる
# N進数でNとなるような数字を10進数表記するためにf(N)と書いた時，f(N)=AのA(10進数)を入力として与えるので，
# Nが存在するなら出力せよ，という問題
# N=10000まで全探索すればA=10**16を超えるのでOK

# ------------------- Answer --------------------
#code:python
# 10進数をN進数に変換: https://iatlex.com/python/base_change
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

A = int(input())
for n in range(2, 10001):
    B = Base_10_to_n(A, n)
    if n == int(B):
        print(n); exit()
print(-1)

# ------------------ Sample Input -------------------
49

# ----------------- Length of time ------------------
# 15分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/codefestival2014final
# これはちょっと問題文が悪い
# f(N)が10進数であることがあまりにもわかりづらい

# ----------------- Category ------------------
#AtCoder
#N進数変換
#全探索
