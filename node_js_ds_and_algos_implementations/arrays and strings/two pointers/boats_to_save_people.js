class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people, limit) {
        /*
        greedy solution
        sort, then try to fit into boats like window problem
        until the window exceeds limit 

        1 2 4 5

        this doesn't work because
        1 2 in one boat, 4 in one boat, 5 in one boat isn't actually optimal here

        rather, try taking from opposite ends? So it's a 2 pointer problem (similar to container with most water)
        since we can only accept up to two at a time. If adding both exceeds the limit,
        we take only the larger number on the right side (which is the greedy aspect) and decrement the right pointer, while 
        keeping the left pointer the same.

        1 2 4 5

        accept 1 5
        2 4

        1 2 2 3 3, limit = 3
    
        If 1 and 3 doesn't work,
        pick only 3
        1 2 2 3
        1 and 3 doesn't work again,
        so pick only 3 again
        1 2 2
        1 and 2 works

        O(NLogN) Time
        O(1) Space
        */
        // sort by decreasing order
        people.sort((a, b) => a - b)
        let l = 0
        let r = people.length - 1
        let res = 0
        while (l <= r){
            // this is a valid boat under the capacity
            // so increment l and decrement r
            if (people[l] + people[r] <= limit){
                ++l   
                --r
            }
            // otherwise, we only accept the greater value which is at r
            else {
                --r
            }
            ++res
        }
        return res
    }
}
