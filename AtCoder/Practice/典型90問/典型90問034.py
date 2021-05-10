# 典型90問034 - There are few types of elements
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ah
# Date: 2021/05/06

# ---------- Ideas ----------
# 典型的なしゃくとり法！
# バグらせずスクラッチで書けるかな？

# ------------------- Answer --------------------
#code:python
from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

kinds = set() # leftからrightまでの数字の種類の保管
counter = defaultdict(int) # leftからrightまでに出現してる各数字の個数

# 初期化
right = 0
kinds.add(a[right])
counter[a[right]] += 1

ans = 1
for left in range(n):

    # 行けるところまで右に行く: 今k種類揃ってて，次の右がそのk種類に入ってなかったら進めない
    while right < n-1 and not (len(kinds) == k and not a[right+1] in kinds):
        right += 1
        kinds.add(a[right])
        counter[a[right]] += 1

    # 現在の長さでans更新
    ans = max(ans, right-left+1)

    if left == right:
        right += 1
    else:
        # 次に左が1つ進むので，counterの個数を減らす。個数が0になってたらkindsからも消す
        counter[a[left]] -= 1
        if counter[a[left]] == 0:
            kinds.remove(a[left])

print(ans)

# 最悪計算量?
n = 10**5
k = 1
a = [10**9+i for i in range(10**5)]

# ------------------ Sample Input -------------------

5 1
1 2 3 4 5

5 4
1 1 2 4 2

10 2
1 2 3 4 4 3 2 1 2 3

4 2
1 3 1 2

# ----------------- Length of time ------------------
# 26分

# -------------- Editorial / my impression -------------
# あってた！！
# スクラッチで書けたのがとても嬉しい

# ----------------- Category ------------------
#AtCoder
#尺取法
#しゃくとり法
#連続部分列
#典型90問