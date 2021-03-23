# ABC152D - Handstand 2
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc152/tasks/abc152_d
# Date: 2021/01/26

# ---------- Ideas ----------
# 10**5なのでO(N^2)は無理。
# 1で始まる数*1で終わる数 + 2で始まる数*2で終わる数 + ... + 9で始まる数*9で終わる数
# 違った。誤読してた。でも近い
# 「1で始まって2で終わる数 * 2で始まって1で終わる数」みたいなのを全部数えて掛け算する
# 先頭と末尾を固定して数え上げる

# ------------------- Answer --------------------
#code:python
n = int(input())

all_integer = [i for i in range(1, n+1)]

table = [[0]*10 for i in range(10)]

ans = 0
for i in range(1, 10): # 先頭
    for j in range(1, 10): # ケツ
        cnt = len([k for k in all_integer if str(k)[0] == str(i) and str(k)[-1] == str(j)])
        table[i][j] = cnt

ans = 0
for i in range(1, 10): # 先頭
    for j in range(1, 10): # ケツ
        ans += table[i][j] * table[j][i]
print(ans)


# ------------------ Sample Input -------------------
"""
25
"""



# ----------------- Length of time ------------------
# 15分AC

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/code-festival-2017-qualc/editorial.pdf
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/01/22/114900

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ABC-D
#先頭と末尾を固定して数え上げる
#数え上げ問題
#緑diff