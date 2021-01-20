# ABC094C - Many Medians
# URL: https://atcoder.jp/contests/abc094/tasks/arc095_a
# 日付: 2020/12/05

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# xをソートして，中央値2つlowerとupperをゲット
# lowerより小さいxを除いたときはupperが中央値に
# それの逆

# ------------------- 解答 --------------------
#code:python
n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(x)
lower = x_sort[n//2-1]
upper = x_sort[n//2]

for i in x:
    if i <= lower:
        print(upper)
    elif i >= upper:
        print(lower)


# ------------------ 入力例 -------------------
1
4

4
2 4 4 3

6
5 5 4 4 3 3

# ----------------- 解答時間 ------------------
# 9分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc095/editorial.pdf
# 解説通りに解けた

# ----------------- カテゴリ ------------------
#AtCoder #abc
#中央値
