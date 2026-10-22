class Node:
    def __init__(self, nid):
        self.nid = nid
        self.next = [None for _ in range(26)]

class PrefixTree:

    def __init__(self):
        self.counter = 0
        self.root = Node(self.counter)
        self.m = {} # word to int index

    def insert(self, word: str) -> None:
        cursor = self.root
        for i, c in enumerate(word):
            idx = ord(c) - ord("a")
            if not cursor.next[idx]:
                # create if not exist yet
                self.counter += 1
                cursor.next[idx] = Node(self.counter)
            cursor = cursor.next[idx] 
        self.m[word] = self.counter
        return

    def search(self, word: str) -> bool:
        return word in self.m

    def startsWith(self, prefix: str) -> bool:
        cursor = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if cursor.next[idx]:
                cursor = cursor.next[idx]
            else:
                return False
            
        return True