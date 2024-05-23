/*
Time Complexity: 

Find Median O(1)
Add Num (OLogN)

the idea behind this solution is using two heaps, one min heap and one max heap
the goal is that the min heap contains all elements that are larger than the elements in max heap,
and the max heap contains all elements less than the elements in min heap.

As calls to "addNum" are made, the two "middle" elements
will be the root of the heaps. This makes it very easy to retrieve the middle elements
and determine the median.

As you call "addNum", you initially add numbers to the max heap. But once the size difference
between the max and min heap > 1, you'll need to balance the heaps out by popping the root of the longer heap
and adding it to the other heap. Before checking this, you also need to check an edge case to make sure
the top of the max heap doesn't exceed the value of the top of the min heap, otherwise, you need to 
pop out of the max heap and push to the min heap.

If the size of both heaps is even, you'll need to sum the two middle elements / 2
If its odd, then you'd take the top element of one of the heaps depending on which one has a greater size.

example:
maxheap = [] minheap = []

add num 1
maxheap = [1] minheap = []

add num 2
maxheap = [2, 1] minheap = []
difference in size is > 1
moves top max heap to min heap
maxheap = [1] minheap = [2]

add num 3
maxheap = [3, 1] minheap = [2]
we reach the edge case where the top of max heap > top min heap,
need to pop top of max heap and move to min heap
maxheap = [1] minheap = [2, 3]

add num 5
max heap = [5, 1] minheap = [2, 3]
edge case is reached again, since top of max heap > top of min heap
maxheap = [1] minheap = [2, 3, 5]

however, we also hit the second if statement, where the size difference > 1
we need to pop the top of min heap this time since it's greater in size,
and add to max heap
maxheap = [2, 1] minheap = [3, 5]

find median
in the numbers we've added so far [1,2,3,5]
if we pop the top of max heap and min heap, we get 2 and 3 respectively
since the lengths of both heaps are the same,
(2+3)/2 = 2.5, returns 2.5 as the median
*/
var MedianFinder = function() {
    // min heap contains all elements that are larger than the elements in max heap
    // max heap contains all elements less than the elements in min heap
    this.minHeap = new MinPriorityQueue()
    this.maxHeap = new MaxPriorityQueue()
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    // by default, add to the max heap first
    this.maxHeap.enqueue(num)
    let topMaxHeap = this.maxHeap.front().element
    let topMinHeap = null
    // because you're defaulting to adding numbers to the max heap,
    // need to handle a case where you check if the number should actually belong in the min heap
    // instead, since the top of max heap must be less than the top of min heap
    if (this.minHeap.size() > 0){
        topMinHeap = this.minHeap.front().element
        if (topMaxHeap > topMinHeap){
            let element = this.maxHeap.dequeue().element
            this.minHeap.enqueue(element)
        }
    }
    if (Math.abs(this.minHeap.size() - this.maxHeap.size()) > 1){
        if (this.maxHeap.size() > this.minHeap.size()){
            let element = this.maxHeap.dequeue().element
            this.minHeap.enqueue(element)
        }
        else {
            let element = this.minHeap.dequeue().element
            this.maxHeap.enqueue(element)
        }
    }
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    let topMaxHeap = this.maxHeap.front().element
    if (this.minHeap.size() > 0){
        if (this.minHeap.size() === this.maxHeap.size()){
            let topMinHeap = this.minHeap.front().element
            return (topMaxHeap + topMinHeap)/2
        }
        // if min heap size is greater than max heap, this indicates the middle element
        // is the top of the min heap
        else if (this.minHeap.size() > this.maxHeap.size()){
            return this.minHeap.front().element
        }
    }
    // if neither case above is true, we return the top of the max heap (i.e max heap size > min heap size)
    return topMaxHeap
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */