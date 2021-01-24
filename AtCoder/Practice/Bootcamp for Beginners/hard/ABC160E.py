# ABC160E - Red and Green Apples
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc160/tasks/abc160_e
# Date: 2021/01/21

# ---------- Ideas ----------
# 貪欲か?
# p,q,rはソートするよね
# Aを食べ続けてみて，Cを食べたほうがいいチャンスが来たら，Bを食べ始める
# Bでも，Cを食べたほうがいいチャンスが来たなら，CをAかB，どっちにした方が -> この方法はダメ。
# ABC172C-Tsundokuににてる: 貪欲で上手く行かない理由は，このTsundokuと同じ。
# たぶん二分探索つかう: Cを何個使うかを決め打ちすれば，AとBから何個食べるか決められる，みたいな？

# Cはどっちに使ってもいいというのが肝

# X=2, A=6のときって，最大でもAから2つしか使わないから，Aから弱いの4つ減らしてOK


# ------------------- Answer --------------------
#code:python
X,Y,A,B,C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)

from itertools import accumulate
p_cum = [0] + list(accumulate(p))
q_cum = [0] + list(accumulate(q))
r_cum = [0] + list(accumulate(r))

ans = 0
for ca in range(C+1):
    if X-ca >= 0:
        for cb in range(C-ca+1):
            if Y-cb >= 0:
                taste = r_cum[ca] + p_cum[X - ca]
                taste += r_cum[cb] - r_cum[ca] + q_cum[Y-cb]
                if taste >= ans:
                    ans = taste
print(ans)
# O(N^2)でTLE


# 無色りんごの個数cを固定する
#
X,Y,A,B,C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)[:X]
q = sorted(list(map(int, input().split())), reverse=True)[:Y]
r = sorted(list(map(int, input().split())), reverse=True)[:X+Y]
C = min(C, X+Y)

from itertools import accumulate
r_cum = [0] + list(accumulate(r))
pq_cum = [0] + list(accumulate(sorted(p+q, reverse=True)))

ans = 0
for c in range(C+1):
    taste = r_cum[c] + pq_cum[X+Y-c]
    ans = max(ans, taste)
print(ans)

# 解説: https://img.atcoder.jp/abc160/editorial.pdf
# よって、残ったリンゴを美味しさの大きい方から X + Y 個食べれば良いです。

X,Y,A,B,C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)[:X]
q = sorted(list(map(int, input().split())), reverse=True)[:X]
r = sorted(list(map(int, input().split())), reverse=True)[:X+Y]

print(sum(sorted(p+q+r, reverse=True)[:X+Y]))


# 「白食べない状態から、白食べた方がいいなら食べる」でも解けるらしい。後ろから考えるやつ
# 最初にX個をA個から貪欲にとる。Y個もB個から取る。
# Cから大きいのを持ってきて，XorYの小さい方と置き換える
# キューやヒープでかけそう
# 考えてみたけど，結局やってることは上と同じようだから，あえてやらない

# ------------------ Sample Input -------------------
1 2 2 2 1
2 4
5 1
3

2 2 2 2 2
8 6
9 1
2 1

2 2 4 4 4
11 12 13 14
21 22 23 24
1 2 3 4

# ----------------- Length of time ------------------
# 1.5時間

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc160/editorial.pdf
# 累積和や二分探索やら色々考えたが，とてつもなく単純な貪欲解法だった
# 複数のものを組み合わせてぴったり作りたい時は，まず貪欲にとってみて，そのあと削るという発想が大事かな

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#復習したい
#貪欲
#
