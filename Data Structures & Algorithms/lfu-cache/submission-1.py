class LFUCache:

    def __init__(self, capacity: int):
        self.key2node_ref_dict = {}
        self.freq2linkedlist_ref_dict = {}
        self.capacity = capacity
        self.element_count = 0

    def get(self, key: int) -> int:
        if key in self.key2node_ref_dict.keys():
            target_node = self.key2node_ref_dict[key]
            value = target_node.value
            self._increase_freq_and_push_to_most_recent(target_node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # present or not
        if key in self.key2node_ref_dict.keys():
            # present: freq += 1, update
            target_node = self.key2node_ref_dict[key]
            target_node.value = value
            self._increase_freq_and_push_to_most_recent(target_node)
        else:
            # if not present -> insert. 
            # but evict or not.
            # firstly create a new node
            target_node = Node(key, value, 0)
            # evict or not
            if self.element_count == self.capacity:
                # need to evict
                self._evict()
            else:
                self.element_count += 1
            # update key2node dict
            self.key2node_ref_dict[key] = target_node
            self._increase_freq_and_push_to_most_recent(target_node, False)
        return

    def _increase_freq_and_push_to_most_recent(self, target_node, remove_from_existing_list=True):
        # frequency += 1, promote to new frequency linked list and set as most frequent
        if remove_from_existing_list:
            self._remove_from_current_freq_list(target_node)
        
        target_node.freq += 1
        if target_node.freq not in self.freq2linkedlist_ref_dict:
            new_freq_linked_list = DoubleLinkedList()
            self.freq2linkedlist_ref_dict[target_node.freq] = new_freq_linked_list
        else:
            new_freq_linked_list = self.freq2linkedlist_ref_dict[target_node.freq]
        new_freq_linked_list.set_most_recent(target_node)
        return

    def _evict(self):
        # evict the tail one of the least frequent
        sorted_freq_list = sorted(self.freq2linkedlist_ref_dict.keys())
        min_freq = sorted_freq_list[0]
        key, no_elements = self.freq2linkedlist_ref_dict[min_freq].evict_tail()
        if no_elements:
            # delete freq entry
            self.freq2linkedlist_ref_dict.pop(min_freq)
        # delete key
        self.key2node_ref_dict.pop(key)
        return

    def _remove_from_current_freq_list(self, target_node):
        prev_node = target_node.prev
        next_node = target_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        target_node.next = None
        target_node.prev = None
        # find linked list from freq
        no_elements = self.freq2linkedlist_ref_dict[target_node.freq].no_elements()
        if no_elements:
            # delete freq entry
            self.freq2linkedlist_ref_dict.pop(target_node.freq)
        return
    
class DoubleLinkedList:
    # each frequency has one linked list, head is the most recent one, tail is the least recent one.
    def __init__(self):
        self.virtual_head = Node()
        self.virtual_tail = Node()
        self.virtual_head.next = self.virtual_tail
        self.virtual_tail.prev = self.virtual_head

    def set_most_recent(self, target_node):
        # push to head
        head = self.virtual_head.next
        target_node.next = head
        target_node.prev = self.virtual_head
        self.virtual_head.next = target_node
        head.prev = target_node
        return
    
    def evict_tail(self):
        # remove the tail one.
        tail = self.virtual_tail.prev
        prev_node = tail.prev
        prev_node.next = self.virtual_tail
        self.virtual_tail.prev = prev_node
        tail.next = None
        tail.prev = None
        # need to return there are elements left or not
        return tail.key, self.no_elements()

    def no_elements(self):
        # need to return there are elements left or not
        if self.virtual_tail.prev == self.virtual_head:
            return True
        else:
            return False

class Node:
    def __init__(self, key=None, value=None, freq=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)