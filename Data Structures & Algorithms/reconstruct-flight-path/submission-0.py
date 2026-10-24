class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # maintain a map, mapping airport to a set of indices where the airport is `from`
        self.m = defaultdict(list)
        for t in tickets:
            self.m[t[0]].append(t[1])

        for k, v in self.m.items():
            self.m[k] = sorted(v)
        
        self.result = []
        # start from JFK
        cursor = "JFK"
        self.dfs(cursor)
        return list(reversed(self.result))

    def dfs(self, cursor):
        outbounds = self.m[cursor]
        while len(outbounds) > 0:
            next_cursor = outbounds[0]
            outbounds.pop(0) # delete the edge
            self.dfs(next_cursor)
        
        self.result.append(cursor)
        return