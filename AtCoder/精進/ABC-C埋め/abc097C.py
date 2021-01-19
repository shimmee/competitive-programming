# ABC097C - K-th Substring
# URL: https://atcoder.jp/contests/arc097/tasks/arc097_a
# 日付: 2020/12/07

# ---------- 思ったこと / 気づいたこと ----------
# 1<=K<=5がポイント！！

# ------------------- 方針 --------------------
# substringを保管するリストを用意: keep
# a-zまでループで回す: letter
# sの各文字をループで回してletterと一致するなら，その文字から5文字目までをkeepに保管
# keepに要素が5つあればbreak

# ------------------- 解答 --------------------
#code:python
s = input()
k = int(input())

import string
letters = list(string.ascii_lowercase)
cnt = 0
keep = []
for letter in letters:
    for i in range(len(s)):
        if s[i] == letter:
            for j in range(i, min(i+5, len(s))):
                keep.append(s[i:j+1])
    keep = list(set(keep))
    if len(keep) >= 5:
        break
print(sorted(keep)[k-1])

# ------------------ 入力例 -------------------
aba
4

atcoderandatcodeer
5

z
1

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc097/editorial.pdf
# 解答や解説を見た感じ，別にアルファベット順じゃなくても，全5000文字について5文字ずつ取り出したとしても余裕で間に合ってた
# 今回の回答はアルファベット順にやってるから更に早そう

# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列
