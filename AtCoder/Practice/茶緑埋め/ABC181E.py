# ABC181E - Transformable Teacher
# URL: https://atcoder.jp/contests/abc181/tasks/abc181_e
# Date: 2021/02/28

# ---------- Ideas ----------
# たぶん事前計算とソート二分探索で行ける
# ペアになるのは自分の左の人か右の人なので，
# 変態が挿入される位置によって，ペアが変わる
# 先生は，奇数番号のやつと必ず組むことになる
#

# ------------------- Solution --------------------
# 0項目からn-1項目までの2項ずつの差をgap_oddとする
# 1項目からn項目までの2項ずつの差をgap_evenとする
# これらの累積和を求める: gap_odd_cum, gap_even_cum
# 先生の変態をmループする
# 先生を挿入するインデックスをhの中から二分探索で見つける
# インデックスが偶数の時，先生は右のやつと組む，奇数のときは左のやつと組む。これらを場合分け
# 先生より左にいる子達の差の和 (gap_odd_cum) + 先生と生徒の差 + 先生より右にいる子達の差の和 (gap_even_cum)

# ------------------- Answer --------------------
#code:python
import bisect
from itertools import accumulate
n, m = map(int, input().split())
h = sorted(list(map(int, input().split())))
w = sorted(list(map(int, input().split())))

gap_odd = []
gap_even = []
for i in range(0, n-1, 2):
    gap_odd.append(abs(h[i] - h[i+1]))
    gap_even.append(abs(h[i+1] - h[i+2]))

gap_odd_cum = [0] + list(accumulate(gap_odd))
gap_even_cum = [0] + list(accumulate(gap_even))

ans = 10**20
for i in range(m):
    idx = bisect.bisect_right(h, w[i]) # 先生が入る場所
    cnt = 0
    if idx % 2 == 0: # 先生は1つ右の人と組む: idxの人
        cnt += gap_odd_cum[idx//2] # 先生の直前までの人は，普通にペアを作る
        cnt += abs(w[i] - h[idx]) # 先生は右の人とペアを組む
        cnt += gap_even_cum[(n-1)//2] - gap_even_cum[idx//2]
        ans = min(ans, cnt)
    else: # 先生は1つ左の人と組む: idx-1の人
        cnt += gap_odd_cum[(idx-1)//2] # 先生とペアを組む人の直前までの人は，普通にペアを作る
        cnt += abs(w[i] - h[idx-1]) # 先生は左の人とペアを組む
        cnt += gap_even_cum[(n-1)//2] - gap_even_cum[(idx-1)//2]
        ans = min(ans, cnt)
print(ans)


# ------------------ Sample Input -------------------
7 3
1 2 4 7 10 14 19
3 7 11

7 5
2 4 6 8 10 12 14
1 3 5 7 9

5 3
1 2 3 4 7
1 3 8

7 7
31 60 84 23 16 13 32
96 80 73 76 87 57 29


# ----------------- Length of time ------------------
# 38分でAC!!!

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc181/editorial
# 最近のABCのdiff1993を初見で解けたのはめちゃ嬉しい
# 問題をみて10秒くらいでざっくりした解法を思いついた
#

# ----------------- Category ------------------
#AtCoder
#二分探索
#ソートして二分探索
#binary_search
#累積和
#ABC-E
#緑diff
#N個のものうち1個を変更・削除したものを解く
#前処理
#左右両端からの結果を前処理
#ソート
#差分更新
#クエリ処理問題
#lower_bound
#数列
#二分探索で挿入する