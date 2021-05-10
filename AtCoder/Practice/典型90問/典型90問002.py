# 典型90問002 - Encyclopedia of Parentheses
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_b
# Date: 2021/05/09

# ---------- Ideas ----------
# カッコ列の確認はポインタを使って増減させて，一度でも負にならず最後に0になってたらOK
# カッコ列はbit全探索で生成する

# ------------------- Answer --------------------
#code:python
n = int(input())

import itertools
all_pattern = itertools.product([0, 1], repeat=n)
ans = []
for pattern in all_pattern:

    # カッコ列の生成
    s = ''
    for i in range(n):
        if pattern[i] == 1:
            s += '('
        else:
            s += ')'

    # カッコ列の確認
    pointer = 0
    flag = True #
    for i in range(n):
        if s[i] == '(':
            pointer += 1
        else:
            pointer -= 1

        if pointer < 0:
            flag = False
            break

    if flag and pointer == 0:
        ans.append(s)

print(*sorted(ans), sep = '\n')


# ------------------ Sample Input -------------------
4

3

# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# とても好きな問題
# 実際ABCで出たら緑diffくらいありそう

# ----------------- Category ------------------
#AtCoder
#カッコ列
#bit全探索
#構築問題
#典型90問