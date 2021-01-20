# 第一回日本最強プログラマー学生選手権-予選- B - Kleene Inversion
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b
# Date: 2021/01/11

# ---------- Ideas ----------
# O(N^2)で解く
# 同じグループ内を数える + 異なるグループ内を数える
# グループ内でAi > Ajとなる個数を数えて，それはk*(k+1)//2分ある
# グループ内でAi < Ajとなる個数を数えて，それはk*(k-1)//2分ある

# ------------------- Solution --------------------
# 1. Ai > Ajとなるものを数えてK倍
# 2. Ai < Ajとなるものは1+2+...(k-1)回

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n, k = map(int, input().split())
a = list(map(int, input().split()))
k1 = k*(k+1)//2
k2 = k*(k-1)//2


ans = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]: # 1. Ai > Ajとなるものを数えてK倍
            ans = (ans + k1) % mod
        elif a[i] < a[j]: # 2. Ai < Ajとなるものは1+2+...(k-1)回
            ans = (ans + k2) % mod
print(ans)


# ------------------ Sample Input -------------------
2 2
2 1

3 5
1 1 1

10 998244353
10 9 8 7 5 6 3 4 2 1

# ----------------- Length of time ------------------
# 17分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/jsc2019-qual/editorial.pdf
# 実験したら思い浮かぶ系の問題
# やたら難しいらしいけどスムーズに溶けた
# fenwick tree (BIT)でも解けるらしい: https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2019-08-25jsc2019%E4%BA%88%E9%81%B8
# 愚直に全探索で二重ループだとO(N^2)だが，BITならO(nlogn)でとける
# 転倒数は、「数列を、隣り合う要素をswapすることで昇順にソートする時、必要なswap回数」という意味を持つ: https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2019/0824_jsc2019_qual

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#転倒数
#バブルソート
