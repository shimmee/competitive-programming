# ABC172-C: Tsundoku
# URL: https://atcoder.jp/contests/abc172/tasks/abc172_c
# 日付: 2020/11/18

# ---------- 思ったこと / 気づいたこと ----------
# 貪欲に短い本から取っていけばいいんじゃない？

# ------------------- 方針 --------------------
# 貪欲に取っていて，AとBの本が両方なくなるor timeの累積がkを超えたらbreak

# ------------------- 解答 --------------------
#code:python
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


time = 0
ans = 0
A_empty = False
B_empty = False
while True:
    if A == []: # 空になったら大きい本を入れる
        A_empty = True
        A.append(10**11)
    if B == []:
        B_empty = True
        B.append(10**11)

    a = A[0]
    b = B[0]

    # これまでの時間と次読む本がkを超えたら終わり
    if time + min(a, b) > k: # ピッタリでもOKなので>
        break

    if A_empty and B_empty:
        break
    ans += 1
    if a <= b: # aを読む
        time += a
        A.pop(0)
    else:
        time += b
        B.pop(0)
print(ans)

# WAWAWAWA!!!!
# 貪欲じゃ解けないケースがある: 長い本1冊の後に短い本が大量にある場合，ソッチのほうがいいのに，逆の方取っちゃう
# AとBの累積和をもとめて，ai+bj <= Kとなる最大のi+jを求める = しゃくとり法
# bisect使った二分探索でO(NlogN)で解けそう

import itertools
import bisect
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_cum = [0] + list(itertools.accumulate(A))
B_cum = [0] + list(itertools.accumulate(B))

ans = 0
for i in range(len(A_cum)):
    j = bisect.bisect_right(B_cum, k-A_cum[i]) - 1
    if A_cum[i] + B_cum[j] <= k:
        ans = max(ans, i+j)
print(ans)

# ------------------ 入力例 -------------------
3 4 240
60 90 120
80 150 80 150

3 4 730
60 90 120
80 150 80 150

5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000


# ----------------- 解答時間 ------------------
# TLEだしWA
# 解説みて自分でbisect使って書いてみた。

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc172/editorial.pdf
# 解説みたら，貪欲に解いちゃいけないっぽい
# https://torus711.hatenablog.com/entry/2020/06/28/124044
# しゃくとり法っていうらしい: 数列の番号に対する単調増加な性質はしゃくとり法
# 超いい問題
#

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#二分探索 #累積和 #しゃくとり法
#貪欲法で解けない

