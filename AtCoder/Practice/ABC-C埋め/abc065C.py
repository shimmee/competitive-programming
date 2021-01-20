# ABC065C - Reconciled?
# URL: https://atcoder.jp/contests/abc065/tasks/arc076_a
# 日付: 2020/12/20

# ---------- 思ったこと / 気づいたこと ----------
# 犬と猿の数の差が2匹以上だと無理
# n==mのときは犬と猿を交互に並べる: 犬の中で自由に入れ替え可能，猿も。なのでn!*m!，でスタートが犬と猿の2パターンなのでそれ*2
# n=m+1 or m=n+1のときは，スタートが多い方なので2パターンないので，単純にn!*m!



# ------------------- 解答 --------------------
#code:python

mod = 10**9+7
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = (ans*i) % mod
    return ans
n, m = map(int, input().split())
if abs(n-m) > 1:
    print(0)
elif n == m:
    print(factorial(n)*factorial(m)*2 % mod)
elif abs(n-m) == 1:
    print(factorial(n) * factorial(m) % mod)

# ------------------ 入力例 -------------------
2 2
3 2

100000 100000

# ----------------- 解答時間 ------------------
# 10分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc076/editorial.pdf
# 解説通りの正解！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#階乗
#mod
