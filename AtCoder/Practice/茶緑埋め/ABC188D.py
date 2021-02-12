# ABC188D - Snuke Prime
# URL: https://atcoder.jp/contests/abc188/tasks/abc188_d
# Date: 2021/02/11

# ---------- Ideas ----------
# imos法で解きたいが，日数が10**9あるので，imos配列を持てないし，累積和も取れない
# 利用するサービスは最大10**5個なので，imos配列があったとしても，埋める要素の数は10**5*2 (aとbが10**5分)
# 2*10**5の配列に座標圧縮すれば，なんとか入れられる
# aとbを混ぜてソートして順番をつける (座標圧縮)
# 圧縮したimos配列にa,bごとに処理していく

# ------------------- Answer --------------------
#code:python
from scipy.stats import rankdata
from itertools import accumulate
n, C = map(int, input().split())
abc = [[int(i) for i in input().split()] for _ in range(n)]
l = [i[0] for i in abc] + [i[1] for i in abc] # aとbを混ぜた集合
l.sort()

# aとbを混ぜた配列lを座標圧縮し，lとrankを対応付ける辞書を用意
rank = rankdata(l, method='dense')  # 色々methodあるけどdense
ab_to_rank = {key: val for key, val in zip(l, rank)}
rank_to_ab = {key: val for key, val in zip(rank, l)}

ab_to_rank.update({0:0})
rank_to_ab.update({0:0})

# いもす法
imos = [0] * (max(rank)+2)
for a, b, c in abc:
    a_rank = ab_to_rank[a]
    b_rank = ab_to_rank[b]
    imos[a_rank] += c
    imos[b_rank+1] -= c
cum = list(accumulate(imos))
cum.pop()

# 圧縮したのを戻す
ans = 0
for i in range(1, len(cum)): # インデックスiはrankを表している
    if cum[i] >= C: # プライム月額より高ければ，Cを払う
        ans += C*(rank_to_ab[i + 1] - rank_to_ab[i])
    else:
        ans += cum[i] * (rank_to_ab[i + 1] - rank_to_ab[i])

print(ans)


# Give up
# この人とほぼ同じことしてるのに...: https://cocoinit23.com/abc188/
# これを参考にしてみる: https://medium.com/@kevinrobot34/abc188-cc47b27f949d
# この人の言うところのzippedがab_to_rank，unzippedがrank_to_ab

def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=None, reverse=reverse)):
        zipped[xi] = i
        unzipped[i] = xi
    return zipped, unzipped

from itertools import accumulate
n, C = map(int, input().split())
ab = []
abc = []
for _ in range(n):
    a,b,c = map(int, input().split())
    ab.append(a)
    ab.append(b+1) # 半開区間でもつ
    abc.append([a,b,c])

zipped, unzipped = compress_coordinate(ab)

# いもす法
imos = [0] * len(zipped)
for a, b, c in abc:
    imos[zipped[a]] += c
    imos[zipped[b+1]] -= c
cum = list(accumulate(imos))

# 圧縮したのを戻す
ans = 0
for i in range(len(cum)-1):
    cost = min(C, cum[i])
    ans += cost*(unzipped[i + 1] - unzipped[i])
print(ans)

##########################################################
# 想定解法: イベントソート
# https://atcoder.jp/contests/abc188/editorial
##########################################################

N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))
event.sort()
ans = 0
fee = 0
t = 0
for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y
print(ans)

# ------------------ Sample Input -------------------
5 8
1 5 3
3 7 4
3 5 2
5 11 3
10 10 6

4 5
1 2 3
2 4 2
3 7 4
8 8 7

2 6
1 2 4
2 2 4


5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409


# ----------------- Length of time ------------------
# 1時間頑張って惜しいところまでいった
# imosの添字，半開区間などの添字でバグって解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc188/editorial
# バグりまくって辛かった。
# 1日ずらすという謎の操作が必要だった。
# バグらせないために半開区間への理解が必要である...

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#イベントソート
#座標圧縮
#imos
#いもす法
