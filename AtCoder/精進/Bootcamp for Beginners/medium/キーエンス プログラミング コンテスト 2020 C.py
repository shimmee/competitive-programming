# キーエンス プログラミング コンテスト 2020 C - Subarray Sum
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/keyence2020/tasks/keyence2020_c
# 日付: 2020/12/30

# ---------- 思ったこと / 気づいたこと ----------
# アホみたいな問題

# ------------------- 方針 --------------------
# SをK個並べて，残りはS+1でいいやん

# ------------------- 解答 --------------------
#code:python
n, k, s = map(int, input().split())
if s == 10**9:
    ans = [s]*k + [1]*(n-k)
else:
    ans = [s] * k + [s + 1] * (n - k)
for i in ans:
    print(i, end = ' ')

# ------------------ 入力例 -------------------
4 2 3


# ----------------- 解答時間 ------------------
# 10分くらい

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/keyence2020/editorial.pdf
# 凡ミスで数字じゃなくてリスト出力してた
# なんかアホみたいな問題

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#解説AC