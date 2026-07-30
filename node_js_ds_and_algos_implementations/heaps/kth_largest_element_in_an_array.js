class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums, k) {
        /* 
        heap 
        when looking for only the kth largest,
        you store only a min heap of size k,
        note that it's a min heap because the kth largest would actually be the "min"
        of the min heap, so it ends up at the front

        Time: O(NLogK)
        Space: O(K), since we're only storing up to K elements in the heap
        */
        let minHeap = new MinPriorityQueue()
        for (let i = 0; i < nums.length; ++i){
            minHeap.enqueue(nums[i])
            if (minHeap.size() > k){
                minHeap.dequeue()
            }
        }
        return minHeap.front()
    }
}

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
/*
Time Complexity: O(N + NlogK)
Space: O(N)
*/
var findKthLargest = function(nums, k) {
    let heap = new MaxPriorityQueue()
    for (let n of nums){
        heap.enqueue(n)
    }
    let res = 0
    for (let i = 0; i < k; ++i){
        res = heap.dequeue()
    }
    return res.element
};