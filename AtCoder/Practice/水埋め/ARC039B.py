# ARC039B - 高橋幼稚園
# URL: https://atcoder.jp/contests/arc039/tasks/arc039_b
# Date: 2021/04/10

# ---------- Ideas ----------
# こういうのは基本均等に配ればいい
# アメをもらえない子が出ちゃうとき，つまりk//n==0のときは，k個のアメをn人に配る重複組合せをする
# 配れる時は
# とりあえずk個のアメをn人にq個ずつ配って，余りがあればr人がq+1個貰えるようにする
# これは順列の問題で，n! / (q個もらえる人数 !) * (q+1個もらえる人数!)
# 重複組合せ: https://hiraocafe.com/note/kumiwake.html

# ------------------- Answer --------------------
#code:python
def factorial(n):
    cnt = 1
    for i in range(1, n + 1):
        cnt = (cnt * i)
    return cnt

mod = 10**9+7
n, k = map(int, input().split())
if k // n == 0: # 全体の幸福度が0になる -> 重複組合せ
    # k個のあめをn人にくばる
    print(factorial(n+k-1) // (factorial(k) * factorial(n-1)) % mod)
    exit()

# みんなに少なくとも1つずつは配れる時
q, r = divmod(k, n)
n1 = r # 1つ多く貰える人数
n2 = n - r # q個貰える子の人数

print((factorial(n) // (factorial(n1)*factorial(n2))) % mod)


# ------------------ Sample Input -------------------
5 2
4 10

100 450


# ----------------- Length of time ------------------
# 16分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc039
# こういう数え上げ問題は好き
# 今なら茶とか緑diffとかになりそう

# ----------------- Category ------------------
#AtCoder
#重複組合せ
#水diff
#数え上げ問題
#順列
#階乗
#組み合わせ