# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192): B - uNrEaDaBlE sTrInG
# URL: https://atcoder.jp/contests/abc192/tasks/abc192_b
# Date: 2021/02/20

# ---------- Ideas ----------
# islower(), isupper()で確認しながらフラッグもつ

# ------------------- Answer --------------------
#code:python
S = input()
n = len(S)
flag = True
for i in range(n):
  s = S[i]
  if i % 2 == 0: # 奇数
    if s.isupper():
      flag = False
  else:
    if s.islower():
      flag = False
print('Yes' if flag else 'No')

# ------------------ Sample Input -------------------
dIfFiCuLt

# ----------------- Length of time ------------------
# 5分

# -------------- Editorial / my impression -------------
# isupperのスペルを見慣れなさすぎてミスったりした

# ----------------- Category ------------------
#AtCoder
#ABC-B
#isupper
#islower