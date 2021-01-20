# AGC034A - Kenken Race
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc034/tasks/agc034_a
# 日付: 2020/12/31

# ---------- 思ったこと / 気づいたこと ----------
# だめな条件を上げる
# スタートとゴールの間に岩が連続で2個ある
# 場合分け3種類ある

# ------------------- 方針 --------------------
# A < C < B < Dのとき，AとCの間，BとDの間に##がなければOK
# A < B < C < Dのとき，AとDの間に##がなければOK
# A < B < D < Cのとき，AとCの間に##がなくて，かつB-1からとD+1の間に...がある

# ------------------- 解答 --------------------
#code:python
n, a, b ,c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
S = input()

if a < c < b < d:
    for i in range(n-1):
        if (a < i < c or b < i < d) and S[i]+S[i+1] == '##':
            print('No')
            exit()
    print('Yes')
elif a < b < c < d:
    for i in range(n - 1):
        if a < i < d and S[i] + S[i + 1] == '##':
            print('No')
            exit()
    print('Yes')
elif a < b < d < c:
    flag = False
    for i in range(n - 1):
        if a < i < c and S[i] + S[i + 1] == '##':
            print('No')
            exit()
        if b <= i <= d and S[i - 1] + S[i] + S[i + 1] == '...': # ここがポイント！！！
            flag = True
    if flag: print('Yes')
    else: print('No')



# ------------------ 入力例 -------------------
7 1 3 6 7
.#..#..

7 1 3 7 6
.#..#..

15 1 3 15 13
...#.#...#.#...

# ----------------- 解答時間 ------------------
# 35分

# -------------- 解説 / 感想 / 反省 -------------
# 解説: https://img.atcoder.jp/agc034/editorial.pdf
# C < Dのときは2マス連続岩があるとだめ
# D < CのときはBからDのどこかに...がある必要あり

# この解説，A<C<B<Dのパターンを無視してないか？

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium