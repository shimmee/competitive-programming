# ABC098C - Attention
# URL: https://atcoder.jp/contests/arc098/tasks/arc098_a
# 日付: 2020/12/05

# ---------- 思ったこと / 気づいたこと ----------
# 累積和
# 最終的にはEEE...E(リーダー)WWW...W みたいにしたい

# ------------------- 方針 --------------------
# リーダーをiとして，「iより左にあるWの数＋iより右にあるWの数」が変更する人数
# iを左から右まで動かしてWの数を数えて累積和 と iを右から左まで動かしてEの数を数えて累積和
# リーダーを動かして変更人数が一番小さくなるiを探す


# ------------------- 解答 --------------------
#code:python
from itertools import accumulate
N = int(input())
S = input()

east = [0]*N
west = [0]*N
for i in range(N):
    if S[i] == 'W': east[i] = 1
for i in range(N):
    if S[i] == 'E': west[i] = 1

east = [0] + list(accumulate(east))
west = list(accumulate(west[::-1]))[::-1] + [0]

ans = 10**10
for i in range(N):
    e = east[i-1]
    w = west[i-1]
    ans = min(ans,  e+w)
print(ans)


# ------------------ 入力例 -------------------
2
WE

5
WEEWW

12
WEWEWEEEWWWE

8
WWWWWEEE

# ----------------- 解答時間 ------------------
# 27分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc098/editorial.pdf
# 添字で時間がかかった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#累積和
