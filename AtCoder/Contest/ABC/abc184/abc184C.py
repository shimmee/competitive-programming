# ABC184C -
# URL: https://atcoder.jp/contests/abc184/tasks/abc184_c
# 日付: 2020/11/22

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

x = abs(r1-r2)
y = abs(c1-c2)

if r1 == r2 and c1 == c2:
    print(0)
    exit()
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1-r2)+abs(c1-c2) <= 3:
    print(1)
    exit()
elif abs(r2 - r1) % 2 == abs(c2 - c1) % 2 or abs(r1-r2)+abs(c1-c2) <= 6 or abs(x-y) <= 3:
    print(2)
    exit()
else:
    print(3)
    exit()




# ------------------ 入力例 -------------------
1 1
5 6

1 1
1 200001

2 3
998244353 998244853

1 1
1 1


# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#
