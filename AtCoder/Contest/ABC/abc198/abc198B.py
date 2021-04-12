# ABC198B - Palindrome with leading zeros
# URL: https://atcoder.jp/contests/abc198/tasks/abc198_b
# Date: 2021/04/11

# ---------- Ideas ----------
# 回分判定: 判定させた文字列と一致すればOK


# ------------------- Answer --------------------
#code:python
def ispalindrome(str): return True if str == str[::-1] else False
n = input()
flag = False
for i in range(20):
    if ispalindrome('0'*i + n):
        flag = True

print('Yes' if flag else 'No')


# ------------------ Sample Input -------------------
1210
01210


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#回分判定