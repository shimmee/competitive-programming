# AGC048A - atcoder < S
# URL: https://atcoder.jp/contests/agc048/tasks/agc048_a
# Date: 2021/03/14

# ---------- Ideas ----------
# 文字を好きな場所に移動できる？
# atcoder < S，としたいから，とりあえず頭をa以外のものにすればOK
# Sがaだけで構成されていれば，どうしようもないので-1
# a以外の文字があれば，左から一番近いa以外の文字までの距離が答えになる -> これは嘘
# S=aaaaaaaaauであればuaaaaaaaaとしなくても，auaaaaaaaでOK
# S = atcccccccccxであれば，atcxccccccでOK -> これは嘘，tacccccccxが最適で操作回数1回
# S=aaaaaaab，S=aaaaaaat

# ------------------- Answer --------------------
#code:python
n = int(input())
for _ in range(n):
    S = input()
    if 'atcoder' < S:
        print(0)
    else:
        m = len(S)
        for i in range(m):
            if S[i] != 'a':
                if S[i] > 't':
                    print(i-1)
                    break
                else:
                    print(i)
                    break
        else:
            print(-1)



# ------------------ Sample Input -------------------

aaaaaaaaaau

atcodere
atzoder

g
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaae


3
atcodeer
codeforces
aaa


# ----------------- Length of time ------------------
# 29分AC: WAが出たのでテストケースカンニングした

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/agc048/editorial
# 最初，S=aaaaaaatはataaaaaaにすれば良いことに気づかず，taaaaaaaaになるまでやると考えていたため，WAが出た
# 1文字さえ移動すればいいことにすぐ気づいたので簡単だった。

# ----------------- Category ------------------
#AtCoder
#AGC-A
#緑diff
#文字列問題
#Greedy
#最小回数
#スワップ
#操作:swap
#操作:隣接swap
#辞書順
#ある量を固定して考える
