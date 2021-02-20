# ABC014B - 価格の合計
# URL: https://atcoder.jp/contests/abc014/tasks/abc014_2
# Date: 2021/02/18

# ---------- Ideas ----------
# ビットが立っている商品のときだけ価格をインクリメント


# ------------------- Answer --------------------
#code:python
n, x = map(int, input().split())
A = list(map(int, input().split()))

x = bin(x)[2:].zfill(n)[::-1]
ans = 0
for i in range(n):
    if x[i] == '1':
        ans += A[i]
print(ans)

# bitの書き方を活かしたのがこれ: https://atcoder.jp/contests/abc014/submissions/3127866
n, x = map(int,input().split())
a = list(map(int,input().split()))
print(sum([a[i] for i in range(n) if x & (1 << i)]))

# ------------------ Sample Input -------------------
4 5
1 10 100 1000

20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/abc014
# bit演算不得意なのが丸見えな解答なので，復讐したい
# xのi桁目にbitが立っているかどうか: if x & (1 << i)

# ----------------- Category ------------------
#AtCoder
#bit演算
#復讐したい
#ABC-B
#茶diff