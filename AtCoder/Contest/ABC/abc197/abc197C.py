# ABC197C - ORXOR
# URL: https://atcoder.jp/contests/abc197/tasks/abc197_c
# Date: 2021/03/27

# ---------- Ideas ----------
# 数列の間に仕切りを入れていく: 最大n-1個入れられる
# n<=20なので，1個からn-1個の仕切りを入れるの全探索する
# 1からn-1のループ走査し，仕切りの個数を固定し，仕切りの場所をitertools.combinationsで仕切りの場所を固定する

# 仕切りのインデックスで数列Aを分割する方法: https://www.geeksforgeeks.org/python-custom-list-split/


# ------------------- Answer --------------------
#code:python
from itertools import combinations, chain
n = int(input())
A = list(map(int, input().split()))

def split_list_with_index(target_list, index_list):
    """

    :param target_list:  [0,1,2,3,4,5,6,7,8,9,10]
    :param index_list: [2, 5]
    :return: [[0, 1], [2, 3, 4], [5, 6, 7, 8, 9, 10]]
    """

    temp = zip(chain([0], index_list), chain(index_list, [None]))
    target_list_split = list(target_list[i: j] for i, j in temp)

    return target_list_split

if n == 1:
    print(A[0])
    exit()

opt = [i for i in range(1, n)] # 仕切りを置けるn-1個の候補すべて
ans = 10**20
for i in range(1, n): # i回切って，i+1個のグループに分ける
    all_pattern = list(combinations(opt, i)) # i回切る時の分け方のパターン
    for pattern in all_pattern:
        xor = 0
        divided_A = split_list_with_index(A, pattern) # Aを分割してlist in listにする
        for l in divided_A:
            or_res = 0
            for a in l:
                or_res = or_res | a
            xor ^= or_res
        ans = min(ans, xor)

print(ans)


# ------------------ Sample Input -------------------
1
0

20
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

3
1 5 7

4
1 5 7 9




# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# 組み合わせ全探索で解いたけど，bit全探索が想定解法だった
# n-1個の仕切りを入れるか入れないかで2**(n-1)のbit全探索

# ----------------- Category ------------------
#AtCoder
#緑diff
#bit全探索
#組み合わせ全探索
#split_list_with_index