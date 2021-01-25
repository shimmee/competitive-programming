# ABC115D - Christmas
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc115/tasks/abc115_d
# Date: 2021/01/24

# ---------- Ideas ----------
# 最長は2**50のバーガーになるから，実際にシミュレーションするのは無理
# iバーガーの層の厚さl[i+1] = 2*l[i]+3 -> l[i] = 2**(i+2)-3
# iバーガーのパティの総数 p[i+1] = 2*p[i]+1 -> p[i] = 2**(i+1)-1

# 1時間考えてわからなすぎて解説みました。以下解説集
# https://takeg.hatenadiary.jp/entry/2019/09/21/204427
# https://betrue12.hateblo.jp/entry/2018/12/08/225123
# https://emtubasa.hateblo.jp/entry/2018/12/28/010000_1
# https://qiita.com/tnodino/items/7c67af5da96ed0cbbe76

# whileで解く or 再帰で解く

# ------------------- Solution --------------------
# 左がバーガーの上，右がバーガーの下側と考える
# 「レベルiバーガーの下からX層にあるパティPの総数」がほしい
# f(i, x) = 「レベルiバーガーの下からX層にあるパティPの総数」とおく
# xが真ん中より右か，真ん中か，左か，の3つで場合分け
# 真ん中より右のとき: f(i, x) = f(i-1, x-1)
# 真ん中のとき: f(i, x) = p[i-1]+1
# 真ん中より左のとき: f(i, x) = p[i-1] + 1 + f(i-1, x-median)

# 初期値はi=0でx=0のとき0, i=0でx==1のとき1

# ------------------- Answer --------------------
#code:python
import sys
sys.setrecursionlimit(100000)
n, x = map(int, input().split())

# レベルiバーガー全部に含まれる層の枚数
def layer(i):
    return 2**(i + 2) - 3

# レベルiバーガー全部に含まれるパティの枚数
def patty(i):
    return 2 ** (i + 1) - 1

def rec(i, x):
    l = layer(i)
    m = (l+1)//2
    if i == 0:
        return 0 if x <= 0 else 1
    elif x == m: # 真ん中のとき: f(i, x) = p[i-1]+1
        return patty(i-1)+1
    elif x > m: # 真ん中より左のとき: f(i, x) = p[i-1] + 1 + f(i-1, x-median)
        return patty(i-1) + 1 + rec(i-1, x-m)
    else: # 真ん中より右のとき: f(i, x) = f(i-1, x-1)
        return rec(i-1, x-1)

print(rec(n, x))
# ------------------ Sample Input -------------------
2 7

1 1

50 4321098765432109


# ----------------- Length of time ------------------
# 考察と解説AC含めて2時間以上

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc115/editorial.pdf
# hard問題の中で一番難しかった
# まず構造を理解するのが難しかった。この解説をみてやっと理解できた: https://takeg.hatenadiary.jp/entry/2019/09/21/204427
# 復習します...

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#再帰的構造に着目する
#フラクタル構造を解く
#再帰関数
#ABC-D