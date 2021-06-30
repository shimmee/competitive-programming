# 典型90問052 - Dice Product（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_az
# Date: 2021/05/27

# ---------- Ideas ----------
# シグマを因数分解するやつ: https://www.google.com/search?q=%E7%AB%B6%E3%83%97%E3%83%AD+%E3%82%B7%E3%82%B0%E3%83%9E+%E5%B1%95%E9%96%8B&oq=%E7%AB%B6%E3%83%97%E3%83%AD+&aqs=chrome.0.69i59j69i57j69i61l3j69i65l3.3000j0j7&sourceid=chrome&ie=UTF-8
# これとおなじ: https://atcoder.jp/contests/arc107/tasks/arc107_a


# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n = int(input())
ans = 1
for _ in range(n):
    a = list(map(int, input().split()))
    ans = ans*sum(a) % mod
print(ans)


# ------------------ Sample Input -------------------
7
19 23 51 59 91 99
15 45 56 65 69 94
7 11 16 34 59 95
27 30 40 43 83 85
19 23 25 27 45 99
27 48 52 53 60 81
21 36 49 72 82 84

# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# 数弱で最初全然思いつかなかってしばらく考えた
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/052.jpg

# ----------------- Category ------------------
#AtCoder
#因数分解
#典型90問