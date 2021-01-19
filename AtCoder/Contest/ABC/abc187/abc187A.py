# ABC187A - Large Digits
# URL: https://atcoder.jp/contests/abc187/tasks/abc187_a
# Date: 2021/01/02

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

a, b = map(int, input().split())
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

print(max(digitSum(a), digitSum(b)))



# ------------------ Sample Input -------------------
123 234

100 999


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ABC187
#ABC-A
#AC_with_editorial #解説AC
