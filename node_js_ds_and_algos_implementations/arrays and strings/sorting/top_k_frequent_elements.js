/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

/* 
Bucket Sort Concept can solve this in O(N) time without needing to do heapify or sort 
Neetcode:
https://youtu.be/YPTqKIgVk-k
*/
var topKFrequent = function(nums, k) {
    /* 
    Bucket Sort O(N) time solution
    Example execution:
    nums = [1,1,2,2,3,4], k = 2
    counter would be {1: 2, 2: 2, 3: 1, 4: 1}
    freq would be 6 individual buckets
     0   1    2  3   4    5   6
    [[], [], [], [], [], [], []]
    at freq 1, there are two elements 3 and 4 that appear one time only
     0     1    2   3   4   5   6
    [[], [3,4], [], [], [], [], []]
    at freq 2, there are two elements 1 and 2 that appear two times only
     0     1      2     3   4   5   6
    [[], [3,4], [1, 2], [], [], [], []]
    Therefore, the answer would be [1,2], because iterating from the back,
    we'd get the frequency of 2 first, which contains two elements
    
    these are the top 2 most frequent elements
    
    */
    let counter = {}
    for (let num of nums){
        if (num in counter){
            counter[num]++
        }
        else {
            counter[num] = 1
        }
    }
    /*
    create a frequency array that's bounded by length of nums,
    where the index is the count in our counter, and the value at freq[index]
    is the array of elements that have that total count.
    The reason it's bounded by the length of nums is because the max freq of any element in the array
    is the length of that array (i.e [1,1,1,1,1,1], 1 occurs 6 times, so we set our freq array indices
    from 0 to 6
    */
    let freq = []
    for (let i = 0; i <= nums.length; ++i){
        freq.push([])
    }
    for (let key in counter){
        let count = counter[key]
        // take the count and then match the count based on the index of the frequency array,
        // add the element that has that count
        freq[count].push(parseInt(key))
    }
    let res = []
    // we start from the back of the array, as these are the elements that would have the greatest frequency
    for (let i = freq.length-1; i >= 0; --i){
        // if there are elements with this particular count, include all elements into res (order doesn't matter)
        if (freq[i].length){
            res = [...res, ...freq[i]]
        }
        // if our total length of res === k, that means we've retrieved the top k frequent elements, so we break and return res
        if (res.length === k){
            break
        }
    }
    return res
    /*
    Heapify - O(KLogN) time solution
    let counter = {}
    for (let num of nums){
        if (num in counter){
            counter[num]++
        }
        else {
            counter[num] = 1
        }
    }
    let maxHeap = new MaxPriorityQueue({priority: (obj) => obj[1]})
    for (let key in counter){
        maxHeap.enqueue([key, counter[key]])
    }
    let res = []
    for (let i = 0; i < k; ++i){
        let element = maxHeap.dequeue().element[0]
        res.push(parseInt(element))
    }
    return res
    */
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let c = {}
    for (let i = 0; i < nums.length; ++i){
        if (nums[i] in c){
            ++c[nums[i]]
        } else {
            c[nums[i]] = 1
        }
    }
    const sortKey = (a, b) => {
        if (c[a] < c[b]){
            return 1
        }
        else if (c[a] > c[b]){
            return -1
        }
        else {
            return 0
        }
    }
    // sort the keys array based on the frequencies found in our counter object
    let sortedKeys = Object.keys(c).sort(sortKey)
    return sortedKeys.slice(0, k)
    
};