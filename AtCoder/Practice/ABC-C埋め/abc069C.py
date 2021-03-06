# ABC069C - 4-adjacent
# URL: https://atcoder.jp/contests/arc080/tasks/arc080_a
# 日付: 2020/12/15

# ---------- 思ったこと / 気づいたこと ----------
# 2の倍数は2つ隣り合えばOKだけど，奇数と並んだらだめ

# ------------------- 方針 --------------------
# 数列の数字を「4の倍数」「4の倍数ではない2の倍数」「奇数」に分けて，それぞれの出現回数をカウントする
# 2の倍数の個数が偶数のとき，互いに打ち消し会えるので，4の倍数と奇数の個数だけ比べればいい
# -> 4の倍数の個数 + 1が奇数の個数以上であればOK
# 2の倍数の個数が奇数のとき，余った2の倍数は奇数と同じにみなせるので，奇数が1つ多いと考える
# -> 4の倍数の個数が奇数の個数以上であればOK

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

k4 = 0 # 4の倍数の個数
k2 = 0 # 4の倍数でなくて偶数の個数
odd = 0 # 奇数の個数
for i in range(n):
    if a[i] % 4 == 0: k4 += 1
    elif a[i] % 2 == 0: k2 += 1
    else: odd += 1

# 2の倍数の個数が偶数のとき，互いに打ち消し会えるので，4の倍数と奇数の個数だけ比べればいい
if k2 % 2 == 0:
    if k4+1 >= odd:
        print('Yes')
    else:
        print('No')
else: # 2の倍数の個数が奇数のとき，余った2の倍数は奇数と同じにみなせるの
    if k4 >= odd:
        print('Yes')
    else:
        print('No')

# ------------------ 入力例 -------------------
3
1 10 100

4
1 2 3 4

3
1 4 1

2
1 1

6
2 7 1 8 2 8

# ----------------- 解答時間 ------------------
# 16分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc080/editorial.pdf
# 割と複雑な考察が必要なのに解説通りに解けててとても嬉しい

# ----------------- カテゴリ ------------------
#AtCoder #abc
#倍数
#偶奇に注目
