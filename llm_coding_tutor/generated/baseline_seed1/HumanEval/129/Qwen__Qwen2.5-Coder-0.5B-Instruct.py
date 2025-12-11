from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    def dfs(x, y, path):
        nonlocal k
        if len(path) == k:
            return path
        min_path = None
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] not in path:
                new_path = dfs(nx, ny, path + [grid[nx][ny]])
                if min_path is None or new_path < min_path:
                    min_path = new_path
        return min_path

    return dfs(0, 0, [])