"""
Top K frequent words

Key concepts:
1) Create max heap by taking a list of tuples, where the first element is the frequency (but negative since it's a max heap)
and the second element is the word
2) Use heapify
3) Heappop() k times

O(NLogK), where Heapify is O(N), and each pop operation is Log(K)
O(N) space
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        counter = dict()
        for i in range(len(words)):
            if words[i] in counter:
                counter[words[i]] += 1
            else:
                counter[words[i]] = 1
        # max heap, so we need to invert the numbers
        heap = []
        for key in counter:
            heap.append((-counter[key], key))
        heapq.heapify(heap)
        res = []
        for i in range(k):
            freq, word = heapq.heappop(heap)
            res.append(word)
        return res