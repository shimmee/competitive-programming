# ABC184B -
# URL: https://atcoder.jp/contests/abc184/tasks/abc184_b
# 日付: 2020/11/22

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python
n, x = map(int, input().split())
s = input()

ans = x
for i in range(n):
    if s[i] == 'x':
        ans = max(0, ans-1)
    else:
        ans += 1
print(ans)
# ------------------ 入力例 -------------------
20 199999
oooooooooxoooooooooo


20 10
xxxxxxxxxxxxxxxxxxxx


# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#
