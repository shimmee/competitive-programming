# AGC022A - Diverse Word
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc022/tasks/agc022_a
# Date: 2021/01/07

# ---------- Ideas ----------
# 単語の桁が繰り上がるみたいなイメージ

# ------------------- Solution --------------------
# n = len(S)としたとき
# n<26なら，使われてない文字があるはずなので，一番小さい文字をSに足して出力
# n == 26のとき，後ろから見ていって[S = ...brga]のとき b <- r <- g <- a みたいに降順になってるのが終わる箇所を探す。
# この場合，bが繰り上がる。(a,g,r)のうち，bより大きい文字に繰り上がる。bがgになる。

# ------------------- Answer --------------------
code:python
    S = input()
    n = len(S)

    import string
    alpha = list(string.ascii_lowercase)
    alpha2num = lambda c: ord(c) - ord('a')

    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
    elif n == 26:
        available = [False]*26
        for i in reversed(range(26)):
            if S[i] != 'z':
                available[alpha2num(S[i])] = True
            else:
                break
        for j in range(26):
            if available[j]:
                idx = j
                break
        print(S[:i-1]+alpha[j])

    else:
        for letter in alpha:
            if not letter in S:
                print(S+letter)
                exit()

    # 諦める！次の日とく！
    # Sが26文字あるとき，次の文字は必ず25文字以下になる

    S = input()
    n = len(S)

    import string
    alpha = list(string.ascii_lowercase)
    alpha2num = lambda c: ord(c) - ord('a')

    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        exit()
    elif n < 26:
        for letter in alpha:
            if not letter in S:
                print(S+letter)
                exit()
    else:
        # Sを後ろから見ていって， w <- b <- c <- e みたいに降順になってるのが終わる箇所を探す
        available = [False] * 26
        for i in reversed(range(1, 26)):
            available[alpha2num(S[i])] = True
            if S[i-1] < S[i]: break

        for j in range(26):
            if available[j] : break
        print(S[:i-1]+alpha[j])
    # 合ってるつもりなのになぜか WAになる


    S = input()
    n = len(S)

    import string
    alpha = list(string.ascii_lowercase)
    alpha2num = lambda c: ord(c) - ord('a')

    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        exit()
    elif n < 26:
        for letter in alpha:
            if not letter in S:
                print(S+letter)
                exit()
    else:
        # Sを後ろから見ていって， w <- b <- c <- e みたいに降順になってるのが終わる箇所を探す
        for i in reversed(range(1, 26)):
            if S[i-1] < S[i]: break

        # 参考: https://atcoder.jp/contests/agc022/submissions/18174504
        # 後ろからi-1番目まで文字のうち，S[i-1]の文字より大きい文字
        t = sorted(S[i - 1:])
        idx = t.index(S[i - 1]) + 1

        print(S[:i-1]+t[idx])


# ------------------ Sample Input -------------------
abcde

abedc

abcdefghijklmnopqrstuvwxyz

atcoder
abc

abcdefghijklmnopqrstuvwzyx

# ----------------- Length of time ------------------
# 2時間

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc022/editorial.pdf
# 最後の部分でWAになったので解説と解答みた。
# 復習したい。

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#AC_with_editorial #解説AC
#wanna_review #medium復習
#辞書順