# ABC103D - Islands War
# URL: https://atcoder.jp/contests/abc103/tasks/abc103_d
# Date: 2021/04/02

# ---------- Ideas ----------
# aとbの差が小さいところから切ったほうがよさそう
# ある辺を切れば，そこをまたがる他の要望はすべて解決できる
# imosで重なりを数える
# 重なりが多い順に辺を切っていって，全部の要望を答えられたらOK?: O(N^2)かかっちゃう

# 区間スケジューリングみたいな貪欲？
# 後ろ側(b)でソートして，now = 0として走査スタート
# aがnowより小さければ，すでにカバーできているのでOK,
# そうでなければ，橋を切る必要があるので，インクリメント


# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    ab.append([a, b])
ab = sorted(ab, key=lambda x: x[1])

now = 0
ans = 0
for a, b in ab:
    if a < now:
        continue
    else:
        ans += 1
        now = b
print(ans)

# ------------------ Sample Input -------------------
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5


9 5
1 8
2 7
3 5
4 6
7 9


# ----------------- Length of time ------------------
# 1時間AC

# -------------- Editorial / my impression -------------
# 最初に区間スケジューリングは思いついたけど詰められそうになかったのでimosで考えはじめてしまった
# 40分くらいたってimosで無理そうなことに気づいて区間スケジュールで考えたら行けた
# N <= 10**5で最大/最小を求める問題は，貪欲の場合が多い？

# ----------------- Category ------------------
#AtCoder
#スケジューリング
#区間スケジューリング
#区間
#区間ソート
#Greedy
#貪欲
#ソートして貪欲
#ABC-D
#水色diff