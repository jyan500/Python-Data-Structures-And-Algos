class Solution {
    /**
     * @param {number} a
     * @param {number} b
     * @param {number} c
     * @return {string}
     */
    longestDiverseString(a, b, c) {
        /* 
        no aaa, bbb, ccc means that if you choose "a"
        you need a cooldown time of at least one to avoid picking more than two in a row

        Heap problem?
        we already have the counts of each character
        max heap, use the character with the most amount first to get the longest
        possible string while still respecting the cooldown time

        you should also maximize picking two characters if you can over just one
        */
        let maxHeap = new MaxPriorityQueue((x) => x[0])
        let pairs = [[a, "a"],[b, "b"],[c, "c"]]
        for (let pair of pairs){
            if (pair[0] > 0){
                maxHeap.enqueue(pair)
            }
        }
        let res = []
        while (!maxHeap.isEmpty()){
            let [count, char] = maxHeap.dequeue()
            // if the last two characters are the same as the one that was just popped out, we can't use this character to avoid making three in a row, so we pop out again to use the 2nd highest
            // count character, and then push the pair that we initially popped out back in again
            if (res.length > 1 && res[res.length - 1] === char && res[res.length-2] === char){
                // if there is no 2nd highest character, break
                if (maxHeap.isEmpty()){
                    break
                }
                // second highest count character
                const [count2, char2] = maxHeap.dequeue()
                res.push(char2)
                // push back in if the count is greater than 0 after using one char
                if (count2 - 1 > 0){
                    maxHeap.enqueue([count2 - 1, char2])
                }
                // push the initial one back in 
                maxHeap.enqueue([count, char])
            }
            else {
                res.push(char)
                if (count - 1 > 0){
                    maxHeap.enqueue([count-1, char])
                }
            }
        }
        return res.join("")
    }
}
