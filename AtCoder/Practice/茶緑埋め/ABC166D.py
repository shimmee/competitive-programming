# ABC166D - I hate Factorization
# URL: https://atcoder.jp/contests/abc166/tasks/abc166_d
# Date: 2021/02/06

# ---------- Ideas ----------
# A, Bともに-1000から1000くらいまで全通り試してみる


# ------------------- Answer --------------------
#code:python
x = int(input())
for a in range(-1001, 1001):
    for b in range(-1001, 1001):
        if a**5 - b**5 == x:
            print(a, b)
            exit()

# ------------------ Sample Input -------------------
33


# ----------------- Length of time ------------------
# 3分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc166/editorial.pdf
# けんちょんさん解説わかりやすい: https://drken1215.hatenablog.com/entry/2020/06/20/231600
# 2015−2005=8080401001 となって、これは 109 を超えている。
# このことは、A や B が 200 以上になるような範囲は調べなくて良い、ということを意味している。
# 1 違うだけで 109 も変わるのだから

# ----------------- Category ------------------
#AtCoder
#全探索
#方程式
#整数問題