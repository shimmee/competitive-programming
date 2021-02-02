# ARC039A - A - B problem
# URL: https://atcoder.jp/contests/arc039/tasks/arc039_a
# Date: 2021/02/01

# ---------- Ideas ----------
# 全探索

# ------------------- Solution --------------------
# aを1桁ずつ回してやつ-b
# a - bを1桁ずつ回したやつ
# これの最大値をキープ

# ------------------- Answer --------------------
#code:python
a, b = input().split()
ans = -1000
for i in range(3): # i桁目
    for j in range(10):
        new = int(a[:i] + str(j) + a[i+1:])
        if new >= 100:
            ans = max(ans, new-int(b))
for i in range(3):  # i桁目
    for j in range(10):
        new = int(b[:i] + str(j) + b[i + 1:])
        if new >= 100:
            ans = max(ans, int(a)-new)
print(ans)

# 解説より，aは各桁を9に置き換えればいいし，bは各桁を0に置き換えればいいだけ
# そんなにコード量変わらないけど...
a, b = input().split()
ans = -1000
for i in range(3): # i桁目
    new = int(a[:i] + str(9) + a[i+1:])
    if new >= 100:
        ans = max(ans, new-int(b))
for i in range(3):  # i桁目
    new = int(b[:i] + str(0) + b[i + 1:])
    if new >= 100:
        ans = max(ans, int(a)-new)
print(ans)

# ------------------ Sample Input -------------------
567 234

999 100

100 999


# ----------------- Length of time ------------------
# 5分AC

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc039
# 解説より，aは各桁を9に置き換えればいいし，bは各桁を0に置き換えればいいだけ
# 他の解答みたけどみんな長さ同じくらい

# ----------------- Category ------------------
#AtCoder
#茶diff
#文字列操作
#桁の入れ替え
#全探索
