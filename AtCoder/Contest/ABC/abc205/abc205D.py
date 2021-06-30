# ABC205D - Kth Excluded
# URL: https://atcoder.jp/contests/abc205/tasks/abc205_d
# Date: 2021/06/13

# ---------- Ideas ----------
# Aに含まれていなくて，かつK番目に小さい: この答えをidxとする
# idx以下の数字が，Aにはx個含まれてるとすると，idx = x+k
# 含まれていない個数はidx - x
# idxを左にOKの二分探索で動かす: idx以下のAの要素数xを数えて，idx-x < kならOk,
# Aに含まれているidx以下の要素の個数を数えるのにまた二分探索がいる
# 二分探索のなかで二分探索が必要なので，O(N*logA*logN)

# ------------------- Answer --------------------
#code:python
import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    k = int(input())
    ok = 0
    ng = 10**19
    while (abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        x = bisect.bisect_left(a, mid) + 1
        if mid - x < k:
            ok = mid
        else:
            ng = mid
    print(ok)



# ------------------ Sample Input -------------------
1 1
9
10

4 3
3 5 6 7
2
5
3



# ----------------- Length of time ------------------
# 30分？

# -------------- Editorial / my impression -------------
# ngの初期値を間違えてたせいでkiller ケースに殺されて2WA
# 本番で二分探索と


# ----------------- Category ------------------
#AtCoder
#ABC-D
#二分探索
#決め打ちして二分探索