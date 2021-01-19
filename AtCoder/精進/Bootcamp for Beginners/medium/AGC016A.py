# AGC016A - Shrinking
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc016/tasks/agc016_a
# 日付: 2020/12/30

# ---------- 思ったこと / 気づいたこと ----------
#
1209 1217
# ------------------- 方針 --------------------
# 一番多い文字からどれだけ離れてるか

# ------------------- 解答 --------------------
#code:python
S = input()
from collections import Counter
dict = Counter(S)
candidate = []
for key, value in dict.items():
    if value == max(dict.values()):
        candidate.append(key)

ans = 10**10
for letter in candidate:
    dist = 0
    max_dist = 0
    for s in S:
        if s == letter:
            dist = 0
        else:
            dist += 1
        max_dist = max(max_dist, dist)

    ans = min(ans, max_dist)
print(ans)

# 3/14WA

# 解説: https://img.atcoder.jp/agc016/editorial.pdf
# アルファベットを固定するらしい。よくわからん
# 他の人の解答: Sの各文字でSをsplitして，splitした各部分の長さのmaxを得てる
# やってること一緒やんけ!!!!
# いや，S = aaaabbbccccccbbbbblllllllllのときは答えが違った。
# 問題をちゃんと理解してなかった。
S = input()

ans = 100
for s in S:
    l = list(map(len, S.split(s)))
    ans = min(ans, max(l))
print(ans)


# ------------------ 入力例 -------------------
ab

aaaabbbccccccbbbbblllllllll

serval

jackal

zzz


whbrjpjyhsrywlqjxdbrbaomnw


# ----------------- 解答時間 ------------------
# 解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://drken1215.hatenablog.com/entry/2020/04/09/020800
# https://img.atcoder.jp/agc016/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#解説AC #medium復習
#文字列