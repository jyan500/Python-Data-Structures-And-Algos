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