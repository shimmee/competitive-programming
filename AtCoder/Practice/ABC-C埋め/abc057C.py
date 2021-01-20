# ABC057C - Digits in Multiplication
# URL: https://atcoder.jp/contests/abc057/tasks/abc057_c
# 日付: 2020/12/10

# ---------- 思ったこと / 気づいたこと ----------
# 約数か√Nで全探索

# ------------------- 方針 --------------------
# 関数Fを定義
# nの約数を列挙
# 約数をループで回してaとする
# nをaで割ったものをbとする
# F(a, b)のminを探す

# ------------------- 解答 --------------------
#code:python
n = int(input())
def F(a, b):
    return max(len(str(a)), len(str(b)))
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

divisors = make_divisors(n)
ans = 10**10
for a in divisors:
    b = n//a
    ans = min(ans, F(a, b))
print(ans)



# ------------------ 入力例 -------------------
10000

1000003

9876543210

# ----------------- 解答時間 ------------------
# 5分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc057/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder #abc
#約数 #√N探索
