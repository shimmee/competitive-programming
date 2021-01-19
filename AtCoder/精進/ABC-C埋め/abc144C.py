# ABC144C - Walk on Multiplication Table
# URL: https://atcoder.jp/contests/abc144/tasks/abc144_c
# 日付: 2020/11/24

# ---------- 思ったこと / 気づいたこと ----------
# 相加相乗平均より2*sqrt(n)-2のceilが答え?

# ------------------- 方針 --------------------
# n=a*bと洗わせる時，答えはa+b-2となる
# nの約数を列挙してn=a*bのa,bの組み合わせを獲得する
# a+b-2の最小を探す

# ------------------- 解答 --------------------
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

n=int(input())
factors = make_divisors(n)
ans = 10**20
for a in factors:
    b = n//a
    ans = min(ans, a+b-2)
print(ans)

# ------------------ 入力例 -------------------
10
50
10000000019



# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc144/editorial.pdf
# √nまでaを全探索するのでよかった。
# 超短く書ける: https://atcoder.jp/contests/abc144/submissions/18016445

# ----------------- カテゴリ ------------------
#AtCoder #abc
#平方根までの全探索
#約数の列挙