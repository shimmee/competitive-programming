# ABC107C - Candles
# URL: https://atcoder.jp/contests/abc107/tasks/arc101_a
# 日付: 2020/11/25

# ---------- 思ったこと / 気づいたこと ----------
# 累積和！

# ------------------- 方針 --------------------
# 一番左のロウソクからの累積和を考える。
# ある地点iまでのK個のロウソクを考えた時，添字はi-k+1からiまでのロウソクとなる。
# このロウソクの累積和を計算してaとする
# 次に，用いるロウソクのなかで，0から一番近いロウソクの座標までの距離をbとする
# aとbの和が移動距離となる

# ------------------- 解答 --------------------
#code:python
n,k = map(int, input().split())
x = list(map(int, input().split()))

# まずは各座標の差を取る
gap = []
for i in range(len(x)-1):
    gap.append(abs(x[i]-x[i+1]))
gap = [0] + gap
# gapの累積和
from itertools import accumulate
cum = list(accumulate(gap))

ans = float('INF')
for i in range(n):
    if i-k+1 >= 0:
        a = cum[i]-cum[i-k+1]
        if x[i]*x[i-k+1] < 0: # もし0をまたいでいるならば
            b = min(-x[i-k+1], x[i])
        elif x[i-k+1] >= 0: # 全部正なら
            b = x[i - k + 1]
        elif x[i] < 0: # 全部負なら
            b = -x[i]
        ans = min(ans, a + b)
print(ans)



# これでACしたけど，全探索が想定解法らしい。つらい。
# 連続したK本を選ぶ
n,k = map(int, input().split())
x = list(map(int, input().split()))

# 訪れる一番左のロウソクをl, 右をrとする
ans = float('INF')
for i in range(n):
    l = i
    r = i+k-1
    if r <= n-1:
        # l->rの順に訪れる場合
        from_l = abs(x[l]) + abs(x[r] - x[l])
        # r->lの順に訪れる場合
        from_r = abs(x[r]) + abs(x[r] - x[l])
        ans = min(ans, from_l, from_r)
print(ans)

# ------------------ 入力例 -------------------
5 3
-40 -15 10 20 60

5 3
-30 -10 10 20 50

1 1
0

3 2
10 20 30

8 5
-9 -7 -4 -3 1 2 3 4


# ----------------- 解答時間 ------------------
# 1時間

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc101/editorial.pdf
# 全く累積和じゃなくて笑った。連続するK本のロウソクを選ぶ全探索でいける

# ----------------- カテゴリ ------------------
#AtCoder #abc
#全探索 #累積和じゃなかった
