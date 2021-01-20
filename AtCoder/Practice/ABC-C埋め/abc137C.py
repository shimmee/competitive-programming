# ABC137C - Green Bin
# URL: https://atcoder.jp/contests/abc137/tasks/abc137_c
# 日付: 2020/11/24

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 各文字列をアルファベット順にならべる: 'acdb'は'abcd'に
# カウンターで数える: もし2以上あればペアが存在することになる
# nC2を数えてansにインクリメント

# ------------------- 解答 --------------------
#code:python
from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

for i in range(n):
    S[i] = ''.join(sorted([s for s in S[i]]))

values = list(Counter(S).values())
ans = 0
for value in values:
    if value >= 2:
        ans += value*(value-1)//2
print(ans)




# ------------------ 入力例 -------------------
3
acornistnt
peanutbomb
constraint

2
oneplustwo
ninemodsix

5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa

# ----------------- 解答時間 ------------------
# 18分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc137/editorial.pdf
# 「文字数を数える or 文字列をソートする 2つの方法がある」と書いてて，両方思いついてた
# 他の解答みたけど同じ方法で説いてた


# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列ソート
#itertools #Counter

