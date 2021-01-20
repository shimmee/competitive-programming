# 第二回全国統一プログラミング王決定戦予選B - Counting of Trees
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b
# Date: 2021/01/13


# ---------- Ideas ----------
# Dの最初の要素D[0]が0のみOK，他はだめ
# i=0以外がD[i]==0ならだめ
# 距離1，つまりD[i]=1の頂点iについては，必ず頂点1にくっついてる
# というか一番短い辺の長さのものが頂点1にくっついていることになるかな

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
from collections import Counter
mod = 998244353
n = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
else:
    # 0<iにおいて，D[i]が0のものがあったらダメ
    if any(i == 0 for i in D[1:]):
        print(0)
    else:
        D.sort()
        dict = Counter(D)
        ans = 1
        for key in range(1, len(dict)):
            value1 = dict[key-1]
            value2 = dict[key]
            ans = (ans * (value1**value2)) % mod
        print(ans % mod)


# ------------------ Sample Input -------------------
1
0

2
0 1

4
0 1 1 2

7
0 3 2 1 2 2 1




# ----------------- Length of time ------------------
# 23分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/nikkei2019-2-qual/editorial.pdf

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#場合の数
#無向グラフ
#頂点同士の距離
#木
#tree
