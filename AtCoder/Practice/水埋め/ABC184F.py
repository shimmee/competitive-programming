# ABC184F - Programming Contest
# URL: https://atcoder.jp/contests/abc184/tasks/abc184_f
# Date: 2021/04/09

# ---------- Ideas ----------
# ARC017C - 無駄なものが嫌いな人と同じ
# 半分全列挙する
# 半分に分けて，前半と後半でbit全探索して，すべての合計時間を列挙
# 前半の合計時間をt1, 後半をt2としたとき，t1+t2 < Tとなる最大のt1+t2がほしい
# 前半の合計時間t1を走査して，T-t1より小さい合計時間を後半から探す: 二分探索

# ------------------- Answer --------------------
#code:python
import itertools
import bisect
n, T = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) < T: print(sum(a)); exit()

a1 = a[:n//2]
a2 = a[n//2:]

n1 = len(a1)
n2 = len(a2)

l1 = []
l2 = []

all_pattern = itertools.product([0, 1], repeat=n1)
for pattern in all_pattern:
    cnt = 0
    for i in range(n1):
        if pattern[i] == 1:
            cnt += a1[i]
    l1.append(cnt)

all_pattern = itertools.product([0, 1], repeat=n2)
for pattern in all_pattern:
    cnt = 0
    for i in range(n2):
        if pattern[i] == 1:
            cnt += a2[i]
    l2.append(cnt)

l1.sort()
l2.sort()
ans = 0
for t1 in l1:
    if T-t1 < 0:continue
    idx = bisect.bisect_left(l2, T-t1)
    if idx-1 >= 0 and t1 + l2[idx-1] <= T:
        ans = max(ans, t1 + l2[idx-1])
    if 0 <= idx < len(l2) and t1 + l2[idx] <= T:
        ans = max(ans, t1 + l2[idx])
    if idx+1 < len(l2) and t1 + l2[idx+1] <= T:
        ans = max(ans, t1 + l2[idx+1])

print(ans)


# 解けたけど，二分探索がとても汚い
# この人綺麗: https://qiita.com/c-yan/items/71444ba44b927b63c2e0
# こんな感じで書けるらしい

for t1 in l1:
    if T-t1 < 0:continue
    idx = bisect.bisect_left(l2, T-t1 + 1) - 1
    ans = max(ans, t1 + l2[idx])

# ------------------ Sample Input -------------------

6 100
101 102 103 104 105 106

5 17
2 3 5 7 11

7 273599681
6706927 91566569 89131517 71069699 75200339 98298649 92857057

# ----------------- Length of time ------------------
# 15分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc184/editorial
# 最後の二分探索の部分が汚くなった
# 超典型なので身についてよかった

# ----------------- Category ------------------
#AtCoder
#半分全列挙
#ABC-F
#半分全列挙
#探索問題
#部分和
#二分探索
#lower_bound
#数列
#水色diff
#指数探索系問題
#bisect