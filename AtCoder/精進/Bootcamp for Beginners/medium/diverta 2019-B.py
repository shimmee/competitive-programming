# diverta 2019 Programming Contest: B - RGB Boxes
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------
#

# ----------------- 方針 --------------------
# rとgのループでbを決める
# bが非負で整数ならOK

# ------------------- 解答 --------------------
#code:python
R, G, B, N = map(int, input().split())

ans = 0
for r in range(N+1):
    for g in range(N-R*r+1):
        b = (N-R*r-G*g)/B
        if b == int(b) and b>=0:
            ans += 1
print(ans)

# ------------------ 入力例 -------------------
1 2 3 4

13 1 4 3000

# ----------------- 解答時間 ------------------
# 10分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/diverta2019/editorial.pdf
# 回答通り

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
