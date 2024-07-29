/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function(tickets, k) {
    /*
    Linear Time Solution (Neetcode)
    https://youtu.be/cVmS9N6kf2Y
    You can skip the simulation and do this in one pass by recognizing this pattern:
    
    because we only want to know how much time is taken until the person at tickets[k] is finished,
    we think about the total amount of time taken at position before k in relation to the amount of tickets[k]
    
    when looking at any i before k, if tickets[i] < tickets[k], the person at tickets[i] would've taken
    tickets[i] amount of time to buy their ticket
    however, if tickets[i] > tickets[k], it would take tickets[k] amount of time until the person at k finishes buying their ticket
    
    If we keep a result, we add tickets[i] if tickets[i] <= tickets[k], or tickets[k] if tickets[k] < tickets[i]
    
    There's one edge case where there are elements before AND after k:
    k=1
    2 3 3
    
    for i = 0, it'd take 2 seconds for the person to finish buying their ticket (because i <= k)
    for i = 1, it'd take 3 seconds for the person to finish buying their ticket (because i <= k)
    for i = 2, even though it would take 3 seconds for this person to buy their ticket, because ticket[k] >= ticket[i], would add ticket[i] - 1 in this case,
    so it's one less pass since the person at k = 1 would've finished buying their ticket before ticket[i]
    
    */
    let res = 0
    for (let i = 0; i < tickets.length; ++i){
        if (i <= k){
            res += Math.min(tickets[i], tickets[k])
        }
        else {
            /*
            2 3 2, k = 1
            at i = 2, you'd choose between tickets[1] - 1 and tickets[2]
            2 3 4, k = 1
            at i = 2, you'd choose between tickets[1] - 1 and tickets[2] (between 2 and 4 in this case, since for the last person,
            it'd do 2 passes, and then tickets[k] would've reached 0, and then we'd stop the execution, so that's why it's one "less" pass)
            */
            res += Math.min(tickets[k] - 1, tickets[i])
        }
    }
    return res
    /*
    simulation
    O(N*M) time
    O(N) Space
    1) within the queue, map each tickets[i] with i to track it's original spot so it can be referenced
    with k
    2) Keep track of time variable
    3) When processing each element of the queue,
        pop 0th element at queue (leftmost)
        decrement from the amount (Tickets[i])
        check if amount > 0, if so push the new amount and the index to the back of the queue
        
        increment the time
        
        if the amount === 0 and the index that we popped off the queue === k, this is the element
        that we wanted to track, so we return the time
    */
    // let queue = tickets.map((element, i) => [element, i])
    // let time = 0
    // while (queue){
    //     let [ amount, index ] = queue[0]
    //     queue.shift()
    //     if (amount - 1 > 0){
    //         queue.push([ amount - 1, index])
    //     }
    //     ++time
    //     if (amount - 1 === 0 && index === k){
    //         return time
    //     }
    // }

};