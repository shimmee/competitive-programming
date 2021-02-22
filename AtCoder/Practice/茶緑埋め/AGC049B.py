# AGC049B - Flip Digits
# URL: https://atcoder.jp/contests/agc049/tasks/agc049_b
# Date: 2021/02/20

# ---------- Ideas ----------
# 01 -> 10: 転倒
# 11 -> 00: 2つずつ変換する
# 転倒数みたいなやつ -> 累積和
# 1の個数は増やせない: Sにある1の個数 < Tにある1の個数，であれば不可能
# 1の個数がSとTで一致していても，S=11100からT=00111は無理: 1は右から左には動かせるけど，左から右は無理
# Sにある1の個数 > Tにある1の個数でも，1の個数の偶奇が一致してなければ無理
# 行ける条件，(Sにある1の個数 > Tにある1の個数)かつ(1の個数の偶奇が一致)かつ
# (Sの各1のインデックスより右側に存在する1の個数を数えて，SよりTが多かったら無理)
# トータルの操作回数 = k1+k2
# k1 = Sから1を2個ずつ変換する回数 (Sの個数-Tの個数)//2
# k2 = 0と1を転倒させる回数
# まずk1個の変換するやつを決める: Sを左から操作して，S[i]==1のときにT[i] == 1であればcontinue,
# T[i]==0であれば，その1は使えないので，0に変換する: 2個ずつ変換する必要があるので，次に出現する1も変換する
# 変換した個数がk1個になるまで変換する: 新しいSをS_newとする
# 0と1を転倒させる回数: Sの各1のインデックスから右側で一番近いTの1の場所 (使用してない場所のみ)

# ------------------- Solution --------------------
# 上の解法ではWAになったので解説ACしました

# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()
T = input()
S_rev = S[::-1]
T_rev = T[::-1]

# Sに含まれる1の個数とTに含まれる1の個数
s1 = len([i for i in S if i == '1'])
t1 = len([i for i in T if i == '1'])

# 行ける条件，(Sにある1の個数 > Tにある1の個数)かつ(1の個数の偶奇が一致)
if s1 < t1 or s1 % 2 != t1 % 2:
    print(-1); exit()

# (Sの各1のインデックスより右側に存在する1の個数を数えて，SよりTが多かったら無理)
S_cum = [0]
T_cum = [0]
for i in range(n):
    if S_rev[i] == '1':
        S_cum.append(S_cum[i]+1)
    else:
        S_cum.append(S_cum[i])

    if T_rev[i] == '1':
        T_cum.append(T_cum[i]+1)
    else:
        T_cum.append(T_cum[i])

flag = True
for i in range(1, n+1):
    if S_cum[i] < T_cum[i]:
        flag = False

if not flag:
    print(-1); exit()

# k1 = Sから1を2個ずつ変換する回数 (Sの個数-Tの個数)//2
# 例えばS=10001をT=00000にするとき，ケツの1を移動しなきゃいけないので，その分も操作回数に含める
k1 = (s1-t1)//2
cnt = 0 # 変換の回数
move = 0 # 変換のための移動回数
S_new = []
pre = -1 # 変換する1が1つ決まった状態の，1つめの1のインデックス
for i in range(n):
    if cnt < k1:
        if S[i] == '1' and pre >= 0:
            S_new.append('0')
            move += i - pre - 1
            cnt += 2
            pre = -1
        elif S[i] == '1' and T[i] == '0' and pre == -1: #
            S_new.append('0')
            pre = i
        else:
            S_new.append(S[i])
    else:
        S_new.append(S[i])

# この時点で，moveが1を変換するための移動回数になっているので，変換する回数k1に足す
k1 += move

# また，S_newは変換後の姿なので，ここから転倒してTに一致させる
# k2: 0と1を転倒させる回数
k2 = 0
now = 0 # Sの位置
for i in range(n): # Tの位置
    if T[i] == '1':
        while S_new[now] != '1':
            now += 1
        k2 += now-i
        now += 1

print(k1+k2)

# 90分かけて，34ケース中15WA: https://atcoder.jp/contests/agc049/submissions/20358103
# giveupします
# 解説: https://atcoder.jp/contests/agc049/editorial
# 累積XoRとか言うててなんかよくわからんけど，普通に貪欲でも解けるっぽい
# わかりやすそう?: https://atcoder.jp/contests/agc049/submissions/19304587

# iより左にあるTの1と，iより右にあるSの1をマッチングさせたい。
# Tを左から走査していく
# Tに1が現れたら，Sの1とマッチングする必要があるので，インデックスをマッチングリストtにいれる
# Sに1が現れたら
# Tのマッチングリストに要素があれば，マッチングさせる。2つの要素の距離が反転回数となるのでインクリメント
# Tのマッチングリストがない場合，このS[i]=1は対消滅させるしかないので，対消滅待ちリストsに入れる
# もし対消滅待ちリストに要素がある場合には，対消滅させる。なかったら入れる。


n = int(input())
S = input()
T = input()

# Sに含まれる1の個数とTに含まれる1の個数
s1 = len([i for i in S if i == '1'])
t1 = len([i for i in T if i == '1'])

# 行ける条件，(Sにある1の個数 >= Tにある1の個数)かつ(1の個数の偶奇が一致)
if not ((s1 >= t1) and (s1 % 2 == t1 % 2)):
    print(-1); exit()

from collections import deque
ans = 0
s = deque([]) # Sにある，対消滅待ちリスト
t = deque([]) # Tにある，マッチング待ちな1のインデックスを保存
for i in range(n):
    if T[i] == "1": # この1をマッチング待ち
        t.append(i)
    if S[i] == "1":
        if len(t) > 0: # マッチング待ちの1がTにあるとき: i以前に出現しているとき
            j = t.popleft() # Sにマッチングさせる
            ans += i - j # 移動距離
        elif len(s) > 0: # すでにsに1が出現してる時，今のiを移動させて対にして消さなきゃいけないので，
            j = s.pop()
            ans += i - j
        else:
            s.append(i) # この子はもう対消滅するしかない
if len(s) != 0 or len(t) != 0:
    print(-1)
    exit()
print(ans)


# ------------------ Sample Input -------------------


9
001000001
110000000

3
001
100

3
001
110

5
10111
01010



# ----------------- Length of time ------------------
# 2時間かかって無理で解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/agc049/editorial/330
# 不可能なときの条件自体は半分くらいあってた?
# 転倒数だと思ってしまったのが沼の始まりだった
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/11/15/051800
# 自分で上に書いた解説が一番わかり易い

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#AtCoder600点
#AGC-B
#緑diff
#パリティ
#Greedy
#0と1の問題
#操作:最小回数
#SをTにすることが目的の操作の問題
#操作:flip
#操作:隣接swap
#端から順に決まって行くGreedy
#今が良いほど未来も良いGreedy
#deque
#対消滅
#マッチング