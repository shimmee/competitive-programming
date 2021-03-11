# パナソニックプログラミングコンテスト2020:D - String Equivalence
# URL: https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_d
# Date: 2021/03/10

# ---------- Ideas ----------
# 長さnの文字列に入る文字数の種類によって場合分けできそう？
# n=3のとき，1種類はaaa, 2種類はaab, aba, abb, 3種類はabc
# だがこれだと厳しそう
# そもそも最初の文字は必ずaから始まる
# 次はaの次はaかb，みたいな感じで樹形図的に広がっていく
# 樹形図を書くと分かるが，これはLunLun numberや755問題と同じ
# 再帰で書けるといいが，for文で書く

# ------------------- Solution --------------------
# 'a'から始めて，「文字列に出現している最大文字+1まで」が使用可能な文字なので，文字列の末尾にくっつけていく
# 'ab'であれば，最大文字はbなので，+1はc，なのでaとbとcが使用可能なので，末尾にくっつける: aba, abb, abc
# 'abc'であれば，最大文字はcなので，+1はd，なのでa,b,c,dが使用可能なので，末尾にくっつける: abca, abcb, abcc, abcd
# こんな感じで長さがnになるまで続ける

# ------------------- Answer --------------------
#code:python
n = int(input())
import string
alpha = list(string.ascii_lowercase)

strings = ['a']
for _ in range(n-1):
    temp = []
    for char in strings:
        idx = alpha.index(max(char))
        avail_alpha = alpha[:min((idx+2), 25)]
        for s in avail_alpha:
            temp.append(char + s)
    strings = temp[:]

strings.sort()
for s in strings:
    print(s)

# 少し短い解答: https://qiita.com/c-yan/items/f088c234fd62da01782b
# import stringなしで，ordを使う方法
n = int(input())

strings = ['a']
for _ in range(n-1):
    temp = []
    for char in strings:
        idx = ord(max(char)) + 2
        for i in range(ord('a'), idx):
            temp.append(char + chr(i))
    strings = temp[:]

strings.sort()
for s in strings:
    print(s)

# ------------------ Sample Input -------------------
1

2

# ----------------- Length of time ------------------
# 46分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/panasonic2020/editorial.pdf
# いわゆる重複順列の全列挙
# 複雑そうな問題を解けてとても嬉しい
# この人と完全に同じ解き方をしてる！
# https://blog.hamayanhamayan.com/entry/2020/03/15/002150

# ----------------- Category ------------------
#AtCoder
#ord
#chr
#構築問題
#緑diff
#文字列の構築
#木構造
#樹形図
#再帰
#ABC-D