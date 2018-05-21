class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        # Make rol x col matrix with all false
        # to track when a cell has been visited
        # cannot go to the same cell twice.
        pacific_visited = [[False for j in range(cols)] for i in range(rows)]
        atlantic_visited = [[False for j in range(cols)] for i in range(rows)]

        pacific_stack = []
        atlantic_stack = []

        # setup cells that touch the oceans
        for i in range(rows):
            # add all cells in first column
            pacific_stack.append(i, 0)
            # add all cells in last column
            atlantic_stack.append(i, cols - 1)

        for j in range(cols):
            # add all cells in first row
            pacific_stack.append([0, j])
            # add all cells in last row
            atlantic_stack.append((rows - 1, j))

        self.dfs(matrix, pacific_stack, rows, cols, pacific_visited)
        self.dfs(matrix, atlantic_stack, rows, cols, atlantic_visited)

        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    res.append([i, j])

        return res

    # Climb up from the edge of oceans
    def dfs(self, matrix, stack, rows, cols, visited):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        while stack:
            x, y = stack.pop()
            # skip the rest if cell is visited
            if visited[x][y]:
                continue
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # If cell has higher value then cell cannot flow that way, so skip
                # since value can only go down, this path can never flow there
                if not self.canFlow(matrix, rows, cols, nx, ny, matrix[x][y]):
                    continue
                stack.append([nx, ny])

    def dfs(self, matrix, stack, rows, cols, visited):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not self.canFlow(matrix, rows, cols, nx, ny, matrix[x][y]):
                    continue
                stack.append([nx, ny])

    def canFlow(self, matrix, rows, cols, x, y, fromFlow):
        if x < 0 or x >= rows:
            return False
        if y < 0 or y >= cols:
            return False
        # if water can flow from new cell to current
        # it means the current one cannot flow down to the new cell
        if matrix[x][y] < fromFlow:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.pacificAtlantic(
        [[1,2,2,3,5],
         [3,2,3,4,4],
         [2,4,5,3,1],
         [6,7,1,4,5],
         [5,1,1,2,4]]))

