# ARC026B - 完全数
# URL: https://atcoder.jp/contests/arc026/tasks/arc026_2
# Date: 2021/02/04

# ---------- Ideas ---------- 
# 約数列挙してsumとって判定するだけ

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
d = make_divisors(n)
d.pop()
if sum(d) == n:
    print('Perfect')
elif sum(d) > n:
    print('Deficient')
else: print('Abundant')

# ------------------ Sample Input -------------------
6

# ----------------- Length of time ------------------
# 2分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc026
# 昔は約数列挙するだけでdif1199もあったんだ

# ----------------- Category ------------------
#AtCoder  
#約数列挙
#ARC-B
#緑diff
