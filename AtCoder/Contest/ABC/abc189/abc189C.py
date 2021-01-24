# ABC189C - Mandarin Orange
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_c
# Date: 2021/01/23

# ---------- Ideas ----------
# 10**4なのでO(N^2)がギリ間に合いそう

# ------------------- Solution --------------------
# iとjをループで回す
# x = a[i]として，右に進めていって，xより小さいa[j]があったらxを更新する
# xがiからj個あるということなので，x*(j-i+1)でansを更新していく

# ------------------- Answer --------------------
code:python

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        now = a[i]
        for j in range(i, n):
            if now <= a[j]:
                ans = max(ans, now * (j - i + 1))
            else:
                now = a[j]
    print(ans)

    # きれいに書く
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans = max(ans, x*(j-i+1))
    print(ans)



# ------------------ Sample Input -------------------
5
1 2 3 2 3

6
2 4 4 9 4 9

7
2 4 4 9 1 4 9

10
2 2 3 1 1 1 1 1 1 1

18

6
200 4 4 9 4 9


# ----------------- Length of time ------------------
# 30分以上

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc189/editorial
# この問題は，ヒストグラムとしてみなして，その中から最大の長方形を探す問題と捉えることができる
# 最大長方形というおもろいアルゴリズムを使えばO(N)で解けるらしい
# こんな変な制約の問題みたことない。とても変な問題。

# ----------------- Category ------------------
#AtCoder
#ABC-C
#最大長方形
#10**4
#全探索