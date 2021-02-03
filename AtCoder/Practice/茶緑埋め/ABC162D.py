# ABC162D - RGB Triplets
# URL: https://atcoder.jp/contests/abc162/tasks/abc162_d
# Date: 2021/02/02

# ---------- Ideas ---------- 
# 各R，G, Bの累積和を持っておく
# 2重ループでiとjを回す。

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()

R_cum = [0]
G_cum = [0]
B_cum = [0]
for i in range(n):
    if S[i] == 'R':
        R_cum.append(R_cum[i] + 1)
    else:
        R_cum.append(R_cum[i])
    if S[i] == 'G':
        G_cum.append(G_cum[i] + 1)
    else:
        G_cum.append(G_cum[i])
    if S[i] == 'B':
        B_cum.append(B_cum[i] + 1)
    else:
        B_cum.append(B_cum[i])

ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if (S[i] == 'R' and S[j] == 'G') or (S[i] == 'G' and S[j] == 'R'):
            ans += B_cum[-1] - B_cum[j]
            if 2*j-i < n and S[2*j-i] == 'B':
                ans -= 1
        if (S[i] == 'G' and S[j] == 'B') or (S[i] == 'B' and S[j] == 'G'):
            ans += R_cum[-1] - R_cum[j]
            if 2*j-i < n and S[2*j-i] == 'R':
                ans -= 1
        if (S[i] == 'B' and S[j] == 'R') or (S[i] == 'R' and S[j] == 'B'):
            ans += G_cum[-1] - G_cum[j]
            if 2*j-i < n and S[2*j-i] == 'G':
                ans -= 1
print(ans)


# 史上最高に回りくどい解き方をしてしまった
# 単純にRの個数*Gの個数*Bの個数からj−i≠k−jとなるものを引けばいい
n = int(input())
S = input()

r,g,b = 0,0,0
for i in range(n):
    if S[i] == 'R': r += 1
    elif S[i] == 'G': g += 1
    elif S[i] == 'B': b += 1

cnt = r*g*b
for i in range(n):
    for j in range(i+1, n):
        k = 2 * j - i
        if k < n:
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                cnt -= 1
print(cnt)
# ------------------ Sample Input -------------------
4
RRGB

39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB


# ----------------- Length of time ------------------
# 18分

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/abc162/editorial.pdf
# とても頭の悪い解き方をしてしまった。
# 因縁深いAGC031A - Colorful Subsequence に良く似てる。https://atcoder.jp/contests/agc031/tasks/agc031_a
# けんちょんさん解説: https://drken1215.hatenablog.com/entry/2020/04/12/225900
# 復習してもいいかなという感じ
# 文字列からピックアップして作り上げる組み合わせは，文字の種類をかけ合わせたものになる

# ----------------- Category ------------------
#AtCoder  
#ABC-D
#包除原理
#補集合を考える
#数え上げ問題
#3重ループを2重ループに
#O(N^2)個のものを考える問題
#文字列問題
#制約条件:等間隔
#茶色diff
