# ABC155C - Poll
# URL:https://atcoder.jp/contests/abc155/tasks/abc155_c
# 日付: 2020/11/24

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# まずは数える: collectionsのcounter
# 最大値を取るものをゲットしてソートして出力


# ------------------- 解答 --------------------
#code:python
from collections import Counter
n = int(input())
s = []
for _ in range(n):
    s.append(input())
dict = Counter(s)
m = max(dict.values())

keys = list(dict.keys())
values = list(dict.values())

l = []
for i in range(len(keys)):
    if values[i] == m:
        l.append(keys[i])

l.sort()
for i in l:
    print(i)


# コードが長すぎるので辞書型を使いこなす必要がある
# 他の人の回答みたけど同じ感じだった。強いて言うならdict.items()として直接for文で回せる
from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
dict = Counter(s)
m = max(dict.values())
ans = []
for key, value in dict.items():
    if value == m:
        ans.append(key)
ans.sort()
print(*ans, sep='\n')


# ------------------ 入力例 -------------------
7
beat
vet
beet
bed
vet
bet
beet


# ----------------- 解答時間 ------------------
# 14分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc155/editorial.pdf
# 解答の方針は解説通りだった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#Counter #itertools
#辞書型 #dictionary
