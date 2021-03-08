# ABC194E - Mex Min
# URL: https://atcoder.jp/contests/abc194/tasks/abc194_e
# Date: 2021/03/06

# ---------- Ideas ----------
# 本番でACできませんでした
# しゃくとり法みたいな感じで，幅がmの区間を右にどんどんずらしていく
# 最も大事な考え方は，
# 「mexの最小値を探せばいいんだから，移動のさいに小さい方にmexが更新される時だけansを更新すればよくて，右の方に探しに行く必要はない」ということ
# mexの最小値が更新されるのは，出ていく子(a_out)の個数が1で，かつ入ってくる子(a_in)が出ていく子(a_in)とは異なる場合のみ


# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
A = list(map(int, input().split()))

# m個の連続部分列の中にある数の出現回数
counter = [0]*(max(A)+2)

# Aの最初のm個の出現回数
for i in range(m):
    counter[A[i]] += 1

# mexの初期値
mex = counter.index(0)

for i in range(m, n): # しゃくとり法っぽく連続部分列を1文字ずつ右にずらしていく
    a_out = A[i-m] # 出ていく子
    a_in = A[i] # 入ってくる子

    # mexの最小値が更新されるのは，出ていく子(a_out)の出現回数が1で，かつ入ってくる子(a_in)が出ていく子(a_in)とは異なる場合のみ
    if counter[a_out] == 1 and a_in != a_out:
        mex = min(mex, a_out)
    counter[a_out] -= 1
    counter[a_in] += 1

print(mex)



# ------------------ Sample Input -------------------
7 3
0 1 2 3 2 0 1

7 3
0 0 1 2 0 1 0


# ----------------- Length of time ------------------
# 1時間頑張って解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc194/editorial
# 解説はよくわからんけど，ツイッターを参考にした
# 参考1: https://twitter.com/Jessica_nao_/status/1368226281892896771
# 参考2: https://twitter.com/jajam1n/status/1368207705651900426
# 「mexが大きくなったときには更新しなくていい」というアイデアが超大事で，たぶん本番中に時間があっても思いつけなかったと思う

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#バケット
#カウンター
#しゃくとり法
#mex
#最小の非負整数