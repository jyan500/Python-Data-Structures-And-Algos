/**
 * @param {number} k
 * @param {number[]} nums
 */
/*
Approach:
The idea is that we have a nums list of length N, but we only want to get 
the Kth largest elements in that list of nums. 
For example:
[4, 5, 8, 2]
k = 3
we only want the 3 largest elements in this list of 4, the kth largest element
would be 4 here

In the constructor, we want to use a min heap instead of a max heap. The concept is reverse thinking,
the smallest element is at the front, and the largest in the back for a min heap. Therefore,
by adding all elements and then popping until the minHeap.size() === k, we get the kth largest elements

min heap: [2, 4, 5, 8]
size is 4, k = 3, so we need to pop() one
min heap is now [4, 5, 8]

Now if we want to add an element:
num to add = 3
min heap : [4, 5, 8]
after adding:
[3,4,5,8]

Now the min heap is now size 4, so we need to pop from min heap to get it back to size k
[4,5,8]

we now return the front element, which is the kth largest element (4)

now if we add 5
min heap: [4, 5, 8], after adding: [4, 5, 5, 8]

pop from min heap to get back to size k
[5, 5, 8],

we return the front element, which is the kth largest element (5) 

Time Complexity:
Constructor: O(NLogN), which is the creation of the min heap when enqueueing 
Add: O(LogN), since we need at most one enqueue operation (OLogN to bubble up any possible smaller elements) and one pop operation which is LogN
*/
var KthLargest = function(k, nums) {
    this.k = k
    this.minHeap = new MinPriorityQueue()
    for (let n of nums){
        this.minHeap.enqueue(n)
    }
    while (this.minHeap.size() > this.k){
        this.minHeap.dequeue()
    }
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    /*
    Note that the heap automatically stores each value as an object
    like so:
    {priority: val, element: val},
    so you need to access the element attribute to get the number
    */
    this.minHeap.enqueue(val)
    if (this.minHeap.size() > this.k){
        this.minHeap.dequeue()
    }
    return this.minHeap.front().element
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */