# CODE FESTIVAL 2017 qual C: C - Inserting 'x'
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_c
# Date: 2021/01/26
1001 1030AC
# ---------- Ideas ----------
# sからまず全てのxを除いたものが回文になっている必要がある。
# 奇数なら，左右の端から真ん中に向かって一致する必要がある (真ん中は何でもOK)
# 奇数なら，左右の端から真ん中に向かって一致する必要がある

# ------------------- Solution --------------------
# xを外して回文になってるかどうかチェック
# xを増やす個数は，左右対称にするために，左右のmaxに合わせる必要がある
# 各文字の間に何個xが入ってるかのリストを作るために
# Sの左から，xが出てきたらcntをインクリメント，x以外ならlにappend
# 両方向から真ん中にループを回して，max-minを取ってインクリメント

# ------------------- Answer --------------------
#code:python
S = input()

S_ = S.replace('x', '')
m = len(S_)

flag = False
# xを除いたs_が回文になってるかチェック
for i in range(m//2):
    if S_[i] != S_[m-1-i]:
        flag = True
if flag:
    print(-1); exit()

l = [] # 各文字の間に何個xが入ってるかのリスト
cnt = 0
for s in S:
    if s == 'x':
        cnt += 1
    else:
        l.append(cnt)
        cnt =0
# 最後の文字の処理がされていないので
# x以外で終わっている場合には0をappend，xで終わる場合cntをappend
if s != 'x':
    l.append(0)
else:
    l.append(cnt)

#
ans = 0
for i in range(len(l)//2):
    ans += max(l[i], l[len(l)-1-i]) - min(l[i], l[len(l)-1-i])
print(ans)

# ACしました！
# 両側から見ていってら簡単に書けるらしい: https://kimiyuki.net/writeup/algo/atcoder/code-festival-2017-qualc-c/
# 左から見ていくポインタlと右から見ていくポインタr
S = input()
n = len(S)
l, r = 0, n-1
cnt = 0

while l < r:
    if S[l] == S[r]:
        l += 1 # lを右に進める
        r -= 1 # rを左にすすめる
    elif S[l] == 'x':
        cnt += 1
        l += 1
    elif S[r] == 'x':
        cnt += 1
        r -= 1
    else:
        cnt = -1
        break
print(cnt)


# ------------------ Sample Input -------------------
xxxxcx

xcxaaxxc

xxaxabcxxxdexdxxcbxaxxa

xabxa

ab

a

oxxx


# ----------------- Length of time ------------------
# 29分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/code-festival-2017-qualc/editorial.pdf
# けんちょんさんは楽に書くため左右からポインターを動かしてる: xだったらcntインクリメント，x以外ならポインタすすめる
# https://drken1215.hatenablog.com/entry/2020/02/19/093100

# ポインタを使った書き方が思いつかないから，復習したい

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#復習したい
#wanna_review
#文字列問題
#回文
#操作:挿入
#緑diff
#ポインタを上手く使う