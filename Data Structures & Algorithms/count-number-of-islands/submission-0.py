class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return None
        m, n = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if (r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c]=="0"): return
            grid[r][c] = "0" 

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count