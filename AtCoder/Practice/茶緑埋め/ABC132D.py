# ABC132D - Blue and Red Balls
# URL: https://atcoder.jp/contests/abc132/tasks/abc132_d
# Date: 2021/03/02

# ---------- Ideas ----------
# 各iについて3つのステップで計算する
# (1). 青をi個に分割して，かたまりとして見る: S = (k-1)C(i-1)
# (2). i個の青と(n-k)個の赤を隣り合わないように並べる: T = (n-k+1)C(i)
# (3). S*T % mod を出力する
# (2)について高校生クイズでみた方法: https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1018972540
# i個の青と(i-1)個の赤を交互にまず並べて，そのあと残りの(n-k-i+1)個の赤をその間に入れる


# ------------------- Answer --------------------
#code:python
mod = 10**9+7
def combination(n, r, mod=10**9+7):
    # n<=10**9, r<=10**6 で使用可能
    p, q = 1, 1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p * pow(q,mod-2,mod) % mod

n, k = map(int, input().split())

for i in range(1, k+1):
    S = combination(k-1, i-1)
    T = combination(n-k+1, i)
    print(S * T % mod)

# ------------------ Sample Input -------------------
5 3

2000 3


# ----------------- Length of time ------------------
# 80分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc132/editorial.pdf
# 高校生クイズで見た方法でやったせいで頭が混乱した
# 解説のように，(n-k)個の赤玉の間or両端にi個の青塊を入れると考えると，単純に(n-k+1)C(i)となり，楽
# 時間は罹ったけど自力で解けて嬉しい

# ----------------- Category ------------------
#AtCoder
#組み合わせ
#二項係数
#重複組合せ
#緑diff
#ABC-D
#逆元