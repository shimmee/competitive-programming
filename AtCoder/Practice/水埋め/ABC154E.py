# ABC154E - Almost Everywhere Zero
# URL: https://atcoder.jp/contests/abc154/tasks/abc154_e
# Date: 2021/04/12

# ---------- Ideas ----------
# 基本は組み合わせ計算で解けそう: 桁数をpとしたとき，p桁からk桁選ぶ，みたいな
# 3つに場合分けする
# n=314159のとき
# (1) 1から099999まで: p-1桁までの処理
# (2) 100000から299999まで: p桁のうち，最高桁が1つ小さい数字まで
# (3) 300000から314159まで: p桁のうち，最高桁がそのままで，nまでの数字

# ------------------- Solution --------------------
# (1)はp-1Ck * 9**k
# (2)はp-1Ck-1 * 9**(k-1) * (最高桁の数字-1)
# (3)は組み合わせ全探索で最高桁以外の桁を全列挙

# ------------------- Answer --------------------
#code:python
from operator import mul
from functools import reduce
from itertools import combinations, product

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n = int(input())
k = int(input())

p = len(str(n))
ans = 0

# 桁が小さい時はそのまま処理
if n < 10**5:
    for i in range(1, n+1):
        if len(str(i)) - str(i).count('0') == k:
            ans += 1
    print(ans)
    exit()


# (1) p-1桁までの処理
ans += cmb(p-1, k) * 9**k

# p桁の処理
p1 = str(n)[0] # 最高桁

# (2) 最高桁がp1より1小さいパターン：n=5435であれば, p1=5で，ここでは4999と1000の間のokなやつを数える
ans += cmb(p-1, k-1) * 9**(k-1) * (int(p1)-1)

# (3) 最高桁がp1の場合，全列挙する
# 最高位は固定して，k−1個のポジションに何かしらの数を入れる
# k-1個のポジションはcombinations()で，何かしらの数字はproductで
for comb in list(combinations(range(1, p), k-1)):
    digits = [p1] + ['0'] * (p - 1)
    for prod in list(product([str(j) for j in range(1, 10)], repeat=k - 1)):
        for i in range(k-1):
            digits[comb[i]] = prod[i]
        num = int(''.join(digits))
        if num <= n:
            ans += 1

print(ans)

# ------------------ Sample Input -------------------
25
2

9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3

100
1

314159
2


# ----------------- Length of time ------------------
# 40分くらい?

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc154/editorial.pdf
# 桁DPで解く問題だったらしい: O(桁数*K)
# 今回は最高桁の場合だけ全列挙したが，100桁C(k-1)がぎりぎり間に合う時間制限だったのでなんとかなった
# この人の解答とほぼ同じ: https://at274.hatenablog.com/entry/2020/02/17/060000


# ----------------- Category ------------------
#AtCoder
#ABC-E
#桁DP
#数え上げ問題
#leadingzero
#再帰的構造に着目する
#二項係数
#水色diff
#DP
#制約条件:K以下
#組み合わせ計算
#場合分け


