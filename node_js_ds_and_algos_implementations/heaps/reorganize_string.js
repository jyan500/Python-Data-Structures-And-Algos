class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    reorganizeString(s) {
        /*
        Heap problem?
        After thinking about this, it's a bit similar to the task scheduler
        problem, where you can't have two tasks next to each other and there's a cooldown time.
        I think this is a similar concept to that, where you get the counts of each character.
        And then you try to use up all the most frequent occurring character first.
        The heap is useful here since it always tell us the most frequently occurring character
        axyy

        for example:
        y
        then y needs to go "cooldown" for at least one turn
        x
        x needs to go on "cooldown"
        y
        a
            
        Time complexity: O(NLogK), where N is the length of s, and K is the amount of distinct characters in s
        Space: O(N)
        */
        let counter = new Map()
        for (let i = 0; i < s.length; ++i){
            if (counter.get(s[i])){
                counter.set(s[i], counter.get(s[i])+1)
            }
            else {
                counter.set(s[i], 1)
            }
        }
        let maxHeap = new MaxPriorityQueue((entry) => entry[1])
        counter.keys().forEach((key) => {
            maxHeap.enqueue([key, counter.get(key)])
        })

        // perform the while loop to reorganize
        // pop off the max heap and place the [character, count] onto "cooldown"
        // if the count is > 0, on the next iteration, place it back onto the queue
        let res = []
        let cooldown = []
        while (maxHeap.size() > 0){
            let [char, count] = maxHeap.dequeue()
            // use the character by consuming one count
            if (cooldown.length > 0){
                let [cooldownChar, cooldownCount] = cooldown
                if (cooldownCount > 0){
                    maxHeap.enqueue(cooldown)
                }
            }
            cooldown = [char, count-1]
            res.push(char)
        }
        // to handle edge cases where the string cannot be reorganized to avoid
        // consecutive characters, the final string length will not be the same
        // as the original
        return res.length === s.length ? res : ""
    }
}
