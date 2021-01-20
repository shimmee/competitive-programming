# ABC140C-Maximal Value
# URL: https://atcoder.jp/contests/abc140/tasks/abc140_c
# 日付: 2020/11/25

# ------------------- 方針 --------------------
# A[n]=B[n-1]
# A[n-1]=min(B[n-1], A[n])
# この漸化式で解けそう。N<=100なのでループが回る


# ------------------- 解答 --------------------
#code:python
n=int(input())
B=list(map(int, input().split()))
B = B[::-1] # reverse
A = [0]*n
A[0] = B[0]
for i in range(1, n-1):
    A[i] = min(B[i], A[i-1])
A[n-1] = A[n-2]
print(sum(A))

# これで半分WAになったので，おそらく解法が間違えている
# 解説みた
# A[i] = min(B[i-1], B[i])

n=int(input())
B=list(map(int, input().split()))
A = [0]*n
A[0] = B[0]
for i in range(1, n-1):
    A[i] = min(B[i-1], B[i])
A[n-1] = B[n-2]
print(sum(A))

# ------------------ 入力例 -------------------
6
0 153 10 10 23

2
3

3
2 5


# ----------------- 解答時間 ------------------
# 半分WAだったので解法が間違えてることに気づいて解説みた

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc140/editorial.pdf
# とく方向が逆だった。後ろからじゃなくて前からminを取っていく


# ----------------- カテゴリ ------------------
#AtCoder #abc
#
