# Educational DP Contest: K - Stones
# URL: https://atcoder.jp/contests/dp/tasks/dp_k
# 日付: 2020/12/25

# ---------- 思ったこと / 気づいたこと ----------
# Nimっぽい
# grundy数で解ける

# ------------------- 方針 --------------------
# 2重ループ O(NK)で解ける
# dp[i]: 残りの石がi個のときのgrundy数

# ------------------- 解答 --------------------
code:python
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = min(a)
    option = set([i for i in range(n+1)])

    dp = [-1]*(k+1)
    for i in range(k+1): # 残りの石の数
        if i < m:
            dp[i] = 0
        else:
            next_grundy = set([]) # 次の状態のgrundy数の集合を溜め込む
            for j in range(n): # 選択肢の集合(a)のインデックス: 取り除く石はa[j]個
                if i-a[j]>=0: # 残りの石i - 取り除く石a[j]は0以上の必要がある
                    next_grundy.add(dp[i-a[j]])

            # 現在の状態におけるgrundy数は，次の状態のgrundyの集合に含まれない最小の非負整数(mex)
            grundy = min(option-next_grundy) # 現在の状態iにおけるgrundy数
            dp[i] = grundy

    if dp[k] == 0:
        print('Second')
    else:
        print('First')

# ------------------ 入力例 -------------------
2 4
2 3
# First

2 5
2 3
# Second

2 7
2 3
# First

3 20
1 2 3
# Second

3 21
1 2 3
# First

1 100000
1
# Second
# ----------------- 解答時間 ------------------
# 18分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.creativ.xyz/dp-practice/
# 初めて所見で解けたgrundy数！！！
# 解説はシンプルに「自分の手番で状態を “負け状態” に変えられるなら、その状態は “勝ち状態” である」とかいてる

# ----------------- カテゴリ ------------------
#EDPC
#動的計画法
#DP
#grundy数