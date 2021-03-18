# ABC195C - Comma
# URL: https://atcoder.jp/contests/abc195/tasks/abc195_c
# Date: 2021/03/13

# ---------- Ideas ----------
# comma1つ: 1000から999999: 10**3から10**6-1
# comma2つ: 1000000から999999999: 10**6から10**9-1
# commma5つまであり得るから，これをループで書く

# ------------------- Answer --------------------
#code:python
n = int(input())
ans = 0

for i in range(1, 6):
    lower = 10**(3*i)
    upper = 10**(3*i+3)-1
    if lower <= n:
        ans += (min(n, upper) - lower + 1)*i
print(ans)

# ------------------ Sample Input -------------------
1010

27182818284590


# ----------------- Length of time ------------------
# 15分?

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc195/editorial
# バグって大変だった

# ----------------- Category ------------------
#AtCoder
#ABC-C


if 1 <= n <= 10**3-1:
    print(0)
elif 10**3 <= n <= 10**6-1:
    print(n-10**3+1)
elif 10**6 <= n <= 10**9-1:
    print((10**6 - 10**3) +
          (n - 10 ** 6 + 1) * 2)
elif 10**9 <= n <= 10**12-1:
    print((10 ** 6 - 10 ** 3) +
          (10 ** 9 - 10 ** 6) * 2 +
          (n - 10 ** 9 + 1) * 3)
elif 10**12 <= n <= 10**15-1:
    print((10 ** 6 - 10 ** 3) +
          (10 ** 9 - 10 ** 6) * 2 +
          (10 ** 12 - 10 ** 9) * 3 +
          (n - 10 ** 12 + 1) * 4)
else:
    print((10 ** 6 - 10 ** 3) +
          (10 ** 9 - 10 ** 6) * 2 +
          (10 ** 12 - 10 ** 9) * 3 +
          (10 ** 15 - 10 ** 12) * 4 +
          1)