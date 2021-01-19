# ABC174D - Alter Altar
# URL: https://atcoder.jp/contests/abc174/tasks/abc174_d
# 日付: 2020/11/20

# ------------------- 方針 --------------------
# 文字列をリストに変換する
# 左端にRがあれば無視できるので消す
# 右端にWがあれば無視できるので消す
# 左端がWかつ右端がだったらansを1増やして，両端を削る
# リストが空になるまで回す
# O(N)で回るはず



# ------------------- 解答 --------------------
#code:python
n = int(input())
c = input()

ans = 0
for i in range(n):
    if c == '':
        break
    if c[0] == 'R' and c[-1] == 'W':
        c = c[1:]
        c = c[:(len(c) - 1)]
    elif c[0] == 'R' and c[-1] == 'R':
        c = c[1:]
    elif c[0] == 'W' and c[-1] == 'R':
        ans += 1
        c = c[1:]
        c = c[:(len(c) - 1)]
    elif c[0] == 'W' and c[-1] == 'W':
        c = c[:(len(c) - 1)]
print(ans)


n = int(input())
c = input()
c = [i for i in c]

ans = 0
for i in range(n):
    if c == []:
        break
    if c[0] == 'R' and c[-1] == 'W': #左端にR，右端にWがあれば，両方無視できるので消す
        c.pop(0)
        c.pop()
    elif c[0] == 'R' and c[-1] == 'R': #左端に
        c.pop(0)
    elif c[0] == 'W' and c[-1] == 'R':
        ans += 1
        c.pop(0)
        c.pop()
    elif c[0] == 'W' and c[-1] == 'W':
        c.pop()
print(ans)




n = int(input())
c = input()
c = [i for i in c] # 文字列をリストにする

ans = 0
for i in range(n): #最大20万回回す
    if len(c) == 0: # リストの要素が空になったらbreak
        break
    if c[0] == 'R': #左端にRがあれば無視できるので消す
        c.pop(0)
    elif c[-1] == 'W': #右端にWがあれば無視できるので消す
        c.pop()
    elif c[0] == 'W' and c[-1] == 'R': # 左端がWかつ右端がだったらansを増やして，両端を削る
        ans += 1
        c.pop(0)
        c.pop()
print(ans)


# 解説読んだ
# https://img.atcoder.jp/abc174/editorial.pdf
# 石を左右に分ける仕切りを用意して動かす。
# 仕切りより左側にあるWと右側にあるRを0にしたい
# max(W, R)を取って，大きい方が必要回数となる。
# 「仕切りより左にあるW」をループのたびに数えるとTLEになるので，累積和を用いる
n = int(input())
c = input()


cum_w = [0]*(n+1)
cum_r = [0]*(n+1)
# WとRの累積和をとる
for i in range(n):
    if c[i] == 'W':
        w = 1
        r = 0
    else:
        w = 0
        r = 1
    cum_w[i + 1] = cum_w[i] + w
    cum_r[i + 1] = cum_r[i] + r


ans = 10**10
for i in range(n+1):
    w = cum_w[i]-cum_w[0]
    r = cum_r[n] - cum_r[i]
    ans = min(ans, max(w, r))
print(ans)

# ------------------ 入力例 -------------------
2
RR

8
WRWWRWRR


# -------------- 解説 / 感想 / 反省 -------------
# 最初の解答でTLEになる理由がわからない。
# https://img.atcoder.jp/abc174/editorial.pdf


# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#累積和
#知ってるアルゴリズムだった
