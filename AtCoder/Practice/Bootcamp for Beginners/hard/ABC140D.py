# ABC140D - Face Produces Unhappiness
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc140/tasks/abc140_d
# Date: 2021/01/28

# ---------- Ideas ----------
# ABC124D - Handstandににてる
# LとRをまたいでひっくり返すなんていう複雑な操作をするはずがない。
# Lの塊をRに，Rの塊をLにすることだけ考えればいい
# 全員同じ方向に向くのが一番理想的
# 連続でたくさん並んでいる塊から

# ------------------- Solution --------------------
# 180度回転は何の意味もないし，LRまたがってやる意味もないから，LorRが連続した部分を反転させることを考える
# LRやRLとなってる部分は不幸なので，入れ替えてあげたい
# LRRLのRRを反転しても，LRRRRLのRRRRを反転しても，幸せになる増加分は2
# 端っこ以外の人を1回反転して増加させられる人数は2人だけ。
# すでにhappyな人に加えて，k回*2人だけ幸せな人を増やせられる

# 現在happyな人を数える
# RLとLRの数を数える: cnt
# 出力は最大でn-1か「happyな人 + k回の反転で幸せにできる人」

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
S = input()

cnt = 0
happy = 0
for i in range(n-1):
    if S[i] == S[i+1]:
        happy += 1
    if S[i]+S[i+1] == 'RL' or S[i]+S[i+1] == 'LR':
        cnt += 1
print(min(n-1, happy + min(k, cnt)*2))


# ------------------ Sample Input -------------------
6 1
LRLRRL
#LRRRRL

13 3
LRRLRLRRLRLLR

10 1
LLLLLRRRRR

9 2
RRRLRLRLL
#RRRLLLLLL

12 2
RRRLRLLLRL

RRRRRLLLLLLLLLLLLLLLLLLRRRRRRRRRLLRRR

# ----------------- Length of time ------------------
# 1時間以上かけて解説AC

# -------------- Editorial / my impression -------------
# 赤坂からヒントもらって解いた
# トラウマになるほど難しかった
# 誰が思いつくんだろう

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#操作:flip
#操作:区間
#条件の言い換え



# 残骸たち
# n, k = map(int, input().split())
# S = input()
#
# from itertools import groupby
# gr = groupby(S)
# l = []
# for key, group in gr:
#     l.append(len(list(group)))
#
# m = len(l)
# seq3 = []
# for i in range(1, m-1):
#     seq3.append(l[i-1]+l[i]+l[i+1])
#
# print(seq3)
#
#
# "aaaLbbb".split('L')