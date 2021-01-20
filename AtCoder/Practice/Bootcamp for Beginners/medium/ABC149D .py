# ABC149D - Prediction and Restriction
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc149/tasks/abc149_d
# Date: 2021/01/04

# ---------- Ideas ----------
# Use greedy algorithm. But in terms of what?



# ------------------- Answer --------------------
#code:python

n, k = map(int, input().split())
point = list(map(int, input().split()))
point = {'rsp'[i]: point[i] for i in range(3)}
win_hand = {'r': 'p', 's': 'r', 'p': 's'} # key: machine hand, value: takahashi's hand
T = input()
T = [i for i in T]

ans = 0
for i in range(n):
    machine = T[i] # win_hand
    takahashi = win_hand[machine] # takahashi's hand to beat the machine
    if k > i: # if i is less than k, takahashi can use any hand to win
        ans += point[takahashi]
    else:
        if T[i] == T[i-k]: # if current i-th  hand is same as (i-k)-th
            if i + k < n: # if takahashi still has another rounds more than k
                if T[i] == T[i+k]:  # try to avoid same hand with the next hand at (i+k)-th
                    T[i] = win_hand[T[i]]  # rewrite with other win_hand
                else:
                    T[i] = 'rsp'.replace(T[i], '').replace(T[i+k], '') #
            else:
                T[i] = win_hand[T[i]] # rewrite with other win_hand
        else:
            ans += point[takahashi]
print(ans)


# ------------------ Sample Input -------------------
5 2
8 7 6
rsrpr

7 1
100 10 1
ssssppr


30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr

# ----------------- Length of time ------------------
# 27 min

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc149/editorial.pdf
# This can be solved by DP or greedy algorithm
# It was fun but took me more time than I expected

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#greedy