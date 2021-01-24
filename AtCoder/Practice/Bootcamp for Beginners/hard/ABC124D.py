# ABC124D - Handstand
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc124/tasks/abc124_d
# Date: 2021/01/23

# ---------- Ideas ----------
# 超有名問題やん?
# 少なくともしゃくとり法では解けそう
# 反転するlrの区間を，数字がまたぐようにとっても意味がなさそう
# groupby使えばいけそう
# 連続した0を1にしたい
# 根本のアイデア: 0の塊をk回連続取ってみて，最長のものをキープする

# ------------------- Solution --------------------
# groupbyで連続した0と1を数える: 直立している人はマイナスをつける
# 0と1の個数の累積和を出す
# 累積和から，インデックス上手いこと使って答え出す

# ------------------- Answer --------------------
code:python
    from itertools import groupby
    n, k = map(int, input().split())
    S = input()

    # groupbyで連続した0と1を数える
    gr = groupby(S)
    l = []
    for key, group in gr:
        if key == '1':
            l.append(len(list(group)))
        if key == '0': # 直立してるひと
            l.append(-len(list(group)))

    # 0と1の個数の累積和を出す
    m = len(l)
    cum = [0]*(m+1)
    neg = set([])
    for i in range(m):
        if l[i] > 0:
            cum[i+1] = cum[i] + l[i]
        else:
            cum[i + 1] = (cum[i] - l[i])
            neg.add(i+1)

    # 累積和から，インデックス上手いこと使って答え出す
    ans = 0
    for i in range(1, m+1):
        if i in neg:
            ans = max(ans, cum[min(i+2*k-1, m)] - cum[i-1])
        else:
            ans = max(ans, cum[min(i+2*k, m)] - cum[i-1])
    print(ans)


# ACになった。けっこう大変だった
# しゃくとり法でも解いてみよう
# 参考: http://fusabee.blogspot.com/2019/04/atcoder-beginner-contest-124_11.html
# やろうとしたけど諦めた


# ------------------ Sample Input -------------------
5 1
00010

14 2
11101010110011

1 1
1

# ----------------- Length of time ------------------
# 50分

# -------------- Editorial / my impression -------------
# けんちょんさん: https://drken1215.hatenablog.com/entry/2019/04/14/222900
# これがきれいに書けるっぽい？: groupbyする -> 1の個数について最初に番兵をおく -> しゃくとり使う
# 二分探索でも解けるらしい。しらんけど
#  区間ごとに分割する

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#緑diff
#しゃくとり法
#累積和
#二分探索
#操作:flip
#反転