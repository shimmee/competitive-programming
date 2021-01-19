# ARC111 B -
# URL: https://atcoder.jp/contests/arc111/tasks/arc111_b
# Date: 2021/01/09

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
ab = [[int(i) for i in input().split()] for _ in range(n)]


from collections import Counter
dict_a = Counter([i[0] for i in ab])
dict_b = Counter([i[1] for i in ab])

for a, b in ab:
    b_freq_in_a = dict[b]
    if dict[b] == 0 and dict[a] >= 2: # bがdictになくて，かつaが2個以上あればaとbをスイッチ
        dict[b] = 1
        dict[a] = dict[a]-1

print(len(dict))



flag = [False]*400001
for a, b  in ab:
    flag[a] = True





# ------------------ Sample Input -------------------
4
1 2
1 3
4 2
2 3

2
111 111
111 111

12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ARC111
#AC_with_editorial #解説AC
#wanna_review #medium復習
