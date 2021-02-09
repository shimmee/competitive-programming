# ARC002C - コマンド入力
# URL: https://atcoder.jp/contests/arc002/tasks/arc002_3
# Date: 2021/02/08

# ---------- Ideas ----------
# Rの2文字分，Lの2文字分はそれぞれABXYのどれを取っても良い
# 4桁のbit全探索 か 4重ループで4文字分決めてあげて全探索
# 各パターンにおいて実際に実際に置換してみて文字数をカウント


# ------------------- Answer --------------------
#code:python
import itertools
n = int(input())
S = input()

button = {0:'A', 1:'B', 2:'X', 3:'Y'}

all_pattern = itertools.product([0, 1, 2, 3], repeat=4)
ans = 10**10
for pattern in all_pattern:
    L = button[pattern[0]] + button[pattern[1]]
    R = button[pattern[2]] + button[pattern[3]]
    ans = min(ans, len(S.replace(L, 'L').replace(R, 'R')))
print(ans)
# ------------------ Sample Input -------------------
13
ABABABABXBXBX

8
AABBAABB


# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc002
# 全探索して置換，これは嘘解法でした。
# S=ABABBABAのとき，L=AB, R=BAとしてL->Rの順に置換するとS=LLBLAになっちゃう。S=LLRRが正解なのに
# だから純粋に置換するのは嘘解法
# 手前から順にDPで置換しながら最小文字数をカウントしていくのが想定解法
# 今回はテストケースが甘くて，嘘解法が通った
# 古い問題だけど，普通に今でも出そうな感じの問題なので復習したい

# ----------------- Category ------------------
#AtCoder
#文字列問題
#文字列置換
#嘘貪欲
#DP
#動的計画法
#復讐したい