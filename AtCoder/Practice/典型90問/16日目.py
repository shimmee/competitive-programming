# 典型90問 - 16日目
# URL: https://github.com/E869120/kyopro_educational_90/blob/main/problem/016.jpg
# Date: 2021/04/15

# ---------- Ideas ----------
# Otoshidamaとほぼ同じ問題
# a円，b円，c円をそれぞれx枚，y枚，z枚としたとき
# a*x + b*y + c*z = n となるので，xとyをループで固定して方程式を満たすか調べればよい
# 硬貨の枚数は合計で9999以下なので，ループの上限は10000。これを二重でやる


# ------------------- Answer --------------------
#code:python


# a円，b円，c円をそれぞれx枚，y枚，z枚としたとき
# a*x + b*y + c*z = n となるので，xとyをループで固定して方程式を満たすか調べればよい
n = int(input())
a,b,c = map(int, input().split())

ans = 10**10
for x in range(10000): # A円の個数
    for y in range(10000-x): # B円の個数
        cz = n - a*x - b*y #
        if cz >= 0 and cz % c == 0:
            z = cz // c
            ans = min(ans, x+y+z)
        elif cz < 0:
            break
print(ans)


# ------------------ Sample Input -------------------
227
21 47 56

9999
1 5 10

998244353
314159 265358 97932

100000000
10001 10002 10003
# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# 1億回ループになっちゃうけど良いの？手元だと10秒くらいかかるよ？
# pypyでコードテストしたら余裕で間に合った

# ----------------- Category ------------------
#AtCoder
#全探索
#工夫する全探索