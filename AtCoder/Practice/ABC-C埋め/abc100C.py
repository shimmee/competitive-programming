# ABC100C - C - *3 or /2
# URL: https://atcoder.jp/contests/abc100/tasks/abc100_c
# 日付: 2020/11/27

# ---------- 思ったこと / 気づいたこと ----------
# 各整数を2で割れる回数の総和が答え

# ------------------- 方針 --------------------
# 各整数を素因数分解して，2の素因数の個数をインクリメント

# ------------------- 解答 --------------------
#code:python
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
def prime_factorize(n: int):
    # 試し割り法による素因数分解
    # https://en.wikipedia.org/wiki/Trial_division
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3 # 奇数でどんどん割っていって，素数を探す。
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f # nをfで割って減らす。
        else:
            f += 2 # 奇数なので+2ずつ足していく。
    if n != 1: factors.append(n)
    # Only odd number is possible
    return factors

ans = 0
for i in range(n):
    ans += Counter(prime_factorize(a[i]))[2]
print(ans)



# ------------------ 入力例 -------------------
10
2184 2126 1721 1800 1024 2528 3360 1945 1280 1776

# ----------------- 解答時間 ------------------
# 5分

# -------------- 解説 / 感想 / 反省 -------------
# 簡単〜

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
