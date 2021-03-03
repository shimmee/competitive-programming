# ABC179E - Sequence Sum
# URL: https://atcoder.jp/contests/abc179/tasks/abc179_e
# Date: 2021/03/02

# ---------- Ideas ----------
# 周期性がありそう
# 同じものが出てきたら周期の始まり
# 周期が始まりのインデックスと周期の長さがわかれば良い
# 周期が始まるまでの和 + 周期の繰り返しの和 + 周期のおこぼれの和

# ------------------- Answer --------------------
#code:python
n, x, m = map(int, input().split())

flag = [False]*(10**5+2) # ある数が出現したら，その出現した際の項数を入れる: A[i]のiの部分
A = [] # A1から最初の周期の終わりまでを保存するリスト

a = x # 初項
for i in range(10**5): # 最大でも10**5回のうちに周期が来るはず
    if flag[a]: # 出現済みなら，このaが周期の始まり
        d = i - flag[a] # 周期の幅
        start = flag[a] # 最初の周期が始まるインデックス (0-indexed)
        break
    else:
        A.append(a)
        flag[a] = i
        a = a**2 % m

# 周期が始まるまでの和 + 周期の繰り返しの和 + 周期のおこぼれの和

A_rep = A[start:] # Aのうち周期している部分
rep, r = divmod(n-start, d) # 周期が完全に繰り返される回数と，余るおこぼれ長さ
ans = sum(A[:start]) # 周期が始まるまでのA[i]の和
ans += sum(A_rep)*rep + sum(A_rep[:r]) # 繰り返しの部分の和と，余りのおこぼれの和

print(ans)



# ------------------ Sample Input -------------------
6 2 1001

1000 2 16

10000000000 10 99959

# ----------------- Length of time ------------------
# 25分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc179/editorial
# いつか参加した回に解説をざっくり読んで周期性で解くって知ってたから，スイスイ解けた
# 手元での考察がとても役に立った: 添え字バグを起こさずに済んだ

# ----------------- Category ------------------
#AtCoder
#AtCoder500点
#ABC-E
#ダブリング
#周期性に着目する
#シミュレーション問題
#サイクル
#整数問題
#数列
#漸化式
#鳩の巣原理
#累積和
#総和を求める
#K回操作後の結果を求める
#操作:整数をreplaceしていく
#緑diff
