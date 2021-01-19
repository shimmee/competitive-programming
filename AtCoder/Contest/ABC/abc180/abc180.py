##############################################################
# AtCoder Beginner Contest 180
# 2020-10-17(土) 20:00 ~ 2020-10-17(土) 21:40 (100分)
##############################################################

##############################################################
# 1問目
# タイトル:
# URL:
# 日時: 2020/10/17
##############################################################

N, A, B = list(map(int,input().split()))
print(N-A+B)


##############################################################
# 2問目
# タイトル:
# URL:
# 日時: 2020/10/17
##############################################################
import numpy as np
import math
N = int(input())
x = np.array(list(map(int,input().split())))

m = abs(x).sum()
u = math.sqrt((abs(x)**2).sum())
c = max(abs(x))

print(m)
print(u)
print(c)

##############################################################
# 3問目
# タイトル: C - Cream puff
# URL:
# 日時: 2020/10/17
##############################################################

N = int(input())


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisor = make_divisors(N)
for i in divisor:
    print(i)


##############################################################
# 4問目
# タイトル: D - Takahashi Unevolved
# URL:
# 日時: 2020/10/17
##############################################################

X, Y, A, B = list(map(int,input().split()))

i = 0
while True:
    if X * (A ** i) <= B and X * (A ** i) < Y:
        if X * (A ** (i + 1)) >= B:
            break
        else:
            i += 1
    else:
        break
strength = X * (A ** i)
exp = i + (Y - (strength + 1)) // B
print(exp)


# X * (A ** i) < Yを入れるのを忘れてて，1ケースだけWAだった。かなしい





##############################################################
# 5問目
# タイトル: E - Traveling Salesman among Aerial Cities
# URL:
# 日時: 2020/10/17
##############################################################

