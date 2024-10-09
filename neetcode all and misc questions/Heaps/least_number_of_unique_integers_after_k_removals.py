class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        keep a hashmap counter as well as a min heap where the priority is based
        on the frequency of the element
        pop k times from the min heap, each time an element is popped, decrement it 
        from the hashmap counter. If the key in the hashmap counter reaches 0, pop
        the key from the hashmap
        at the end, return the length of the hashmap to show how many unique elements are left
        Time: O(NLogK), where N is the len(arr) and k is the value of K
        Space: O(N)
        """
        import heapq
        from collections import Counter
        c = Counter(arr)
        minHeap = []
        for num in arr:
            heapq.heappush(minHeap, (c[num], num))
        for i in range(k):
            freq, key = heapq.heappop(minHeap)
            c[key] -= 1
            if c[key] == 0:
                del c[key]
        return len(c)