# ABC045C - たくさんの数式
# URL: https://atcoder.jp/contests/abc045/tasks/arc061_a
# 日付: 2020/12/18

# ---------- 思ったこと / 気づいたこと ----------
# これは再帰か？どんどん仕切りを増やしていく再起ではないのか？
# 全てのパターンを列挙する方法として3つほど挙げられる
# アイデア1: [[125]]にしきりを1つずつどんどん増やす -> [[125], [1, 25], [12, 5]] -> [[125], [1, 25], [12, 5], [1, 2, 5]]
# アイデア2: [[1, 2, 5]]から1つずつ仕切りをへらす -> [[1,2,5], [12, 5], [1, 25]] ->
# アイデア3: 空のリストから初めて (1) リストの最後の文字にi番目の文字を付け足し and (2) リストのケツにi番目の文字をappend


# ------------------- 方針 --------------------
# 3つめのアイデアは簡単にfor文で書ける

# ------------------- 解答 --------------------
#code:python

S = input()
n = len(S)

L = [[S[0]]]
for i in range(1, n):
    new = []
    for l in L:
        new.append(l+[S[i]])
        l[-1] = l[-1]+S[i]
        new.append(l)
    L = new

ans = 0
for l in L:
    ans += sum([int(i) for i in l])
print(ans)

# 解説はbit全探索だった: https://img.atcoder.jp/data/arc/061/editorial.pdf
# 数字の組み合わせではなく，+をどこに入れるかに着目して，N<=10なのでどこに入れるか全探索できる
# n桁の数字に対して最大でn-1個の＋をいれられる
S = input()
n = len(S)
ans = 0
import itertools
pattern = itertools.product([0, 1], repeat=n-1)
for p in pattern:
    now = S[0]
    for i in range(n-1): # i桁目とi+1桁目の間
        if p[i] == 0:
            now += S[i+1]
        else:
            ans += int(now)
            now = S[i+1]
    ans += int(now)
print(ans)


# ------------------ 入力例 -------------------
1234

125

9999999999

# ----------------- 解答時間 ------------------
# 50分 色々考えすぎた

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/arc/061/editorial.pdf
# bit全探索で解く問題だったけど，ただのfor文で全探索してしまった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#bit全探索
#復習したい
