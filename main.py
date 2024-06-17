class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not (1 <= m <= 100 and 1 <= n <= 100):
            raise ValueError("m and n must be between 1 and 100 inclusive.")

        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
