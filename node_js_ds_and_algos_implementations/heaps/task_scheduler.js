/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
/*

Data Structures:
1) Use a hash map to store the counts of each task
2) You want to use a max heap which stores the counts 
of all the tasks. The count will be decremented. 
3) Also you need a queue to represent the task that we just processed. We save the remaining count for that task, as well
as the next valid time that this task can be processed.

would look something like this:
tasks = ["A","A","A", "B", "B", "C"]
counter = {"A": 3, "B": 2, "C": 1}
max heap = [3,2,1]
queue = [{ remaining: 6, nextValidTime: time + n }]

Approach:
By using a max heap, this is a greedy approach, as we
want to focus on processing the tasks that have the highest count first, so that tasks with less occurrences can be scheduled during the idle time.
after all the necessary data processing above:

keep track of a time variable to show the time elapsed
Use a while loop, as long as heap or queue still has items
    increment time
    if heap has items
        pop the top of the heap
        check if the amount remaining - 1 > 0
            if so push the remaining - 1, and (time + cooldown time n) onto the queue as an object
    if queue has items
        peek to get the remaining and nextValidTime from the top of the queue
        if the remaining time === nextValidTime
            this means the cooldown time has ended for this element, so pop from the queue
            push back onto the max heap to show that it can be processed again
            
return the time. Because of the greedy approach of using a max heap, this will be the minimum time by definition.

Time Complexity:
O(cooldown time * MLogM), where M is the amount of tasks
Space:
O(M)
*/
var leastInterval = function(tasks, n) {
    /* 
    create a counter that shows the amount per each 
    task, so we can plug only the counts into the max heap
    */
    let counter = tasks.reduce((acc, task) => {
        if (task in acc){
            ++acc[task]
        }   
        else {
            acc[task] = 1
        }
        return acc
    }, {})
    let queue = []
    // create the max heap
    let heap = new MaxPriorityQueue()
    let time = 0
    for (let val of Object.values(counter)){
        heap.enqueue(val)
    }
    while (queue.length || heap.size() > 0){
        ++time
        if (heap.size() > 0){
            let {element: remaining} = heap.dequeue()
            /* if there are elements remaining, we push both the remaining (decremented by one), as well as the next valid time onto the queue so that it can be processed at the valid time after its cooldown (time + n)*/
            if (remaining - 1 > 0){
                queue.push({remaining: remaining-1, nextValidTime: time+n})
            }
        }
        if (queue.length){
            let {remaining, nextValidTime} = queue[0]
            /*
            if the element at the top of the queue can be processed
            if its the right time, we pop from the queue,
            and then push the remaining value we saved earlier it back onto the heap so it can be re-processed again in a further iteration. Note that if we can't pop anything off the queue, this would be considered "idle" time.
            */
            if (nextValidTime === time){
                queue.shift()
                heap.enqueue(remaining)
            }
        }
    }
    return time
};