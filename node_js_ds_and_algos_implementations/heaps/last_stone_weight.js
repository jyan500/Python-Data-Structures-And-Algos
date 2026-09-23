class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        /* 
        Revisited 9/22/2026
        max heap
        pop two from the front and applying the logic
        pushing back in if the stone isn't destroyed
        */

        let maxHeap = new MaxPriorityQueue()
        for (let i = 0; i < stones.length; ++i){
            maxHeap.enqueue(stones[i])
        }
        while (maxHeap.size() > 1){
            let first = maxHeap.dequeue()
            let second = maxHeap.dequeue()
            if (first !== second){
                let difference = Math.abs(first-second)
                maxHeap.enqueue(difference)
            }
        }
        return maxHeap.size() > 0 ? maxHeap.front() : 0
    }
}

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    /*
    convert array to max heap to maintain sorted order of the stone weights
    
    while max heap size > 1
        pop the first two values off the heap
        apply the logic to figure out the new weight
        push the new weight to the heap if valid

    Time complexity:
    O(NLogK) (where K is the height of the heap, and N is the number of stones)
    Each logK is referring to the complexity needed to push and pop a node.
    Space complexity:
    O(N) for the heap
    */
    let heap = new MaxPriorityQueue()
    for (let stone of stones){
        heap.enqueue(stone)
    }
    while (heap.size() > 1){
        let { element: s1 } = heap.dequeue()
        let { element: s2 } = heap.dequeue()
        if (s1 !== s2){
            heap.enqueue(s1-s2)
        }
    }
    return heap.size() === 0 ? 0 : heap.front().element
    
    
};