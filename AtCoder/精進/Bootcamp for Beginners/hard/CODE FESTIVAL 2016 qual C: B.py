# CODE FESTIVAL 2016 qual C: B - K個のケーキ
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b
# Date: 2021/01/15

# ---------- Ideas ---------- 
# 数が多いケーキは最初と最後に?
# 自分と自分以外の数の個数の差に注目
# 連続しないように並べる: 個数の差に注目!!!

# にてる問題がある!: CODE FESTIVAL 2016 qual C: B

# ------------------- Solution -------------------- 
# i番目ケーキの個数とa[i]とそれ以外のケーキの個数のトータルを比べて，
# それ以外のトータルの方が多かったら，i番目が連続することはないけど，
# a[i]の方が多かったら，多かった分だけ連続させざるを得ない。
# これを1つずつ見ていく

# ------------------- Answer --------------------
#code:python
k, t = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)

ans = 0
for a in A:
    other = total - a
    ans += max(0, a-other-1)
print(ans)

# ------------------ Sample Input -------------------
7 3
3 2 2

6 3
1 4 1

100 1
100

# ----------------- Length of time ------------------
# 14分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/other/code-festival-2016-qualc/editorial.pdf
# 似たような問題を思い出せたおかげで解けた！！
# 解説通り!
# ヒープつかって貪欲にも解けるらしい。

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#連続しないように並べる
#個数の差に注目
