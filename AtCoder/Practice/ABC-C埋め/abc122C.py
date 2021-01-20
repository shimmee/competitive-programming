# ABC122C - GeT AC
# URL: https://atcoder.jp/contests/abc122/tasks/abc122_c
# 日付: 2020/11/26

# ---------- 思ったこと / 気づいたこと ----------
# 一番シンプルな累積和

# ------------------- 方針 --------------------
# まずはACの累積和を求める

# ------------------- 解答 --------------------
#code:python
from itertools import accumulate
n,q=map(int, input().split())
s=input()

ac = [0]*n
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        ac[i] = 1
cum = list(accumulate(ac))

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(cum[r]-cum[l])


# ------------------ 入力例 -------------------
8 3
ACACTACG
3 7
2 3
1 8


# ----------------- 解答時間 ------------------
# 6分でAC!!!!

# -------------- 解説 / 感想 / 反省 -------------
# 単純な累積和だった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#累積和
