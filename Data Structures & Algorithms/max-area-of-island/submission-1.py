class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        unvisited = set()
        self.row_count = len(grid)
        self.column_count = len(grid[0])
        for i in range(self.row_count):
            for j in range(self.column_count):
                if grid[i][j] == 1:
                    unvisited.add((i, j))

        connected_blocks = {}
        while len(unvisited) > 0:
            source_node = unvisited.pop()
            connected_blocks[source_node] = 1
            local_unprocessed = deque([source_node])

            while len(local_unprocessed) > 0:
                block = local_unprocessed.popleft()
                for adj_block in self.find_all_adjacent_land_blocks(block): # mind out-of-boundary
                    if adj_block in unvisited:
                        unvisited.remove(adj_block)
                        # not visited yet
                        connected_blocks[source_node] += 1
                        local_unprocessed.append(adj_block)
        
        if len(connected_blocks) == 0:
            return 0
        else:
            return max(connected_blocks.values())
    
    def find_all_adjacent_land_blocks(self, block):
        row, column = block
        output = []
        for (adj_row, adj_column) in [(row, column - 1), (row, column + 1), (row - 1, column), (row + 1, column)]:
            if 0 <= adj_row <= self.row_count and 0 <= adj_column <= self.column_count:
                output.append((adj_row, adj_column))
        return output