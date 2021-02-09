# ABC165D - Floor Function
# URL: https://atcoder.jp/contests/abc165/tasks/abc165_d
# Date: 2021/02/08

# ---------- Ideas ----------
# xはなるべく大きく，かつx%bが正でなるべく小さくなるようにしたい?
# nをbで割った商と余りをq,rとすると，b*q, b*q+r, b*q-1, b*q+r-1，あたりが候補になりそう

# ------------------- Answer --------------------
#code:python
def fun(a, b, x):
    return a*x//b - a*(x//b)
a, b, n = map(int, input().split())
if b > n:
    print(fun(a,b,n))
else:
    q, r = divmod(n, b)
    x1 = b*q
    x2 = b * q + r
    x3 = b*q - 1
    x4 = b * q +r -1
    print(max(fun(a,b,x1), fun(a,b,x2), fun(a,b,x3), fun(a,b,x4)))

# ------------------ Sample Input -------------------
11 10 9

11 10 21

1000000 1000000000000 1000000000000
# ----------------- Length of time ------------------
# 18分

# -------------- Editorial / my impression -------------
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/05/02/225600
# 実験を繰り返せば，x=min(B-1, N)すればいいことがわかるらしい。

# ----------------- Category ------------------
#AtCoder
#ABC-D
#整数問題
#気付き系
#周期性に着目する
#単調性に着目する
#実験
#茶diff