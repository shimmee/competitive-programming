# ABC171E - Red Scarf
# URL: https://atcoder.jp/contests/abc171/tasks/abc171_e
# Date: 2021/02/15

# ---------- Ideas ----------
# x[i] はa[i]以外のxor和で表せる
# まず全てのiに関するxor和(total_xor)を求めて，ループでtotal_xor^a[i]としてx[i]を求める
# 累積XORっぽい感じ?

# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

total_xor = 0
for a in A:
    total_xor ^= a

ans = []
for a in A:
    ans.append(total_xor^a)

print(*ans)
# ------------------ Sample Input -------------------
4
20 11 9 24

#-> 26 5 7 22


3
7 10 4

14 3 13


# ----------------- Length of time ------------------
# 18分

# -------------- Editorial / my impression -------------
# https://drken1215.hatenablog.com/entry/2020/06/22/122500
# XORの問題をまともに解けてとても嬉しい。
# E問題だったから茶上位だったけど，D問題だったらもっと正答率高くてdiff低そう

# ----------------- Category ------------------
#AtCoder
#ABC-E
#排他的論理和
#XORの性質
#パリティ
#方程式
#連立一次方程式
#対称性
#数列
#式変形
#茶diff
