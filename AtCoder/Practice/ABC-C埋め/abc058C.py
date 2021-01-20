# ABC058C - 怪文書
# URL: https://atcoder.jp/contests/abc058/tasks/arc071_a
# 日付: 2020/12/21

# ---------- 思ったこと / 気づいたこと ----------
# ソートしていいやん (する必要なかった)
# 各アルファベットが含まれてる個数の最小値がほしい

# ------------------- 方針 --------------------
# 各SについてCounterで各アルファベットの出現回数を得る
# アルファベットa-zでループを回す
# 各SのCounterの結果をループで回す
# 各アルファベット(letter)が全Sに含まれているminを得る
# このmin分は使用できるということになる
# 使用できる使用できるアルファベットを結合して出力

# ------------------- 解答 --------------------
#code:python
n = int(input())
S = [input() for _ in range(n)]
S = [sorted(i) for i in S]

from collections import Counter
dict_list = [Counter(S[i]) for i in range(n)]

import string
az = list(string.ascii_lowercase)

ans = ''
for letter in az:
    cnt = 10**10
    for dict in dict_list:
        cnt = min(cnt, dict[letter])

    for i in range(cnt):
        ans += letter
print(ans)

# ------------------ 入力例 -------------------
3
cbaa
daacc
acacac

3
a
aa
b

# ----------------- 解答時間 ------------------
# 16分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc071/editorial.pdf
# 解法考えるのに時間かかった。解説通りに溶けた


# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列
#Counter
