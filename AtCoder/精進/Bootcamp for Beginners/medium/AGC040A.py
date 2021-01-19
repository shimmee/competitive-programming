# AGC040A - ><
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc040/tasks/agc040_a
# 日付: 2020/12/28

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 解説AC: https://img.atcoder.jp/agc040/editorial.pdf
# 解説みてもムズい
# ai−x < ai−x+1 < · · · < ai のとなっていれば，ai は x 以上でなくてはなりません．
# また同様に， ai > ai+1 > · · · > ai+x のときも，ai は x 以上でなくてはいけません．
# すると，a の各項について，その値は，左に連続する < の個数と右の連続する > の個数の max 以上である必要があるとわかります．
# 逆に，左に連続する < の個数と右の連続する > の個数の max とすれば，条件 をみたす数列が得られます．
# よって，各項の最小値がわかり，その総和が答えになります．

# 長さ|S|+1のリストを用意
# ループでS[i]が<なら，l[i+1]=l[i]+1で更新
# 2回目のループをreversedで回す
# S[i]が>なら，l[i+1]=l[i]+1かl[i]で大きい方をl[i]にいれる

# ------------------- 解答 --------------------
#code:python

# 参考: https://atcoder.jp/contests/agc040/submissions/19017978
S = input()
n = len(S)

now = S[0]
l = [0]*(n+1)
for i in range(n):
    if S[i] == '<':
        l[i+1] = l[i] + 1

for i in reversed(range(len(S))):
    if S[i]==">":
        l[i] = max(l[i],l[i+1]+1)


print(sum(l))
# ------------------ 入力例 -------------------
<>>><<><<<<<>>><


# ----------------- 解答時間 ------------------
# 解説AC

# -------------- 解説 / 感想 / 反省 -------------
# 10分考えて全く手がかりなしでgive up
# むずすぎる
# 頭が混乱して吐きそう
# ABC-D相当とか言われてる: https://ami-atcoder.hatenablog.com/entry/20191106/1573017581

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#解説AC #medium復習