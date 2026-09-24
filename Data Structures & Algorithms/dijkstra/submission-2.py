class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        output={}
        Q={i: float('inf') for i in range(n)}
        Q[src] = 0
        prev={}

        while len(Q) != 0:
            k = pick_min_dist_vertex(Q)
            min_dist_to_k = Q[k]
            if min_dist_to_k == float('inf'):
                break
            Q.pop(k)
            output[k] = min_dist_to_k

            for edge in edges:
                if edge[0] == k:
                    dest = edge[1]
                    if dest not in Q.keys():
                        continue
                    inter_dist = edge[2]
                    k_to_dest = min_dist_to_k + inter_dist
                    if Q[dest] > k_to_dest:
                        # update
                        Q[dest] = k_to_dest
                        prev[dest] = k

        for k in Q.keys():
            output[k] = -1
        return output

def pick_min_dist_vertex(Q):
    minimal=min(Q.values())
    for k,v in Q.items():
        if v == minimal:
            return k

