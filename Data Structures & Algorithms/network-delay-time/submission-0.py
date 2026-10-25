import itertools
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # priority queue needs to store nid and distance
        self.pq = []
        heapq.heapify(self.pq)
        self.dist = [float("inf") for _ in range(n)]
        self.dist[self.nid_to_index(k)] = 0
        self.m = defaultdict(list)
        for time in times:
            self.m[time[0]].append(time)

        heapq.heappush(self.pq, (0, k))
        self.dijkstra()
        max_dist = -1
        for dist in self.dist:
            if dist == float("inf"):
                return -1
            if dist > max_dist:
                max_dist = dist
        return max_dist

    def dijkstra(self):
        while len(self.pq) > 0:
            dist, nid = heapq.heappop(self.pq)
            if dist > self.dist[self.nid_to_index(nid)]:
                continue
            for _, tar, dist in self.m[nid]:
                if self.dist[self.nid_to_index(tar)] > (self.dist[self.nid_to_index(nid)] + dist):
                    self.dist[self.nid_to_index(tar)] = self.dist[self.nid_to_index(nid)] + dist
                    heapq.heappush(self.pq, (self.dist[self.nid_to_index(tar)], tar))
        return

    def nid_to_index(self,i):
        return i-1