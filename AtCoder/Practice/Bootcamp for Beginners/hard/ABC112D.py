# ABC112D - Partition
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc112/tasks/abc112_d
# Date: 2021/01/20

# ---------- Ideas ---------- 
# 一応部分和問題ではある
# 出力するべきgcdは，mの約数でもある必要がありそう
# n=3, m = 14のとき2+4+8=14 -> 2*(1+2+4)=14

# mの約数から，gcdとなる候補を探して，部分和問題におとしこむ
# ただ，m<=10**9なので，実際にdpで部分和問題を解くのは不可能

# ------------------- Solution -------------------- 
# mの約数を列挙
# ある約数をdとしたときに，dの倍数の中からn個とってきて和を取ってmにする。
# n個の要素の和なので，各要素はm//n以下である必要がある
# よって，約数のうちm//n以下のものをピックアップする
# この最大値がサンプルの答えに一致してる

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

n, m = map(int, input().split())

divisors = make_divisors(m)
divisors = [i for i in divisors if i <= m//n]
print(max(divisors))


# ------------------ Sample Input -------------------
3 14

10 123

100000 1000000000


# ----------------- Length of time ------------------
# 14分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc112/editorial.pdf
# なぜこれでACするのかわからなかったが，解説とけんちょん解説を見てわかった
# mの約数のうちm//n以下のもので最大の数字をdとすると，
# d+d+d+d+...+ m-(n-1)*dとすればmが作れる。なのでdだ最大のgcdとなる

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#約数列挙
#整数問題
#最大公約数