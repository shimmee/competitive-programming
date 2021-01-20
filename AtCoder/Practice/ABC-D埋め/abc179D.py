# ABC179D-Leaping Tak
# URL: https://atcoder.jp/contests/abc179/tasks/abc179_d
# 日付: 2020/11/20

# ---------- 思ったこと / 気づいたこと ----------
# DPで解けそう: 単純な部分和問題
# 単純な計算量では20万**2で間に合わんけど，とりあえず書いてみよう

# ------------------- 解答 --------------------
code:python
    mod = 998244353
    import numpy as np
    n, k = map(int, input().split())
    S = np.array([False]*(n+1))
    for _ in range(k):
        l, r = map(int, input().split())
        S[l:r+1] = True
    S = [i for i in range(n+1) if S[i]]


    dp = [0]*n
    dp[0] = 1
    for i in range(1, n):
        for s in S:
            if i-s >= 0:
                dp[i] = (dp[i] + dp[i-s]) % mod

    print(dp[n-1] % mod)

    # TLE。
    # けんちょんさんのブログ: https://drken1215.hatenablog.com/entry/2020/09/20/081800
    # DPを高速化する手法があって，それが必要らしい:。
    # K個の区間の累積和を取っておいて，n*Kのループでマスっぽい
    # dpの累積和sdpを用意して
    # dp[i] = sum_k(sdp[i-lr[r]] - sdp[i-lr[l]]) で求めるらしい

    mod = 998244353
    n, k = map(int, input().split())
    S = [[int(i)-1 for i in input().split()] for _ in range(k)]

    dp = [0]*n
    sdp = [0]*(n+1) # dpの累積和

    # テーブルの初期化
    dp[0] = 1
    sdp[1] = 1

    for i in range(1, n):
        for l, r in S:
            left = max(0, i-r-1)
            right = max(0, i-l)
            dp[i] = (dp[i] + sdp[right] - sdp[left]) % mod
        sdp[i+1] = (sdp[i] + dp[i]) % mod
    print(dp[n-1] % mod)



# ------------------ 入力例 -------------------
5 2
1 1
3 4


5 1
1 2

5 2
3 3
5 5

60 3
5 8
1 3
10 15



# ----------------- 解答時間 ------------------
# WAの解答は10分くらいでかけた

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/abc179/editorial/121
# 参考: https://qiita.com/xkent/items/95bf00b72bfac711bd20
# なんかわかったようでわかってない。でもこの系統の問題がきたらこれで解けそうってのはわかった


# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#DP #動的計画法 #累積和
#知らないアルゴリズムだった