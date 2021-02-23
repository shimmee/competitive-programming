# ABC109D - Make Them Even
# URL: https://atcoder.jp/contests/abc109/tasks/abc109_d
# Date: 2021/02/22

# ---------- Ideas ----------
# 「コインを満遍なく散らばらせて，偶数枚のコインを持つマスの個数を最大にしてね」
# 0枚のマスも偶数枚として扱われる
# まず，「最終的に何マスを偶数枚にできるのか」を事前に計算する必要はあるのか？
# というか，総数が偶数のときは必ず全て偶数にできそう
# ジャバラのようにウネウネ，ジグザグに一筆書き動かせばかならず行ける
# 奇数があったら次のマスにわたす！

# ------------------- Solution --------------------
# まず最初に偶数番目の行を反転させる: ジグザグをバグらせないため
# ジャバラに進む
# 奇数マスがあれば，それを持ってどんどん進む，奇数マスに当たれば，そこに放置して，進む


# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(h)]

move = []
for y in range(h):
    if y % 2 == 0:  # 奇数行目のとき左から右に進む
        for x in range(w):
            if y == h-1 and x == w-1: # 最後のマスだったら終わり
                continue
            if A[y][x] % 2 == 1: # 奇数を発見
                if x == w-1: # 右端にいるなら下に降りる
                    move.append([y, x, y + 1, x])
                    A[y + 1][x] += 1
                else: # それ以外なら右のマスに渡す
                    move.append([y, x, y, x + 1])
                    A[y][x + 1] += 1
    else: # 偶数行目のとき，右から左に進む
        for x in reversed(range(w)):
            if y == h-1 and x == 0: # 最後のマスだったら終わり
                continue
            if A[y][x] % 2 == 1: # 奇数を発見
                if x == 0: # 左端にいるなら下に降りる
                    move.append([y, x, y + 1, x])
                    A[y + 1][x] += 1
                else: # それ以外なら右のマスに渡す
                    move.append([y, x, y, x - 1])
                    A[y][x - 1] += 1
print(len(move))
for m in move: # 1-indexedにして出力
    print(*[i + 1 for i in m])


# ------------------ Sample Input -------------------
3 2
1 0
2 1
1 0

2 3
1 2 3
0 1 1


# ----------------- Length of time ------------------
# 45分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc109/editorial.pdf
# なぜかジグザグに気づけた
# 超楽しかった
# ARC080D - Grid Coloringと同じ感じだった！

# ----------------- Category ------------------
#AtCoder
#一筆書き
#ジグザグ
#ウネウネ
#経路復元
#グリッド
#構築問題
#ABC-D
#緑diff
#パリティ
