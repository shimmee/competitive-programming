# ABC028D - 乱数生成
# URL: https://atcoder.jp/contests/abc028/tasks/abc028_d
# Date: 2021/02/18

# ---------- Ideas ----------
# 全通り: n**3
# 3つの中に中央値kは必ず含まれる
# 取り方1: (k, k, k) -> 1パターン
# 取り方2: (k-i, k, k+j) -> 6パターン
# 取り方3: (k, k, k+i) -> 3パターン
# 取り方4: (k-i, k, k) -> 3パターン


# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())

p_all = n**3
p1 = 1
p2 = (n-k)*(k-1)*6
p3 = (n-k)*3
p4 = (k-1)*3
print((p1 + p2 + p3 + p4)/p_all)

# ------------------ Sample Input -------------------
10 4

3 2

765 573


# ----------------- Length of time ------------------
# 13分AC

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/abc028
# ただの数え上げだった
# 解説通りに溶けた

# ----------------- Category ------------------
#AtCoder
#確率
#中央値
#乱数
#数え上げ問題