# ABC098B - Cut and Count
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc098/tasks/abc098_b
# 日付: 2020/12/28


# ------------------- 方針 --------------------
# 半分に切る場所をループして変えていく
# 各アルファベットが両方に入ってたらインクリメント

# ------------------- 解答 --------------------
#code:python
n = int(input())
S = input()

import string
abc = list(string.ascii_lowercase)

ans = 0
for i in range(1, n):
    s1 = S[:i]
    s2 = S[i:]
    cnt = 0
    for letter in abc:
        if letter in s1 and letter in s2:
            cnt += 1
    ans = max(ans, cnt)
print(ans)

# ------------------ 入力例 -------------------
6
aabbca

10
aaaaaaaaaa

45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir

# ----------------- 解答時間 ------------------
# 3分

# -------------- 解説 / 感想 / 反省 -------------
#  https://img.atcoder.jp/arc098/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#アルファベット
#ABC-B