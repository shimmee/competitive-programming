# ABC185
# URL: https://atcoder.jp/contests/abc185/tasks/abc185_b
# 日付: 2020/12/13

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python

n,m,t = map(int, input().split())
time_out = 0 # 外に出た時間
mah = n
for i in range(m):
    a, b = map(int, input().split())
    mah = mah - (a-time_out)
    # カフェに入る時点で0以下ならだめ
    if mah <= 0:
        print('No')
        exit()
    else:
        # OKなら充電
        mah = min(mah + b-a, n)
        time_out = b

# 最後のカフェを出た
mah = mah - (t-time_out)
if mah <= 0:
    print('No')
    exit()
else:
    print('Yes')





# ------------------ 入力例 -------------------
10 2 20
9 11
13 17

10 2 20
9 11
13 16

15 3 30
5 8
15 17
24 27

20 1 30
20 29

20 1 30
1 10

# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい