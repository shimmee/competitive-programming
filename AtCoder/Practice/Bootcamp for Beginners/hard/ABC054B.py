# ABC054B - Template Matching
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc054/tasks/abc054_b
# Date: 2021/01/13

# ---------- Ideas ---------- 
# Aの左上からm*mを切り取ってBに一致するか調べる
# 左上さえ固定すれば，m*mは決まる:n-
#

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

for y in range(n-m+1):
    for x in range(n-m+1):

        # Aのマス(x,y)から左下に向かうm*mの正方形のマスを切り取る
        # 左上(x, y), 右上(x+m, y), 左下(x, y+m), 右下(x+m, y+m)
        mm = [A[y+i][x:x+m] for i in range(m)]

        # Bがmmに一致するか調べる。
        flag = True
        for i in range(m):
            for j in range(m):
                if B[i][j] != mm[i][j]:
                    flag = False
        if flag:
            print('Yes')
            exit()
print('No')
# ------------------ Sample Input -------------------

3 2
#.#
.#.
#.#
#.
.#

4 1
....
....
....
....
#


# ----------------- Length of time ------------------
# 11分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc054/editorial.pdf
# 中の内包表記がなくても，単純な4重ループで書ける

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#画像処理
#マスの一致
#4重ループ
#グリッド
#grid
