# ARC068D - Card Eater
# URL: https://atcoder.jp/contests/arc068/tasks/arc068_b
# Date: 2021/03/06

# ---------- Ideas ----------
# たぶん貪欲で解く。どう貪欲するか？
# 1枚のやつはもったいないから避けておく
# 2枚被ってるカードを小さいのと大きいのを取り出して消せる
# 被ってるやつのうち最小と最大を食べる

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
A = deque(sorted(list(map(int, input().split()))))

ans = set()
while A:
    if len(A) == 3:
        ans.add(A[1])
        break
    if len(A) == 1:
        a = A.popleft()
        ans.add(a)
        break
    a = A.popleft()
    b = A.pop()

    if A[0] == a and A[-1] == b:
        continue
    elif A[0] != a and A[-1] == b:
        ans.add(a)
        A.append(b)
    else:
        ans.add(b)
        A.appendleft(a)

print(len(ans))

# 解説のヒント見ます: https://img.atcoder.jp/arc068/editorial.pdf
# 基本的には 1 枚しかないカードを取り除かれないカードに，
# 余っているカードを取り除かれるカードに選ぶことができるので操作は「 2 枚の カードを選んで取り除く」とみなしてほぼ構いません．

# わからんので他の解説見ます: https://yamakasa.net/atcoder-abc-053-d/
# カードの種類をmとします。このとき、残ったカードをm枚にするためには、N–m枚のカードを取り除かなければいけません。
# 1回の操作で取り除かれるカードは2枚なので、N–mが偶数であれば答えはmとなり、奇数であれば答えはm–1となります。

# つまり，基本的に全部できるんだけど，偶奇でズレが決まっちゃうということ

n = int(input())
A = sorted(list(map(int, input().split())))

m = len(set(A))
if (n-m) % 2 == 1: print(m-1)
else: print(m)


# ------------------ Sample Input -------------------

5
1 2 1 3 7

15
1 3 5 2 1 3 2 8 8 6 2 6 11 1 1


# ----------------- Length of time ------------------
# 1時間かけて解けなくて解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc068/editorial.pdf
# 貪欲シミュレーションだと思ってしまった
# 貪欲でも解けるらしいけど，pythonで貪欲してる人いなかった
# 基本は全部残せる。パリティで決まる
# 嘘貪欲にハマってしまった

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#全部できる
#偶奇に注目
#パリティ

