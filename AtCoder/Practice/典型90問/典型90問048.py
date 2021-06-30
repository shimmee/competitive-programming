# 典型90問048 - I will not drop out（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_av
# Date: 2021/05/24

# ---------- Ideas ----------
# 2分の満点を，1分部分点からの追加点と考えて，違う問題と見なす
# ソートして貪欲

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]
l = []
for i in range(n):
    a, b = ab[i]
    l.append(b)
    l.append(a-b)

l.sort(reverse=True)
print(sum(l[:k]))


# ------------------ Sample Input -------------------
4 3
4 3
9 5
15 8
8 6

10 12
987753612 748826789
36950727 36005047
961239509 808587458
905633062 623962559
940964276 685396947
959540552 928301562
60467784 37828572
953685176 482123245
87983282 66762644
912605260 709048491
# ----------------- Length of time ------------------
# 10分くらい?

# -------------- Editorial / my impression -------------
# 思いつくのに案外時間がかかった
# どう貪欲するかがポイント
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/048.jpg

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#ソートして貪欲
#貪欲
#上階と下界を見積もる