# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        num_pairs=len(pairs)
        if num_pairs == 0:
            return []
        results=[pairs]
        if num_pairs == 1:
            return results

        ordered_pairs=[pairs[0]]
        for index in range(1,num_pairs):
            target = pairs[index]
            unordered_pairs=pairs[index+1:]
            ordered_pairs=binary_insert(ordered_pairs,0,index-1,target)
            results.append(ordered_pairs+unordered_pairs)
            # insert intermediate result every time
        return results

def binary_insert(pairs, start, end, target):
    if start == end:
        if pairs[end].key <= target.key:
            pairs.insert(end+1,target)
        else:
            pairs.insert(end,target)
        return pairs

    if start + 1 == end:
        if pairs[end].key <= target.key:
            pairs.insert(end+1,target)
        elif pairs[start].key <= target.key:
            pairs.insert(end,target)
        else:
            pairs.insert(start,target)
        return pairs

    mid = (start + end)//2
    mid_val=pairs[mid]
    if mid_val.key < target.key:
        start=mid
        return binary_insert(pairs,start,end,target)
    elif mid_val.key > target.key:
        end = mid
        return binary_insert(pairs,start,end,target)
    else:
        cursor_idx=mid
        while pairs[cursor_idx].key == target.key:
            cursor_idx += 1
        pairs.insert(cursor_idx,target)
        return pairs