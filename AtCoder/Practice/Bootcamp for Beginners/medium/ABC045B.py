# ABC045B - 3人でカードゲームイージー
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc045/tasks/abc045_b
# Date: 2021/01/01


# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# Convert abc to 012 to uniform their names and numbers in their cards
#

# ------------------- Answer --------------------
#code:python
from collections import deque
S = [input() for _ in range(3)]
cards = [[] for _ in range(3)]
for i in range(3):
    s = S[i]
    for j in range(len(s)):
        if s[j] == 'a': cards[i].append(0)
        if s[j] == 'b': cards[i].append(1)
        if s[j] == 'c': cards[i].append(2)
cards = deque(cards)

turn = 0
while True:
    if len(cards[turn]) == 0:
        ans = turn
        break
    turn = cards[turn].popleft()

if ans == 0: print('A')
elif ans == 1: print('B')
elif ans == 2: print('C')


# More efficient answer using dictionary: https://atcoder.jp/contests/abc045/submissions/7992008

S = {i:list(input()) for i in "abc"}
turn = 'a'
while S[turn]:
    turn = S[turn].pop(0)
print(turn.upper())


# ------------------ Input example -------------------
aca
accc
ca

abcb
aacb
bccc


# ----------------- Length of time ------------------
# 30 min

# -------------- Editorial / my impression -------------
# Because of using deque.pop() instead of popleft(), the last card in their hand was picked up.
# I should have used dictionary instead of converting from abc to 012

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#wanna_review #medium復習