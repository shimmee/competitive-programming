# AGC006A - Prefix and Suffix
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc006/tasks/agc006_a
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# iのループを回す
# 新しい文字列 l = sの頭からi文字分 + tの全部
# lが接頭語と接尾語の条件を満たしてれば出力

# ------------------- 解答 --------------------
#code:python
n = int(input())
s = input()
t = input()

for i in range(n+1):
    l = s[:i] + t
    if len(l) >= n:
        if l[:n] == s and l[-n:] == t:
            print(len(l))
            exit()

# ------------------ 入力例 -------------------
3
abc
cde

1
a
z

4
expr
expr

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/agc/006/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#部分文字列
#AGC-A