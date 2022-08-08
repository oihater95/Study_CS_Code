# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def dfs(r, c):
  grid[r][c] = '2'  # 방문 체크

  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    if 0 <= nr < m and 0 <= nc < n:
      if grid[nr][nc] == '1':
        dfs(nr, nc)


m = len(grid)
n = len(grid[0])
result = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(m):
  for j in range(n):
    if grid[i][j] == '1':
      dfs(i, j)
      result += 1

print(result)  # LeetCode에서는 return