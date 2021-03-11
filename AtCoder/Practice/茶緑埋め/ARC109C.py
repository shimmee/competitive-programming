# ARC109C - Large RPS Tournament
# URL: https://atcoder.jp/contests/arc109/tasks/arc109_c
# Date: 2021/03/09

# ---------- Ideas ----------
# 2**100人いるのでシミュレーションはできない
# i%mod+1とか書いてるけど，単純に2**k人にsを左から順繰りに当てはめていくだけ: 各人の手は簡単に定まる
# あいこのときは左の人が勝つ: というか手だけ知りたいから，手が勝ち残るだけ
# 規則性がありそうだから，簡単に解けるのだろう
# 試合数はkに依存: k=1は1試合, k=2は3試合，k=3は7試合，一般に2**k-1試合
# brute forceは愚直にシミュレーション
# kが大きかったとしても，nが100以下なので，一番下のブロックでは同じ形の試合がたくさんあるのではないか？周期性
# 戦うのはsの中の隣り合う2人: 第一回戦で勝つのはわかる: kが偶数ならsを1回で周回，kが奇数なら2回で周回


# ------------------- Solution --------------------
# 解説見ました
# sを偶数にするために，s=s*2として扱う
# 1回戦目はこの新しいsが連続したものと見なせるが，この勝者は単純にsの中で対決させた勝者が並ぶことになる
# 勝者の人々をtすると，2回戦目は手がtの人たちが戦うことになるので，同様にs=t*2として第二回戦を行う
# これをk回シミュレーションしたとき，優勝者はtの最初に来ることになる
# n=3, k=3, s='RPS'のとき, s=s*2='RPSRPS', t='PRS'
# 参考: https://scrapbox.io/procon-kirokuyou/ARC109_C_-_Large_RPS_Tournament_(500)
# 「Sの勝敗結果から作った文字列をTとすると、次の階層の試合結果はTを必要な長さ分繰り返したものになる」

# ------------------- Answer --------------------
#code:python
def janken(a, b):
    if a == b: return a
    elif (a == 'R' and b == 'P') or (a == 'P' and b == 'R'): return 'P'
    elif (a == 'R' and b == 'S') or (a == 'S' and b == 'R'): return 'R'
    elif (a == 'S' and b == 'P') or (a == 'P' and b == 'S'): return 'S'

n, k = map(int, input().split())
s = input()
s = s*2

for _ in range(k):
    t = ''
    for i in range(0, len(s), 2):
        t += janken(s[i], s[i+1])
    s = t*2
print(s[0])


# ------------------ Sample Input -------------------
11 1
RPSSPRSPPRS


# ----------------- Length of time ------------------
# 1時間かけて解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc109/editorial
# 「kが偶数ならsを1回で周回，kが奇数なら2回で周回」という点までは思いついていたが，
# 単純に2*sをk回シミュレーションすればいいということは思いつかなかった
# DPで解けるらしく，DPで解くとなると難易度が高そうだけど，今回の想定解法だと緑diffで納得はいく

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#ARC-C
#緑diff
#再帰的に上位桁から順に値で分類した木を作る
#循環するものを二周させる
#数珠
#操作列が文字列で与えられる
#ジャンケン
#トーナメント