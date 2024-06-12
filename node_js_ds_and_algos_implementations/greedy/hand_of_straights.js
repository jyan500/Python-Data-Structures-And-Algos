/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
var isNStraightHand = function(hand, groupSize) {
    /*
    Optimized Solution (using Min Heap)
    Time: O(NLogN)
    Space: O(N)

    1) Similar to the brute force, keep a counter to track the amount of each value
    2) Keep each value in the min heap,
        we want to continually pop the min from the min heap, and then find the consecutive numbers after 
        the min according to the group size
        
        There are two cases when this fails and we need to return false
            a) the consecutive number is not found 
            b) the consecutive number's amount has been used up, but this consecutive
            number is NOT the min of the min heap. This means that a previous value
            would not be able to form a group, making this invalid. For example,
            [{1:1, 2:0, 3:1}], groupSize = 3
            if the min was one, but we ran out two's, there's no way
            to make the group 1 2 3
    */
    if (hand.length % groupSize !== 0){
        return false
    }
    let counter = {}
    for (let i = 0; i < hand.length; ++i){
        if (!(hand[i] in counter)){
            counter[hand[i]] = 1
        }
        else {
            ++counter[hand[i]]
        }
    }
    let minHeap = new MinPriorityQueue()
    for (let key of Object.keys(counter)){
        minHeap.enqueue(parseInt(key))
    }
    while (minHeap.size() > 0){
        let { element: top } = minHeap.front()
        for (let i = top; i < top + groupSize; ++i){
            if (!(i in counter)){
                return false
            }
            --counter[i]
            if (counter[i] === 0){
                if (i !== minHeap.front().element){
                    return false
                }
                minHeap.dequeue()
            }
        }
    }
    return true
};

/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
var isNStraightHand = function(hand, groupSize) {
    /*
    Brute Force:
    Time: O(N^2)
    Space: O(N)
    1) One initial check to save time is that the length of the hand must be divisible by groupSize,
    otherwise it's impossible to split the hand evenly.
    2) Use a hashmap to get the counts of each card available in the hand
    3) As a greedy approach, we always pick the smallest card available to us in the hand,
    and then see if we can form the consecutive group that we need.
    For example:
    [1,2,3,6,2,3,4,7,8]
    Group size
    would create a hashmap like this:
    {1:1, 2:2, 3:2, 4:1, 6:1:, 7:1, 8:1}
    There are two 2's, and two 3's
    so starting from the smallest value, it's 1, so
    the group would need to be 1,2,3 in order to be valid.
    
    If we can't create this group, we automatically return false
    */
    if (hand.length % groupSize !== 0){
        return false
    }
    let counter = {}
    for (let i = 0; i < hand.length; ++i){
        if (!(hand[i] in counter)){
            counter[hand[i]] = 1
        }
        else {
            ++counter[hand[i]]
        }
    }
    let count = hand.length / groupSize
    while (count > 0){
        let nums = Object.keys(counter).map((x)=>parseInt(x))
        let min = Math.min(...nums)
        if (counter[min] > 0){
            for (let i = 0; i < groupSize-1; ++i){
                if (!(min+i+1 in counter)){
                    return false
                }
                --counter[min+i+1]
                // if the count has reached 0, delete the key
                if (counter[min+i+1] === 0){
                    delete counter[min+i+1]
                }
            }
            --counter[min]
            if (counter[min] === 0){
                delete counter[min]
            }
            --count
        }
    }
    return true
};