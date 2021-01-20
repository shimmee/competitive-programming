##############################################################
# 大会名: HHKB プログラミングコンテスト 2020
# 時間: 2020-10-10(土) 21:00 ~ 2020-10-10(土) 22:40 (100分)
##############################################################


##############################################################
# 1問目
# タイトル: A - Keyboard
# URL: https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_a
##############################################################
S = input()
T = input()

if S == "Y":
    print(T.upper())
else:
    print(T)


##############################################################
# 2問目
# タイトル:
# URL:
##############################################################
H, W = list(map(int,input().split()))
s_h = [input() for i in range(H)]
s_w = []
for i in range(W):
    string = ''
    for j in range(H):
        string += s_h[j][i]
    s_w.append(string)

count = 0
for i in range(H):
    string = s_h[i]
    dots = string.split('#')
    for dot in dots:
        num_dot = dot.count('.')
        if num_dot >= 2:
            count += num_dot-1
for j in range(W):
    string = s_w[j]
    dots = string.split('#')
    for dot in dots:
        num_dot = dot.count('.')
        if num_dot >= 2:
            count += num_dot-1
print(count)

# 模範解答の発想: 今いる場所を動かして，右か下がドットならincrement
# 今いる場所を動かす方が簡単な場合もある
# 思いついた発想のために標準入力をごちゃごちゃイジるくらいなら，入力のまま活かせる方法を考えた方がいい

##############################################################
# 3問目
# タイトル: C - Neq Min
# URL: https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c
##############################################################
N = int(input())
P = list(map(int, input().split()))
# all = set([i for i in range(200000)])

# 最初に0が出るまで0を出力
zero_index = P.index(0)
for i in range(zero_index):
    print(0)

# 出現した数のリスト
occured = set(P[:zero_index])
min_val = 0
for j in range(zero_index, N):
    occured.add(P[j])

    # 最小値を更新: 出現したリストにない整数のうち最小のもの
    min_val = min(set(range(1, len(occured) + 1)) - set(occured))
    print(min_val)


# 模範解答
# https://atcoder.jp/contests/hhkb2020/submissions/17294209
N = int(input())
P = list(map(int, input().split()))
flag = [False] * 200001
i = 0
for p in P:
    flag[p] = True
    while flag[i]:
        i += 1
    print(i)

# 学んだこと: フラグを立てるという発想
# whileでフラグをどんどん進めていくという発想


##############################################################
# 4問目
# タイトル:
# URL:
##############################################################