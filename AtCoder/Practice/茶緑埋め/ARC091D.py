# ARC091D - Remainder Reminder
# URL: https://atcoder.jp/contests/arc091/tasks/arc091_b
# Date: 2021/03/10

# ---------- Ideas ----------
# aとbはK以上になる: a or bがk未満だと，余りは必ずK未満になるから
# bはk+1以上じゃないとだめ: b=kのとき，余りが0になってしまう
# 解法思いついたけど言語化するのが難しい

# ------------------- Solution --------------------
# bを固定するため，k+1からnまで走査する
# あるbについて，a=1,2...,nを割ると，余りは1,2,3,...b-1,0が繰り返される
# この余り1,2,3,...b-1,0はb個の項数であって，k以上のものはb-k個ある。これが繰り返されるわけである
# 1からnをbで割った時のk以上の余りは
# q, r = divmod(n, b)として，(b-k)個がまずq回繰り返しがあって，かつr個の余りの中にr-k+1個あるので，これらの和になる

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())

def mod_cnt(a, b, k): # aをbで割った余りがk以上であるような，aとbの組み合わせ数
    q, r = divmod(a, b)
    cnt = (b-k)*q # q個の繰り返しに含まれるk以上の余りの個数
    cnt += max(r-k+1, 0) # 残りのr個に含まれるk以上の余りの個数
    return cnt

if k == 0:
    print(n**2)
    exit()

ans = 0
for b in range(k+1, n+1):
    ans += mod_cnt(n, b, k)
print(ans)

# ACしたけど
# 短く書ける

n, k = map(int, input().split())
if k == 0:
    print(n**2)
    exit()

ans = 0
for b in range(k+1, n+1):
    q, r = divmod(n, b)
    ans += (b - k) * q  # q個の繰り返しに含まれるk以上の余りの個数
    ans += max(r - k + 1, 0)  # 残りのr個に含まれるk以上の余りの個数
print(ans)


# ------------------ Sample Input -------------------
5 2

10 0

31415 9265


# ----------------- Length of time ------------------
# 32分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc091/editorial.pdf
# 解説通り解けたあああああああああああ
# 前考えた時ても足も出なかったのでとても嬉しい
# 整数問題の数え上げは，表を描いてみると規則が見えることがある
# 結構好きな問題だった


# ----------------- Category ------------------
#AtCoder
#整数問題
#表を描いて規則を見つける
#余り
#実験
#