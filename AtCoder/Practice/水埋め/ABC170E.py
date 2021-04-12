# ABC170E - Smart Infants
# URL: https://atcoder.jp/contests/abc170/tasks/abc170_e
# Date: 2021/04/06
1140
# ---------- Ideas ----------
# リスト1: aとbの入力そのまま (二次元配列)
# リスト2: 各クラスがインデックスを表して，クラスに属する子のレート (二次元)
#
# クエリごとに2つめのリストを更新できたら一番嬉しくて，
# ・リスト2の移動元から値を消す: O(logN)
# ・リスト2の移動先に値を入れる: O(logN)
# ・リスト2の移動元と移動先の最大を更新: O(logN)
# ・全体の最小を更新: O(1)

# 最小値(ans_min)が更新されるのはいつか？
# 移動元のmaxがans_minのとき
# - 移動する子がmax (つまりans_min)のとき，
#   - 1人しかいなければ，ans_minを計算し直す? O(N)
#   - 2人以上いれば，移動元の2番目に大きいレートがans_minになる
# - 移動する子がmaxではないとき，
#   - 移動先のmaxがans_minなら，ans_minを計算し直す? O(N)

# 移動元のmaxがans_minではないとき
# - 移動する子が移動元の幼稚園内でmaxのとき，
#   -
#  - 移動元でmaxじゃない子が，移動先でmaxになる: 移動先が更新の候補
# 移動元でmaxの子が，移動先でmaxではない: 移動元が更新の候補
# 移動元でmax, 移動先でもmaxになる: 移動元が更新の候補

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
import heapq
n, q = map(int, input().split())
m = 2*10**5
ab = []
school = [[] for _ in range(2*10**5)]  # インデックスが幼稚園番号(0-index),

for i in range(n):
    a, b = map(int, input().split())
    b -= 1 # 幼稚園を0-indexに
    ab.append([a, b])
    heapq.heappush(school[b], -a)

school_max = [] # 各幼稚園の最大レートのリスト
for i in range(m):
    if school[i]:
        max_a = heapq.heappop(school[i]) * (-1) # 最大値を取り出す
        school_max.append(max_a)
        heapq.heappush(school[i], -max_a)

ans_min = min(school_max)
for _ in range(q):
    c, d = map(int, input().split())

    c -= 1 # 幼児番号
    a, b = ab[c] # レートと今の幼稚園

    rate1_from = heapq.heappop(school[b]) * (-1) # 移動元の幼稚園の最高レート
    rate1_to = heapq.heappop(school[d]) * (-1)  # 移動先の幼稚園の最高レート


    if a > max_rate_to: # 移動先でmaxになる場合，移動先が更新の候補
        ans = min(ans_min, a)



    ab[c] = [a, d] # 次の幼稚園に移動させる






# ------------------ Sample Input -------------------
6 3
8 1
6 2
9 3
1 1
2 2
1 3
4 3
2 1
1 2


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
