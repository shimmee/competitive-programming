# ABC089C - March
# URL: https://atcoder.jp/contests/abc089/tasks/abc089_c
# 日付: 2020/12/06

# ---------- 思ったこと / 気づいたこと ----------
# 再帰関数で書きたい
# 頭文字の以外必要ない
# 頭文字がMARCHじゃないやつはいらない
# O(1)か？

# ------------------- 方針 --------------------
# 方針1:
# 組み合わせを全列挙して，同じ文字が入ってる組み合わせは消す

# 方針2:
# O(1)で解く
# 全通りnC3から「同じ2文字+違う1文字を使う場合の数」「同じ3文字使う場合の数」を引く

# ------------------- 解答 --------------------
#code:python
from itertools import combinations
n = int(input())
S = []
for _ in range(n):
    s = input()
    if s[0] in 'MARCH':
        S.append(s[0])

ans = 0
for p in combinations(S, 3):
    if p[0] != p[1] and p[1] != p[2] and p[2] != p[0]:
        ans += 1
print(ans)


# これだとTLE
# 組み合わせの総数が10万C3とかになってる
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input())
keys = ['M', 'A', 'R', 'C', 'H']
values = [0]*5
dict = {key: val for key, val in zip(keys, values)}

cnt = 0 # 入力の頭文字がmarchのものの数
for _ in range(n):
    s = input()
    if s[0] in 'MARCH':
        dict[s[0]] += 1
        cnt += 1
if cnt <= 2: # marchの頭文字をもった入力が2つ以下の場合は何もっできないのでprint0
    print(0)
    exit()

x = list(dict.values())
all_pattern = combinations_count(sum(x), 3) # 全通り

# 3つとも同じ
three = 0
for i in x:
    if i >= 3:
        three += combinations_count(i, 3)

# 2文字が同じ
two = 0
for i in x:
    if i >= 2:
        two += combinations_count(i, 2)*(sum(x)-i)

print(all_pattern-three-two)
# AC!!




# ------------------ 入力例 -------------------
4
ZZ
ZZZ
Z
ZZZZZZZZZZ

5
MASHIKE
RUMOI
OBIRA
HABORO
HOROKANAI

5
CHOKUDAI
RNG
MAKOTO
AOKI
RINGO

# ----------------- 解答時間 ------------------
# 40分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc089/editorial.pdf
# 再帰の問題と聞いて解いてみたら，再帰で書けなかった(実力的に)
# 組み合わせを全通り列挙したらTLEになった
# O(1)で得しかないのでは？

# ----------------- カテゴリ ------------------
#AtCoder #abc
#場合の数 #組み合わせ