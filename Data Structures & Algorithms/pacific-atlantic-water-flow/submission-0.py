class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.p_result = set()
        self.a_result = set()
        self.row_cnt = len(heights)
        self.col_cnt = len(heights[0])
        self.heights = heights

        near_p = set((0, c) for c in range(self.col_cnt)).union(set((r, 0) for r in range(self.row_cnt)))
        near_a = set((self.row_cnt - 1, c) for c in range(self.col_cnt)).union(set((r, self.col_cnt - 1) for r in range(self.row_cnt)))

        for pacific, start_points in [(True, near_p), (False, near_a)]:
            for r, c in start_points:
                self.dfs(r, c, pacific)
        result = []
        for (r, c) in self.p_result.intersection(self.a_result):
            result.append([r, c])
        return result

    def dfs(self, r, c, pacific):
        value = self.heights[r][c]
        self.heights[r][c] = -1
        if pacific is True:
            self.result_set = self.p_result
        else:
            self.result_set = self.a_result
        
        if (r, c) not in self.result_set:
            self.result_set.add((r, c))
            neighbours = self.validNeighbours(r, c, value)
            for (nr, nc) in neighbours:
                self.dfs(nr, nc, pacific)
        self.heights[r][c] = value
        return

    def validNeighbours(self, r, c, value):
        neighbours = []
        for mask_r, mask_c in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = mask_r + r
            nc = mask_c + c

            if 0 <= nr < self.row_cnt and 0 <= nc < self.col_cnt and self.heights[nr][nc] >= value:
                neighbours.append((nr, nc))
        return neighbours