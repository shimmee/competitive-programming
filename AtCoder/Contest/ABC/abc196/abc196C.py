#
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
m = len(str(n))
ans = 0
for i in range(1, m//2+1):
    if int(str(9)*i*2) <= n:
        ans += 9*(10**(i-1))
    else:
        p = min(int(str(n)[:i]), int(str(n)[i:]))

        ans += max(0, p - 10**(i-1)+1)
print(ans)



n = int(input())
ans = 0
for i in range(7):
    if 10**(2*i+1) < n:
        if n <= 10**(2*i+2)-1:
            q, r = divmod(n, 10**(i+1))
            if r < q:
                q -= 1
            ans += (q - max(0, (10**i-1)))
        else:
            ans += 9*(10*i)
print(ans)

# 30分くらい解いてたけど本番間に合わなかった。
# ABDの3完になっちゃった

n = int(input())
ans = 0
for i in range(1, 10**6+1):
    if int(str(i)*2) <= n:
        ans += 1
print(ans)



# ------------------ Sample Input -------------------
33

1333

10000000



# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
