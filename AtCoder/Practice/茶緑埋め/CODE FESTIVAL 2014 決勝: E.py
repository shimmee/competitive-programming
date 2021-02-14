# CODE FESTIVAL 2014 決勝: E - 常ならずグラフ
# URL: https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_e
# Date: 2021/02/12

# ---------- Ideas ----------
# 上下で始まるものと下上で始まるものを2つ試して，点の多い方を出力する?
# 手前から貪欲に上下になるようにとっていく? -> 嘘解法でした
# しゃくとり法の要領で，極値になる点を取っていく。
# flagとポインタを使って，減少or増加が続く限り右まで進み，進みきったところで前回追加した要素より小さいor大きいならOK

# ------------------- Answer --------------------
#code:python
n = int(input())
R = list(map(int, input().split()))

# 上下: 0-indexで偶数番目が上
l1 = [R[0]]
flag = True # 今上にいるフラッグ
for i in range(1, n):
    if flag and l1[-1] > R[i]: # いま上で次が下
        flag = False
        l1.append(R[i])
    elif (not flag) and l1[-1] < R[i]: # いま下で次が上
        flag = True
        l1.append(R[i])

# 下上: 0-indexで偶数番目が下
l2 = [R[0]]
flag = True # 今下にいるフラッグ
for i in range(1, n):
    if flag and l2[-1] < R[i]: # いま下で次が上
        flag = False
        l2.append(R[i])
    elif (not flag) and l2[-1] > R[i]: # いま上で次が下
        flag = True
        l2.append(R[i])

l = max(len(l1), len(l2))
if l < 3: print(0)
else: print(l)

# 嘘解法です
# R = [1 2 100 2] だったら[1,100,2]ができるのに，手前から貪欲に取ると[1,2]となって最後の2がとれない
# しゃくとり法で右に行けるまで行く or N<3000なので2重ループで書いてみる?
# 普通にポインターを1つ右に動かしていけばいいだけ

n = int(input())
R = list(map(int, input().split()))
if n < 3:
    print(0); exit()

# Trueなら下上下上...となるグラフ，Falseなら上下上下...となるグラフ
flag = True if R[0] < R[1] else False
vec = [R[0]]
i = 1
while i < n:
    if flag: # いま下で，上を探し続ける
        while i < n - 1 and R[i] <= R[i + 1]:
            i += 1
        if vec[-1] < R[i]:
            vec.append(R[i])
        flag = False
    else:
        while i < n - 1 and R[i] >= R[i + 1]:
            i += 1
        if vec[-1] > R[i]:
            vec.append(R[i])
        flag = True
    i += 1

if len(vec) < 3: print(0)
else: print(len(vec))

# やっとAC!!!

# for文でかける...: https://qiita.com/DaikiSuyama/items/bd8bb46c1439caf71904

n = int(input())
R = list(map(int, input().split()))
if n < 3:
    print(0); exit()

vec = [R[0]]
for i in range(1, n-1):
    if vec[-1] < R[i] and R[i] > R[i+1]: # 上昇の極値を探す
        vec.append(R[i])
    elif vec[-1] > R[i] and R[i] < R[i+1]: # 減少の極値を探す
        vec.append(R[i])
    if i == n-2:
        vec.append(R[i+1])

if len(vec) < 3: print(0)
else: print(len(vec))

# ------------------ Sample Input -------------------
5
1 10 10 10 1

3
1 10 1

5
5 5 5 5 5

5
5 4 5 6 7

5
5 4 5 5 5

11
1 2 3 4 3 2 1 10 11 10 10

4
1 2 5 1

5
1 2 3 4 5

6
10 4 1 6 4 1

# ----------------- Length of time ------------------
# 2時間でAC。インデックスがバグりまくった

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/codefestival2014final
# 想定解法はO(N^2)DPだけど，普通にO(N)貪欲で解ける
# 時間がかかりすぎた... 難しく考えすぎた
# 最終的にwhileで書いたけど，for文で書けたっぽい: https://qiita.com/DaikiSuyama/items/bd8bb46c1439caf71904


# ----------------- Category ------------------
#AtCoder
#貪欲
#greedy
#極値
#復習したい