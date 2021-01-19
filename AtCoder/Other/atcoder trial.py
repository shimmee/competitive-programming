from sys import stdin

N = stdin.readline().rstrip()
N = int(N)
satisfied_pattern = 10 ** N - (2 * (9 ** N) - 8 ** N)
output = satisfied_pattern % (10 ** 9 + 7)
print(output)

from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')

from sys import stdin

s = stdin.readline().rstrip()
print(int(s[0]) + int(s[1]) + int(s[2]))

from sys import stdin
import numpy as np

N = stdin.readline().rstrip()
A = np.array([int(x) for x in stdin.readline().rstrip().split()])

time = 0
while sum(A % 2) == 0:
    A = A / 2
    time += 1
print(time)

from sys import stdin

A = int(stdin.readline().rstrip())
B = int(stdin.readline().rstrip())
C = int(stdin.readline().rstrip())
X = int(stdin.readline().rstrip())
time = 0
for a in range(0, A + 1):
    for b in range(0, B + 1):
        for c in range(0, C + 1):
            total = 500 * a + 100 * b + 50 * c
            if total == X: time += 1
print(time)

from sys import stdin
import numpy as np

N, A, B = [int(x) for x in stdin.readline().rstrip().split()]
sum_of_n = 0
for n in range(1, N + 1):
    digit_sum = np.array(list(str(n))).astype(int).sum()
    if digit_sum >= A and digit_sum <= B:
        sum_of_n = sum_of_n + n
print(sum_of_n)

from sys import stdin

N, Y = [int(x) for x in stdin.readline().rstrip().split()]

max_10000 = Y // 10000
max_5000 = Y // 5000

res = None
for n_10000 in range(0, min(N, max_10000) + 1):
    for n_5000 in range(0, min(N, max_5000) + 1):
        n_1000 = N - (n_10000 + n_5000)
        if n_1000 < 0: break
        total = 10000 * n_10000 + 5000 * n_5000 + 1000 * n_1000
        # if total > Y: break
        if total == Y:
            res = [n_10000, n_5000, n_1000]
            break

if res is None:
    print('-1 -1 -1')
elif res is not None:
    print(f'{res[0]} {res[1]} {res[2]}')

from sys import stdin
import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
A.sort()
A = A[::-1]
alice_index = [i for i in range(N) if i % 2 == 0]
bob_index = [i for i in range(N) if i % 2 == 1]
gap = A[alice_index].sum() - A[bob_index].sum()
print(gap)

S = input()
S_original = None
while S_original != S:
    S_original = S
    if S[-5:] == 'erase':
        S = S[:-5]
    elif S[-5:] == 'dream':
        S = S[:-5]
    elif S[-6:] == 'eraser':
        S = S[:-6]
    elif S[-7:] == 'dreamer':
        S = S[:-7]

    if S == '':
        print('YES')
        exit()
print('NO')

# 1
S = input()
if S[-1] != 's':
    print(S + 's')
else:
    print(S + 'es')

# 2
N = int(input())
D = [list(map(int, input().split())) for i in range(N)]
time = 0
for i in range(N):
    if D[i][0] == D[i][1]:
        time += 1
        if time == 3:
            print('Yes')
            exit()
    else:
        time = 0
print('No')

# ここまで10分

# 3
import numpy as np

N = int(input())
A = np.arange(1, N, 1)
ans = 0
for a in A:
    ans += int((N - 1) / a)
print(ans)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


C = np.arange(1, N, 1)
ans = 0
for c in C:
    print(c)
    fact_list = factorization(N - c)
    num_fact = 1

    if len(fact_list) == 1 and fact_list[0][0] == 1:
        pass
    else:
        for fact in fact_list:
            num_fact *= fact[1] + 1
    ans += num_fact
print(ans)

# 5
N, X, M = map(int, input().split())


def fun(x, m):
    return x % m


N, X, M = 10000, 10, 99959

ans = 0
arr = np.zeros((N))
for i in range(N):
    ans += X
    X = fun(X ** 2, M)
    arr[i] = X
print(ans)

(arr == 68480).sum()

import numpy as np
import scipy.stats as stats

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)
A_plus = A + 1
A_minus = A - 1
A = np.append(A, A_plus)
A = np.append(A, A_minus)
print(stats.mode(A).count[0])








import numpy as np
import math
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

N = int(input())
N=2
if len(factorization(N)) == 1:
    max_prime = 1
else:
    max_prime = factorization(N)[-1][0]
k = max_prime

while True:
    if k != 1 and (int((1 / 2) * k * (k + 1)) % N == 0 or int((1 / 2) * k * (k - 1)) % N == 0):
        print(k)
        break
    k += max_prime


# 赤坂の回答
import math
N = int(input())
for p in range(1, 2 * N - 1):
    sq = int(math.sqrt(2*N * p))
    if 2 * N * p % sq == 0 and 2 * N * p == sq * (sq + 1):
        print(sq)
        break




K = int(input())
print('ACL'*K)

# B 問題
a,b,c,d = map(int,input().split())
if (c <= b and b <= d) or (a <= d and d <= b):
    print('Yes')
else:
    print('No')





a, b = map(int, input().split())
x = int((a+b)/2)
y = int((a-b)/2)
print(x, y)


S = 'ATCGTGCATGTGCACAGTGACATGCACACATGTGTGCGCTATGTCATAT'
N = 49

N, S =  input().split()
N = int(N)

count = 0
for start in range(0, N-1):
    for end in range(start+2, N+1):
        # print(S[start:end])
        T = S[start:end]
        if T.count('A') == T.count('T') and T.count('C') == T.count('G'):
            count += 1
print(count)


S = 'AAATTTCG'
N = 8

import numpy as np
count = 0
start = 0
while start < N-1:
    end_index = list()
    for end in range(start+2, N+1):
        T = S[start:end]
        if T.count('A') == T.count('T') and T.count('C') == T.count('G'):
            end_index.append(end)
    start = np.array(end_index).min() + 1
    print(start)