def numIslands(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(r, c):
        if (r < 0 or r >= m or c < 0 or c >= n
                or grid[r][c] == '0' or visited[r][c]):
            return

        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count


grid = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '1']
]

print(numIslands(grid))