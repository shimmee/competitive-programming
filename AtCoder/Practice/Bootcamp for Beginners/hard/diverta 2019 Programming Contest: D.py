# diverta 2019 Programming Contest: D - DivRem Number
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d
# Date: 2021/01/27

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# Nの約数を列挙する: ある約数をaとする
# m = n//a - 1とする
# nをこのmで割ったときに，商と余りが一致してればOK

# ------------------- Answer --------------------
#code:python
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
a = make_divisors(n)
m = [n//i-1 for i in a if i <= n//2]
ans = 0
for i in m:
    q, r = divmod(n, i)
    if q == r:
        ans += i
print(ans)


# ------------------ Sample Input -------------------
8

1000000000000

# ----------------- Length of time ------------------
# 29分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc036/editorial.pdf
# 少し時間がかかってしまったが，解説どおりにとけた
# けんちょんさん: https://drken1215.hatenablog.com/entry/2019/05/12/004500

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ARC-D
#緑diff
#約数
#探索候補を絞る
#全探索
