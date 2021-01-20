# ABC088C - Takahashi's Information
# URL: https://atcoder.jp/contests/abc088/tasks/abc088_c
# 日付: 2020/12/08

# ---------- 思ったこと / 気づいたこと ----------
# 列iと列i+1の差を取ると，同じになってほしい

# ------------------- 方針 --------------------
# flag = Trueを持つ
# 任意の2列(or2行)の要素ごとの差を取って，その結果が同じ値ならOK，異なればflagをFalseにする

# ------------------- 解答 --------------------
#code:python
import numpy as np
c = [[int(i) for i in input().split()] for _ in range(3)]
c = np.array(c)

flag = True
for b in range(2):
        l = c[:,b]-c[:,b+1]
        if len(set(l)) != 1:
            flag = False

for a in range(2):
    l = c[a, :] - c[a + 1, :]
    if len(set(l)) != 1:
        flag = False

if flag: print('Yes')
else: print('No')

# ------------------ 入力例 -------------------
1 0 1
2 1 2
1 0 1

2 2 2
2 1 2
2 2 2

0 8 8
0 8 8
0 8 8

1 8 6
2 9 7
0 7 7

# ----------------- 解答時間 ------------------
# 10分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc088/editorial.pdf
# 解説も多分同じ感じ

# ----------------- カテゴリ ------------------
#AtCoder #abc
#差に注目
