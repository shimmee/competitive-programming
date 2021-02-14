# ARC006C - 積み重ね
# URL: https://atcoder.jp/contests/arc006/tasks/arc006_3
# Date: 2021/02/13

# ---------- Ideas ----------
# n<=50なのでどうとでもなる
# 貪欲でいいかも
# 各山の一番上の重さ要素とするリストを持つ
# 今載せたいものが山の一番上にいるダンボール以下でかつ差が小さいところに置いていけばいい
# 毎回ソートすればいい


# ------------------- Answer --------------------
#code:python
n = int(input())
load = [int(input())]
for _ in range(n-1):
    w = int(input())
    load.sort()
    for j in range(len(load)):
        if load[j] >= w:
            load[j] = w
            break
    else:
        load.append(w)
print(len(load))

# ------------------ Sample Input -------------------

5
4
3
1
2
1

7
93
249
150
958
442
391
25

# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/12/25/185948
# 貪欲で解けないやんとおもって考え込んでしまった。貪欲で解けた。

# ----------------- Category ------------------
#AtCoder
#greedy
#緑diff
#貪欲
#ソート