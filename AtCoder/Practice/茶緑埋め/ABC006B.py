# ABC006B - トリボナッチ数列
# URL: https://atcoder.jp/contests/abc006/tasks/abc006_2
# Date: 2021/02/01

# ---------- Ideas ----------
# ループで書こう


# ------------------- Answer --------------------
#code:python
mod = 10007
n = int(input())
a = [0, 0, 1]
for i in range(3, n):
    a.append((a[i-1] + a[i-2] + a[i-3])%mod)
print(a[n-1])

# ----------------- Length of time ------------------
# 2分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/abc006
# フィボナッチみたいなのは再帰で描くよりfor文で書いたほうが絶対楽

# ----------------- Category ------------------
#AtCoder
#フィボナッチ
#トリボナッチ
