# 天下一プログラマーコンテスト2012 予選C: B - ロイヤルストレートフラッシュ
# URL: https://atcoder.jp/contests/tenka1-2012-qualC/tasks/tenka1_2012_10
# Date: 2021/03/04

# ---------- Ideas ----------
# 全探索する
# カードの枚数の制約がよくわからん
# ループでSから空のリストTに1枚ずつカードを入れていって，Tの中でロイヤルが完成していたらその時点でbreak
# もう一度ループを回して，royalの構成じゃないカードをansにインクリメントしていく

# ------------------- Answer --------------------
#code:python
royals = [{'S10', 'SJ', 'SQ', 'SK', 'SA'},
          {'H10', 'HJ', 'HQ', 'HK', 'HA'},
          {'D10', 'DJ', 'DQ', 'DK', 'DA'},
          {'C10', 'CJ', 'CQ', 'CK', 'CA'}]

S = input()
S = S.replace('S', ' S').replace('H', ' H').replace('D', ' D').replace('C', ' C').split()
T = []

for s in S:
    T.append(s)
    for royal in royals:
        flag = True
        for c in royal:
            if not c in T:
                flag = False
        if flag: # ロイヤルストレートラッシュが入っていれば
            break
    if flag: break

if len(T) == 5:
    print(0)
else:
    ans = ''
    for t in T:
        if not t in royal:
            ans += t
    print(ans)


# ------------------ Sample Input -------------------
CQSAS10SQH10SKSJD3

S10SJSQSKSAC2
# ----------------- Length of time ------------------
# 18分

# -------------- Editorial / my impression -------------
# 解説なかったけどたぶん合ってる。ACしたし。

# ----------------- Category ------------------
#AtCoder
#トランプ
#ロイヤルストレートフラッシュ
#文字列操作