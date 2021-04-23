# 典型90問021 - Come Back in One Piece（★5）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_u
# Date: 2021/04/22

# ---------- Ideas ----------
# サイクルごとに分解して，各サイクルに属する頂点数を数えて組み合わせ数を数えれば良さそう
# 強連結成分分解(scc)という便利なアルゴリズムがあった
# scipyの関数を使えば自前実装より速いっぽい

# ------------------- Answer --------------------
#code:python
# scipyを用いた強連結成分分解(scc)
# 参考: https://kawap23.hatenablog.com/entry/2019/10/06/143159
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

# 入力のグラフ受け取り: n頂点，m辺
n, m = map(int, input().split())
edge = np.array([input().split() for _ in range(m)], dtype = np.int64).T

# グラフをscipy用の疎行列に変換
graph = np.ones(m, dtype = np.int64).T
graph = csr_matrix((graph, (edge[:] -1)), (n, n))

# 強連結成分分解の実行
scc_res = connected_components(graph, directed = True, connection = 'strong')
# n=4, m=7のとき以下の結果を得たとする scc_res: (2, array([1, 1, 0, 1], dtype=int32))
# これは頂点1,2,4が同じグループ1で，頂点3はグループ0に属し，全部で2グループあることを表している

# あとはグループ内の組み合わせ数を数えるだけ
from collections import Counter
ans = 0
for key, value in Counter(scc_res[1]).items():
    if value >= 2:
        ans += value*(value-1)//2
print(ans)

# ------------------ Sample Input -------------------
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3

# ----------------- Length of time ------------------
# ググるの含めて30分

# -------------- Editorial / my impression -------------
# 便利なアルゴリズムだった
# 内部ではdfsを2回やってる感じ

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#scc
#強連結成分分解
#サイクルの個数
#サイクルに属する頂点数