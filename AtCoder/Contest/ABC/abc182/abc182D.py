
import sys
from io import StringIO
import unittest

# def resolve():
#     n = intput()
#     a = lint()
#
#     cum = [0]
#     for i in range(n):
#         cum.append(cum[i] + a[i])
#
#     cumcum = [0]
#     for i in range(n):
#         cumcum.append(cumcum[i] + cum[i + 1])
#
#     # 各累積の最大値
#     m_cum = [inf] * n
#     m_cum[0] = a[0]
#     for i in range(1, n):
#         m_cum[i] = max(m_cum[i - 1], m_cum[i - 1] + a[i])
#
#     ans = 0
#     for i in range(n - 1):
#         ans = max(ans, m_cum[i] + cumcum[i + 1])
#     print(ans)

# これでWAなった

# 解答見てみる: https://atcoder.jp/contests/abc182/editorial/291
# 今の座標xを0としてi=1,2,3,…,Nについて以下を行う
# rを、max(r,x+qi)で置き換える
# xをx+piで置き換える
# よくわからんが，maspyさんの解答は自分の上の解答と同じ方針でnumpyで書いてた

def resolve():
    from collections import defaultdict, deque
    from heapq import heappush, heappop
    from itertools import permutations, accumulate
    from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians
    from bisect import bisect_left, bisect_right, insort_left, insort_right

    import sys
    sys.setrecursionlimit(1000000)
    mod = 1000000007
    inf = float('INF')

    def intput(): return int(input())
    def mint(): return map(int,input().split())
    def lint(): return list(map(int,input().split()))
    def getX(n): return [int(input()) for i in range(n)]
    def getXY(n):
        xy = [map(int, input().split()) for _ in range(n)]
        x, y = [list(i) for i in zip(*xy)]
        return x, y

    def getNest(n):
        nest = [[int(i) for i in input().split()] for _ in range(n)]
        return nest
    import numpy as np
    n = intput()
    a = lint()

    cum = np.zeros(n + 1, int)
    cum[1:] = np.cumsum(a)
    cumcum = np.cumsum(cum)

    cum_max = np.maximum.accumulate(cum)
    ans = np.max(cumcum[:-1] + cum_max[1:])
    print(ans)

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3
2 -1 -2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-2 1 3 -1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
-1000 -1000 -1000 -1000 -1000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
