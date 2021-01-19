# CODE FESTIVAL 2017 Final: B - Palindrome-phobia
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b
# 日付: 2020/12/30

# ---------- 思ったこと / 気づいたこと ----------
# 文字の種類数えてなんかすればいけそう

# ------------------- 方針 --------------------
# a,b,cが出てくる回数をカウント
# 一番多い数-一番少ない数が2以上差があるとだめ!!
# nが1と2は例外処理

# ------------------- 解答 --------------------
#code:python

S = input()
n = len(S)
counter = [0]*3
for s in S:
    if s == 'a': counter[0] += 1
    elif s == 'b': counter[1] += 1
    elif s == 'c': counter[2] += 1

max_value = max(counter)
min_value = min(counter)

if n == 1:
    print('YES')
elif n == 2:
    if max_value == 2:
        print('NO')
    else:
        print('YES')
else:
    if max_value - min_value < 2:
        print('YES')
    else:
        print('NO')




# ------------------ 入力例 -------------------
abac

aba

babacccabab

# ----------------- 解答時間 ------------------
# 23分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/cf17-final/editorial.pdf
# 気づくまでにかなり実験した。
# 気づいたのも奇跡のよう

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium