class Node:
    def __init__(self):
        self.next = [None]*26
        self.exists = False

class Solution:
    def __init__(self):
        self.results = set()
        self.s = set() # if nid in s, it means it is the end of a word. 
        self.matched_count = 0
        self.counter = 0
        self.root = Node()
        self.m = {0:self.root} # map id to node

    def buildTrie(self, words):
        for w in words:
            cursor = self.root
            for c in w:
                idx = ord(c) - ord("a")
                if not cursor.next[idx]:
                    self.counter += 1
                    n = Node()
                    cursor.next[idx] = n
                    self.m[self.counter] = n
                cursor = cursor.next[idx]
            cursor.exists = True
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.words = words
        self.buildTrie(words)
        matched = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                idx = ord(self.board[r][c])-ord("a")
                if self.root.next[idx]:
                    self.dfs(r, c, self.root.next[idx], [])
                if self.matched_count == len(words):
                    return words
        return list(self.results)

    def validNeighbours(self, r, c, path):
        valid = []
        for (nr, nc) in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
            if 0 <= nr < len(self.board) and 0 <= nc < len(self.board[0]) and (nr, nc) not in path:
                valid.append((nr, nc))
        return valid

    def dfs(self, r, c, cursor, path):
        if cursor.exists:
            # back trace
            s = ""
            for (tr, tc) in path:
                s += self.board[tr][tc]
            s += self.board[r][c]

            if s not in self.results:
                self.matched_count += 1
                self.results.add(s)
            # 还是要继续，不能直接break

        for (nr, nc) in self.validNeighbours(r, c, path):
            nchar_idx = ord(self.board[nr][nc]) - ord("a")
            if cursor.next[nchar_idx]: # 满足任意一个邻居就行
                new_path = path + [(r,c)]
                self.dfs(nr, nc, cursor.next[nchar_idx], new_path)
        return