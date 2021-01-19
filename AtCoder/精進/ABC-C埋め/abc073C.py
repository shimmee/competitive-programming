# ABC073C - Write and Erase
# URL: https://atcoder.jp/contests/abc073/tasks/abc073_c
# 日付: 2020/11/29

# ---------- 思ったこと / 気づいたこと ----------
# 各数字の出現回数が偶数ならば紙にないし，奇数ならある

# ------------------- 方針 --------------------
# 各数字の出現回数をカウントする

# ------------------- 解答 --------------------
#code:python
n = int(input())
A = [int(input()) for _ in range(n)]
from collections import Counter
dict = Counter(A)
values = list(dict.values())
ans = 0
for i in values:
    if i % 2:
        ans += 1
print(ans)
# ------------------ 入力例 -------------------
3
6
2
6

4
2
5
5
2

6
12
22
16
22
18
12


# ----------------- 解答時間 ------------------
# 6分AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc073/editorial.pdf
# 簡単だった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#偶奇に注目
#Counter