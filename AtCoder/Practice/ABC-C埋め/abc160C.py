# ABC160C - Traveling Salesman around Lake
# URL: https://atcoder.jp/contests/abc160/tasks/abc160_c
# 日付: 2020/11/23


# ------------------- 方針 --------------------
# 一番距離が離れている家同士を探す。
# もしK/2より小さかったら離れている家の手前の家から時計回り，
# K/2より大きかったら手前の家から反時計回り

# ------------------- 解答 --------------------
#code:python
k, n = map(int, input().split())
a = list(map(int, input().split()))

d = []
for i in range(n-1):
    d.append(a[i+1]-a[i])

d_max = max(d)
s = d.index(d_max) # start
if d_max < k/2:
    print(sum(d))
else:
    new_a = a[:s+1] + [i-k for i in a[s+1:]]
    new_a.sort()
    dist = 0
    for i in range(n - 1):
        dist += abs(new_a[i + 1] - new_a[i])
    print(dist)


# WAが多いので解法が間違ってる?
# 解説みたら方針はあってそう
# 円のうち通らないのは一番長い辺なので，長い辺を引けばいい

k, n = map(int, input().split())
a = list(map(int, input().split()))

dist = 0
for i in range(n - 1):
    dist = max(dist, a[i + 1] - a[i])
dist = max(dist, k-a[-1]+a[0])

print(k-dist)


# ------------------ 入力例 -------------------
20 3
5 10 15


20 3
0 5 15


# ----------------- 解答時間 ------------------
# 30分以上？

# -------------- 解説 / 感想 / 反省 -------------
# 簡単なはずなのに思いつかなかったから諦めた

# ----------------- カテゴリ ------------------
#AtCoder #abc
#円周
