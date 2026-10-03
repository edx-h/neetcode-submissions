class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_count = len(edges)
        self.node_parent_ref = {i: i for i in range(1, node_count + 1)}
        for (ln, rn) in edges:
            ln_parent = self.find(ln)
            rn_parent = self.find(rn)
            if ln_parent == rn_parent:
                return [ln, rn]
            else:
                # update, union
                # randomly union
                self.node_parent_ref[ln_parent] = rn_parent
    
    def find(self, node):
        parent = self.node_parent_ref[node]
        if parent == node:
            return node
        else:
            # reorganize the root
            new_parent = self.find(parent)
            self.node_parent_ref[node] = new_parent
            return new_parent
