# ARC035B - アットコーダー王国のコンテスト事情
# URL: https://atcoder.jp/contests/arc035/tasks/arc035_b
# Date: 2021/02/12

# ---------- Ideas ----------
# 小さい方から貪欲に解くのがベスト
# 同じ点数の問題があれば，それらは順番を変えてもOK

# ------------------- Solution --------------------
# ソートする
# 累積和の累積和が答え
# 点数の出現回数をCounterして，入れ替えてOKなので，階乗する。

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
from itertools import accumulate
from collections import deque, Counter
n = int(input())
a = sorted([int(input()) for _ in range(n)])

print(list(accumulate(accumulate(a)))[-1])

def factorial_mod(n):
    cnt = 1
    for i in range(1, n + 1):
        cnt = (cnt * i) % mod
    return cnt
d = Counter(a)
ans = 1
for key, value in d.items():
    ans = ans*factorial_mod(value) % mod
print(ans)

# ------------------ Sample Input -------------------
5
2
1
2
1
2


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc035
# 解けた！
# 問題に2つの要素があって面白かった
# 累積和と階乗modの教育的な良い問題。

# ----------------- Category ------------------
#AtCoder
#階乗
#Counter
#累積和
#ソート
#貪欲
#ソートして貪欲
#greedy




