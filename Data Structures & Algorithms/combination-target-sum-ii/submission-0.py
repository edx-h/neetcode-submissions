class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = list(sorted(candidates))
        self.results = []
        self.dfs(target, -1, [])
        return self.results

    def dfs(self, rSum, cursor, path):
        if cursor >= 0 and self.candidates[cursor] > rSum:
            return # no valid solution, stop dfs
        
        if cursor != -1:
            newrSum = rSum - self.candidates[cursor]
            updatedPath = path + [self.candidates[cursor]]
        else:
            newrSum = rSum
            updatedPath = []

        if newrSum == 0:
            self.results.append(updatedPath) # has valid solution, but ends here. also stop dfs
            return
        
        visited = []
        for newCursor in range(cursor + 1, len(self.candidates)):
            if self.candidates[newCursor] in visited:
                continue
                
            self.dfs(newrSum, newCursor, updatedPath)
            visited.append(self.candidates[newCursor])
        return
        