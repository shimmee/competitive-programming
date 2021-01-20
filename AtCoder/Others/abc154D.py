# ABC154D - Dice in Line
# URL: https://atcoder.jp/contests/abc154/submissions/me
# 日付: 2020/12/09



# ------------------- 方針 --------------------
# k個のサイコロの和の期待値は，各サイコロの期待値の和なので
# まずは各サイコロの期待値を求める = (i*(i+1)/2)/i
# 累積和使う

# ------------------- 解答 --------------------
#code:python
n, k = map(int, input().split())
p = list(map(int, input().split()))
import itertools
(6*7/2)/6
exp = [(i*(i+1)/2)/i for i in p]
cum = [0] + list(itertools.accumulate(exp))
ans = 0
for i in range(1, n+1):
    if i-k >= 0:
        ans = max(ans, cum[i]- cum[i-k])
print(ans)

# ------------------ 入力例 -------------------
5 3
1 2 2 4 5


# ----------------- 解答時間 ------------------
# 5分くらい

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc154/editorial.pdf
# 超単純な累積和

# ----------------- カテゴリ ------------------
#AtCoder #abc
#累積和 #確率論
#期待値
#独立
#事前計算



