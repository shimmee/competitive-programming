# キャディプログラミングコンテスト2021(AtCoder Beginner Contest 193): C - Unexpressed
# URL: https://atcoder.jp/contests/abc193/tasks/abc193_c
# Date: 2021/02/27

# ---------- Ideas ----------
# aを2から√Nまで全探索
# エラトステネスっぽく，a**bがNを超えなくなるまで試す
# 4，8のように1度出現したやつはもう試すべきじゃないので，出現済みをsetで管理
#

# ------------------- Answer --------------------
#code:python
n = int(input())
ans = n
l = set([])
for a in range(2, int(n**0.5)+1):
    if a in l: continue
    b = 2
    while a**b <= n:
        l.add(a**b)
        ans -= 1
        b += 1
print(ans)

# ------------------ Sample Input -------------------
8

20

100

100000

10000000000

# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# aは素数だけ考えればいいじゃん，と思って書いてたけど違った
# 6**2=36みたいなのが飛ばされてしまう。
# 灰diffにしてはちょっと時間がかかりすぎたけどAC

# ----------------- Category ------------------
#AtCoder
#ハッシュテーブル
#O(√N)
#全探索
#エラトステネス風
