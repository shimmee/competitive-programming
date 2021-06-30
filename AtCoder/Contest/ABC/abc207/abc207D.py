# ABC207
# URL:
# Date: 2021/06/26

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
import math
def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

n = int(input())
S = [[float(i) for i in input().split()] for _ in range(n)]
T = [[float(i) for i in input().split()] for _ in range(n)]

sortT = sorted(T)
relaT = []
for j in range(n):
    relaT.append([sortT[0][0] - sortT[j][0], sortT[0][1] - sortT[j][1]])

for angle in range(3601):
    # Sをangle度回転させる
    S_ = []
    for i in range(n):
        theta = math.radians(angle/10)
        x, y = rotate((0, 0), S[i], theta)
        S_.append([x, y])

    sortS = sorted(S_)
    relaS = []
    for j in range(n):
        relaS.append([round(sortS[0][0] - sortS[j][0], 6),
                      round(sortS[0][1] - sortS[j][1], 6)])

    if relaS == relaT:
        print('Yes')
        exit()
        break
print('No')






import math
def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

n = int(input())
S = [[int(i) for i in input().split()] for _ in range(n)]
T = [[int(i) for i in input().split()] for _ in range(n)]

distS = []
distT = []

for i in range(n):
    s1 = S[i]
    for j in range(i+1, n):
        s2 = S[j]
        dist = get_distance(s1[0], s1[1], s2[0], s2[1])
        distS.append(dist)

for i in range(n):
    t1 = T[i]
    for j in range(i+1, n):
        t2 = T[j]
        dist = get_distance(t1[0], t1[1], t2[0], t2[1])
        distT.append(dist)

if sorted(distT) == sorted(distS):
    print('Yes')
else:
    print('No')


# ------------------ Sample Input -------------------
6
10 5
-9 3
1 -5
-6 -5
6 9
-9 0
-7 -10
-10 -5
5 4
9 0
0 -10
-10 -2


3
1 0
1 1
3 0
-1 0
-1 1
-3 0


3
0 0
0 1
1 0
2 0
3 0
3 1


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい


distS