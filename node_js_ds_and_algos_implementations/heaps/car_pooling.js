class Solution {
    /**
     * @param {number[][]} trips
     * @param {number} capacity
     * @return {boolean}
     */
    carPooling(trips, capacity) {
        /*
        5/12/2026

        Time: O(NLogN)
        Space: O(N)
        
        (used very similar solution to meeting rooms II
            where you store the endings of each trip in the min heap,
            along with the numPassengers on that trip

            if prevEnd > curStart
                if we don't exceed capacity, add to the minHeap
                otherwise, return false

                also add curPassengers to capacity if not false

            else 
                // free up space if we have a new trip that doesn't overlap with the previous
                while (top of min heap's end time < curStart)
                    pop out min heap
                    decrement curCapacity

                add to heap
                add to curCapacity
        )
        [numPassengers, from, to]
        capacity = 4
        [3, 1, 3]
           [1, 2, 4]
           this is okay, because total capacity = 4
        
        cur = 4
        curInterval is now [1, 4]

        now we if we see another trip
        [1, 3, 6], this won't work because we are already at full capacity
        BUT if it was 
        [2, 4, 5], this is okay, because we are dropping off passengers at 4
        based on the previous interval, so we free up some space

        similar concept to meeting rooms II
        make priority queue based on the ending destination
        make sure if we have a trip that has start that's greater than the 
        top of the heap, we pop out, otherwise we push
        but we also keep track of current capacity in the heap as well,

        so that in the case we pop out, we also need to pop out the passengers from the 
        previous trip to free up capacity

        */
        // make sure trips are sorted based on the start distance in ascending order
        trips.sort((a,b)=>{
            if (a[1] < b[1]){
                return -1
            }
            else if (a[1] > b[1]){
                return 1
            }
            return 0
        })

        let minHeap = new MinPriorityQueue((x) => x[2])
        let curCapacity = trips[0][0]
        minHeap.enqueue(trips[0])
        for (let i = 1; i < trips.length; ++i){
            let [curPassengers, curStart, curEnd ] = trips[i]
            let [prevPassengers, prevStart, prevEnd ] = minHeap.front()
            // if overlapping
            if (prevEnd > curStart){
                if (curCapacity + curPassengers > capacity){
                    return false
                }
                minHeap.enqueue(trips[i])
                curCapacity += curPassengers
            }
            else {
                // while the cur starting is greater than the ending at the top of the heap,
                // that means we should be popping out of the min heap
                // and freeing up capacity
                while (minHeap.size() > 0 && curStart >= minHeap.front()[2]){
                    let [passengers, _, __] = minHeap.dequeue()
                    curCapacity -= passengers
                }
                minHeap.enqueue(trips[i])
                curCapacity += curPassengers
            }
        }
        return true
    }
}
