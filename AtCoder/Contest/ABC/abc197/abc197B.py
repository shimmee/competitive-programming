#
# URL:
# Date: 2021/03/27

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
H,W,X,Y = map(int, input().split())
X, Y = Y-1, X-1
G = [input() for _ in range(H)]

ans = 1 if G[Y][X] == '.' else 0

for y in reversed(range(0, Y)):
    if G[y][X] == '.':
        ans += 1
    else:
        break

for y in range(Y+1, H):
    if G[y][X] == '.':
        ans += 1
    else:
        break

for x in reversed(range(0, X)):
    if G[Y][x] == '.':
        ans += 1
    else:
        break

for x in range(X+1, W):
    if G[Y][x] == '.':
        ans += 1
    else:
        break

print(ans)


# ------------------ Sample Input -------------------
3 5 1 4
#....
#####
....#


4 4 2 2
##..
...#
#.#.
.#.#

5 5 4 2
.#..#
#.###
##...
#..#.
#.###


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
