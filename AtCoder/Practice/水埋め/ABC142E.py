# ABC142E - Get Everything
# URL: https://atcoder.jp/contests/abc142/tasks/abc142_e
# Date: 2021/04/03

# ---------- Ideas ----------
# ヘンリーとはじめての競プロ合宿 (日帰り)
# N <= 12なので，bitが絡んだ解き方ができそう
# M <= 1000なので，O(M*2**N)とかは間に合う
# bit DPで解けそう
# N個の箱のそれぞれを開けられたかどうかをbitで管理: N桁のビット
# i番目の鍵で開けられる箱をビットで表現
# dp[i][s]: i番目の鍵まで使用可能で，sで表現される箱を開けるときの最小コスト

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())

inf = float('INF')
dp = [[0]+[inf]*(2**n-1) for _ in range(m+1)]

for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    c = [p-1 for p in c]

    # i番目の鍵で開けられる箱のbit(2進数表記)と10進数
    c_bit = ['0']*n
    for j in c:
        c_bit[j] = '1'
    c_bit = ''.join(c_bit)
    c_10 = int(c_bit, 2)

    for k in range(1, 2**n): # すべての箱の組み合わせをbitで表現
        k_bit = bin(k)[2:].zfill(n)

        # cの鍵を用いることで，kで表される箱の組み合わせを開けるようになるとき，もともとの箱はどんな組み合わせであればよいか，の表現: gap_bit
        gap_bit = ['0']*n
        for j in range(n):
            if c_bit[j] == '0' and  k_bit[j] == '1':
                gap_bit[j] = '1'
        gap_bit = ''.join(gap_bit)

        gap_10 = int(gap_bit, 2)

        # i番目の鍵を使う
        if dp[i+1][k] >= dp[i][gap_10] + a:
            dp[i + 1][k] = dp[i][gap_10] + a

        # i番目の鍵を使わない
        if dp[i+1][k] >= dp[i][k]:
            dp[i + 1][k] = dp[i][k]

ans = inf
for i in range(m+1):
    ans = min(ans, dp[i][-1])

if ans == inf:
    print(-1)
else:
    print(ans)

# これだと3ケースTLEになる
# 3重ループになっていて，遷移の元の集合を探すのに3重目のループが必要になっているが，これを除く方法がわからん
# O(N*M*2**N)で，定数倍の勝負に負けてる
# ヘンリーが再帰書いてACした
# 色々工夫したけどTLEが取れないので解説見る
# アイデアはほとんど合ってたけど，遷移の仕方が少し非効率だった
# 貰うDPではなくて配るDPで考えるべきだった
# ある鍵のbit表現が0101なら，1つめ，3つめの箱が開いた状態で表される任意の箱bit表現に遷移できる
# これは，bitの演算でいうとorである
# なので鍵を2進数で表現 -> ビットシフトで10進数に変換: c_bitとする
# 状態sから，s|c_bitに遷移できるので，コストが安くなるのであれば更新する
# dp手＝ブルは2次元の方がわかりやすいが，1次元でも書くことができる

n, m = map(int, input().split())

inf = float('INF')
dp = [0] + [inf]*(2**n-1)

for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))

    c_bit = 0
    for j in c:
        c_bit |= 1 << (j - 1)

    for s in range(2**n):
        dp[s|c_bit] = min(dp[s|c_bit], dp[s] + a)

if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])

# ------------------ Sample Input -------------------
2 3
10 1
1
15 1
2
30 2
1 2


# ----------------- Length of time ------------------
# 2時間かけて解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc142/editorial.pdf
# 超楽しかった
# 配るDPと貰うDPを意識するべきだった
# どうにか貰う形で書こうとしてたから上手く行かなかった
# けんちょん: https://drken1215.hatenablog.com/entry/2019/09/29/103500

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#dp
#動的計画法
#bitDP
#bitmasking_dp
#ビットシフト
#配るDP