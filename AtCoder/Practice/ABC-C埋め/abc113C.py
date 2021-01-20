# ABC113C- ID
# URL: https://atcoder.jp/contests/abc113/tasks/abc113_c
# 日付: 2020/11/23


# ------------------- 方針 --------------------
# 県ごとに全部の市に番号をふる=座標圧縮
# numpyで座標圧縮する
# http://prpr.hatenablog.jp/entry/2016/10/09/Python3%E3%81%A7%E9%85%8D%E5%88%97%E3%81%AE%E8%A6%81%E7%B4%A0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E4%BA%91%E3%80%85%E3%81%99
# 0を頭に足して出力する

# ------------------- 解答 --------------------
#code:python
import numpy as np
from scipy.stats import rankdata
n, m = map(int, input().split())
py = [[int(i) for i in input().split()] for _ in range(m)]
py = np.array(py)
# 市別のidをふる
py = np.insert(py, 0, np.array([i for i in range(m)]), axis=1)

df = np.empty((0, 4), int)
for i in range(1, n+1):
    py_i = py[py[:,1] == i]
    rank = rankdata(py_i[:,2]).astype(int)
    py_i = np.insert(py_i, 3, rank, axis=1)
    df = np.append(df, py_i, axis=0)

code = []
for i in range(m):
    code.append(str(df[i, 1]).zfill(6)+str(df[i, 3]).zfill(6))

df = df.astype(str)
df = np.insert(df, 4, np.array(code), axis=1)
df = df[df[:,0].argsort(), :]
for i in range(m):
    print(df[i, 4])

# WA!とTLE!
# 県はあっても市がないという県があるらしいから，それでWAなの？
# こんな長ったらしくnumpy使わなくてもいいっぽい
# 短めの解答: https://atcoder.jp/contests/abc113/submissions/17722674

# アイデア: ソートしてenumerateの番号で順番を表現する
# まず県数の大きさのリストpyを作る
# 入力を県番号0indexにして，入力順も一緒にpyにappendしていく受け取る
# リストのインデックスが県を表し，中身が[年, 入力順]を表してる

n, m = map(int, input().split())
ans = [0] * m
py = [[] for _ in range(n)]
for i in range(m):
    p, y = map(int, input().split())
    py[p - 1].append((y, i))

for i, j in enumerate(py):
    # iが県のループ番号
    # jが県に属する市のリスト
    j.sort() # 年でソート
    for k, (l, m) in enumerate(j):
        # kが市のループ番号
        # (l, m)は[年, 入力順]
        # kが市が生まれた順番になってるので，iとkで6桁ずつ作ればいい
        ans[m] = "%06d%06d" % (i + 1, k + 1)
for i in ans:
    print(i)
# 賢い！！！Pythonic!!!


# maspyさんの解答
# 辞書を使ってるが，アイデアは上と同じenumerate
# https://atcoder.jp/contests/abc113/submissions/6013757
from collections import defaultdict
p_to_y = defaultdict(set)

N, M = map(int, input().split())
PY = [[int(x) for x in input().split()] for _ in range(M)]
for p, y in PY:
    p_to_y[p].add(y)

def set_to_rank_dict(se):
    return {x: i for i, x in enumerate(sorted(se), 1)}

p_to_y = {p: set_to_rank_dict(se) for p, se in p_to_y.items()}
for p, y in PY:
    print('{:06g}{:06g}'.format(p, p_to_y[p][y]))



# ------------------ 入力例 -------------------
2 3
1 32
2 63
1 12
# 000001000002
# 000002000001
# 000001000001

2 3
2 55
2 77
2 99
# 000002000001
# 000002000002
# 000002000003


# ----------------- 解答時間 ------------------
# WA出した

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc113/editorial.pdf
# 他の人の解答みたら，enumerateを上手く使ってて感動した
# もう一度解くために，ACしないでおこう

# ----------------- カテゴリ ------------------
#AtCoder #abc
#座標圧縮 #pythonic #enumerate
