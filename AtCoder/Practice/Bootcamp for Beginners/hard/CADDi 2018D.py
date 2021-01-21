# CADDi 2018D - Harlequin
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/caddi2018/tasks/caddi2018_b
# Date: 2021/01/20

# ---------- Ideas ----------
# grundy数だ！！！！！！ Nimだ！！！
# 「異なる色のりんごを食べる」=「Nimで違う山から選ぶ」という点が普通のNimとは異なる
# 同じ色のりんごは1回で1つしか食べられない
# 2個以上残ってるりんごの山が残りいくつあるか？


# ------------------- Solution --------------------
# grundy数使いながら実験したら，残りの山が全て偶数個だったら後攻で，otherwise 先行，という感じっぽい
# Nimではなさそう

# ------------------- Answer --------------------
#code:python
n = int(input())
a = [int(input()) for _ in range(n)]
if all(i % 2 == 0 for i in a):
    print('second')
else:
    print('first')

# ------------------ Sample Input -------------------
2
1
2

3
100000
30000
20000


# ----------------- Length of time ------------------
# 40分

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/caddi2018/editorial.pdf
# けんちょんさん解説: https://drken1215.hatenablog.com/entry/2018/12/23/014700
# 解説にも書いてるけど，実験しないと法則がわからない類の問題らしい。おもろい。

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#grundy数
#ゲーム
#パリティ
#偶奇に注目
#実験
#ARC-D
#緑diff
