# ABC067C - Splitting Pile
# URL: https://atcoder.jp/contests/abc067/tasks/arc078_a
# 日付: 2020/12/20

# ---------- 思ったこと / 気づいたこと ----------
# 単純な累積和

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(abs(a[0]-a[1]))
    exit()

from itertools import accumulate
cum = [0] + list(accumulate((a)))

ans = float('INF')
for i in range(1, n-1): # すぬけが取るカードの枚数
    x = cum[i]
    y = cum[n] - cum[i]
    ans = min(ans, abs(x-y))

print(ans)

# ------------------ 入力例 -------------------
6
1 2 3 4 5 6

2
10 -10

# ----------------- 解答時間 ------------------
# 7分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc078/editorial.pdf
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#累積和
