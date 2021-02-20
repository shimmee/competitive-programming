# 三井住友信託銀行プログラミングコンテスト2019: E - Colorful Hats 2
# URL: https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e
# Date: 2021/02/18

# ---------- Ideas ----------
# 樹形図が対象なのがポイント
# 色のパターンを勝手に固定する
# 3色が出現した回数を数えるリストを用意する
# 例えば[2,2,1] であればrが2，gが2，bが1回出現しており，a[i]=2であれば，rとgが当てはまるので，2をかける
# a[i]=2なので，リストを[2,2,1]から[3,2,1]か[2,3,1]に更新する

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n = int(input())
A = list(map(int, input().split()))

cnt = [0, 0, 0]
ans = 1
for i in range(n):
    a = A[i]
    c = cnt.count(a)
    if c == 0:
        print(0); exit()
    ans = ans * c % mod
    idx = cnt.index(a)
    cnt[idx] += 1
print(ans)


# ------------------ Sample Input -------------------
54
0 0 1 0 1 2 1 2 3 2 3 3 4 4 5 4 6 5 7 8 5 6 6 7 7 8 8 9 9 10 10 11 9 12 10 13 14 11 11 12 12 13 13 14 14 15 15 15 16 16 16 17 17 17

# ----------------- Length of time ------------------
# 30分AC!!!!!

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/sumitrust2019/editorial.pdf
# 勝手にパターンを固定するのがポイントだった
# E問題だから緑上位なだけであって，D問題だったらもう少しdiff低そう


# ----------------- Category ------------------
#AtCoder
#数え上げ問題
#樹形図
#パターンを固定する
#緑diff
#500点問題