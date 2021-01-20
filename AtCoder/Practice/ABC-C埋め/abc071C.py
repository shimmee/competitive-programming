# ABC071C - Make a Rectangle
# URL: https://atcoder.jp/contests/arc081/tasks/arc081_a
# 日付: 2020/12/15

# ---------- 思ったこと / 気づいたこと ----------
# 2本以上ある長さの組を探す

# ------------------- 方針 --------------------
# Counterで各長さの出現回数を得る
# 各長さに対して，出現回数が2回以上であれば長方形の辺としてつかえる
# 長方形の辺として使える回数をpairに格納
# pairをソートして，一番長いのと2番目に長いのの積が答え

# ------------------- 解答 --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

import collections
dict = collections.Counter(A)

pair = []
for key, value in dict.items():
    if value >= 2:
        time = value//2
        for _ in range(time):
            pair.append(key)

if len(pair) < 2: print(0)
else:
    log = sorted(pair, reverse=True)
    print(log[0]*log[1])


# ------------------ 入力例 -------------------
6
3 1 2 4 2 1

4
1 2 3 4

10
3 3 3 3 4 4 4 5 5 5

# ----------------- 解答時間 ------------------
# 7分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc081/editorial.pdf
# 解説通りに溶けた

# ----------------- カテゴリ ------------------
#AtCoder #abc
#Counter
