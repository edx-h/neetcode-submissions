class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create an adjacencyList

        self.adjacencyList = {i: [] for i in range(numCourses)}
        self.inDegree = {i: 0 for i in range(numCourses)}

        for tgt, src in prerequisites:
            self.adjacencyList[src].append([tgt, src])
            self.inDegree[tgt] += 1

        # initialization: find all start node
        self.q = deque(self.pickZeroIndegree())
        self.tp_order = []

        while len(self.q) > 0:
            node = self.q.popleft()
            # remove edges starting from node, and update indegree
            for target, _ in self.adjacencyList[node]:
                self.inDegree[target] -= 1
                
                if self.inDegree[target] == 0:
                    self.q.extend([target])

            self.tp_order.append(node)

        if len(self.tp_order) < numCourses:
            return []
        return self.tp_order
    
    def pickZeroIndegree(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1] == 0, self.inDegree.items())))
