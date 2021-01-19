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



#
# n = input()
# k = len(n)
# if int(n) % 3 == 0:
#     print(0)
# else:
#     ans = -1
#     for i in range(1, k):
#         for j in range(i, k+1):
#             p = n[:(i-1)] + n[j-1:]
#             print(p)
#             if int(p) % 3 == 0:
#                 ans = max(ans, len(p))
#     if ans == -1:
#         print(ans)
#     else:
#         print(k-ans)

# 連続する桁かと思ったらどこでもよかった！
# bit全探索でとこう

import sys
from io import StringIO
import unittest

def resolve():
    n = input()
    k = len(n)

    ans = -1
    for i in range(2 ** k):
        n_ = ''
        for j in range(k):
            if (i >> j) & 1:
                n_ += n[j]
        if n_ != '':
            if int(n_) % 3 == 0:
                ans = max(ans, len(n_))
    if ans == -1:
        print(-1)
    else:
        print(k-ans)
resolve()

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
        input = """35"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """369"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6227384"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


35
369
6227384
11
