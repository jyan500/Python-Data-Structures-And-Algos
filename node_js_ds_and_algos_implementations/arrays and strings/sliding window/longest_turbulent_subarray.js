class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    maxTurbulenceSize(arr) {
        /*
        turbulent array demonstration:

        arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]

        Let's look at the comparisons between each pair of adjacent elements:

        9   4   2   10   7   8   8   1   9
        \   \   /    \   /   =   \   /
        >   >  <     >  <    =    >

        9 > 4 (down)
        4 > 2 (down) → same direction as before, breaks turbulence
        2 < 10 (up)
        10 > 7 (down)
        7 < 8 (up)
        8 = 8 (equal) → breaks turbulence immediately, equal is never allowed
        8 > 1 (down)
        1 < 9 (up)

        So scanning through, the comparisons look like: down, down, up, down, up, equal, down, up

        The longest run where the signs strictly alternate (no repeats, no equals) is:

        [2, 10, 7, 8]  →  <, >, <   (up, down, up — alternates perfectly)

        That has length 4. But wait, let's also check after the equal sign:

        [8, 1, 9] → >, < (down, up — alternates, but only length 3)

        So the longest turbulent subarray in this example is [2, 10, 7, 8], 
        with length 5 if you count elements (2, 10, 7, 8 is actually 4 elements — let me recount: indices 2,3,4,5 → values 2, 10, 7, 8 → that's 4 elements, 3 comparisons: <, >, <, all alternating). 


        Seems like a sliding window problem, where the next element that we're including in the window
        must be alternate of the previous (so if down, then up, and vice versa, but never equal or the same direction)

        for example
        9, 4, 2, 10, 7, 8, 8, 1, 9

        starting at 9, 4 is down,
        2 is also down, in this case, we would actually shift to where 4 is, since that's considered
        a valid window on its own (so l = r - 1)

        However in a case like this:
        1, 1, 2

        we see that there's an equals, so we should shift l = r (at 1),
        since there's no valid window that can be made before that
        */
        if (arr.length <= 1){
            return 1
        }
        let l = 0
        let max = 1
        let prevDirection = 0
        for (let r = 1; r < arr.length; ++r){
            if (prevDirection === -1 && arr[r] < arr[r-1] || prevDirection === 1 && arr[r] > arr[r-1]){
                l = r - 1
            }
            else if (arr[r] === arr[r-1]){
                l = r
                prevDirection = 0
            }
            else {
                max = Math.max(r-l+1, max)
                // note that if our previous is less than current, the direction went up
                // otherwise, it went down
                prevDirection = arr[r-1] < arr[r] ? 1 : -1
            }
        }
        return max
    }
}
