"""
https://leetcode.com/problems/task-scheduler/
https://www.youtube.com/watch?v=s8p8ukTyA2I&ab_channel=NeetCode
Time Complexity: O(mlog(26) * n), where m is the number of tasks, log26 represents the constant num of characters 
whenever we do heappop(), and n is the cooldown period between same tasks

Because log(26) is basically constant, we can simplify this to O(m*n)

Space Complexity: O(m), where m is the number of tasks

Key Concepts:
1) We map the tasks to its amount of occurrences
2) Our goal is to start by getting the tasks with the most of amount of occurrences
done first, as we can schedule tasks with less occurrences during the idle time
3) Create a max heap, by inverting the count of that given task
4) Track our current time 
5) We will also keep track of a queue that will store the task that was just processed. Specifically,
we store the current time (time) as well as the next time that this task can be processed (time + n)
6) Within the while loop, if there's a task that we can process, we pop off the max heap and add that to our queue
7) If there's already an item in our queue, check the top item, and see if our current time has reached
the time which this task can be processed again. If so, add that back to our max heap
8) We will end the iteration when there's no more items in both our max Heap and queue

Example:

["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

Counter=  A:6, B:1, C:1, D:1, E:1, F:1, G:1
Max Heap = [-6, -1, -1, -1, -1, -1, -1]
Queue = []
Time = 0

1)
increment time by 1
Pop -6 off the max heap (representing A)
Add to our queue, where the next time this can be processed is 1 + n, which is 3
Also increment by 1 (this is essentially decrementing, but we're using negative numbers to represent the max heap)

Max Heap = [-1, -1, -1, -1, -1, -1]
Queue = [(-5, 3)]
Time = 1
illustration of our current process: "A"

2)
increment time by 1
Pop -1 off the max heap (representing B)
However, we don't add B to the queue, since 1 + -1 = 0, this is the only
time we would need to process B

Max Heap = [-1, -1, -1, -1, -1]
Queue = [(-5, 3)]
Time = 2
current process "A" -> "B"

3) 
increment time by 1, time is now 3
Pop -1 off the max heap, don't need to add it to the queue 

Max Heap = [-1, -1, -1, -1]

However, we can process A again since our current time is 3,
and the item on the queue is (-5, 3)
Pop off the queue, and add back to our heap

Max Heap = [-5, -1, -1, -1, -1]
Queue = []
Time = 3
current process "A" -> "B" -> "C"

4) 
Increment time by 1 (4)
Pop -5 off the max heap (representing A) 
Add to our queue, remaining goes from -5 to -4, next time is 4 + n which is 6

Max Heap = [-1, -1, -1, -1]
Queue = [(-4, 6)]
time = 4
current process "A" -> "B" -> "C" -> "A"

5) 
Increment time by 1 (5)
Pop -1 off the max heap (representing D)
Since it's -1, don't add to the queue

Max Heap = [-1, -1, -1]
Queue = [(-4, 6)]
time = 5
current process "A" -> "B" -> "C" -> "A" -> "D"

6) 
Increment time by 1 (6)
Pop -1 off the max heap (representing E)
maxHeap = [-1, -1]
Since it's -1, don't add to the queue

Note that we can pop the item off queue because 6 == 6, add back to the heap

Max Heap = [-4, -1, -1]
Queue = []
time = 6
current process "A" -> "B" -> "C" -> "A" -> "D" -> "E"

7) 
Increment time by 1 (7)
Pop -4 off the max heap, add to the queue
remaining goes from -4 to -3, next time is 7 + n which is 9

Max Heap = [-1, -1]
Queue = [(-3, 9)]
time = 7
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A"

8)
Increment time by 1 (8)
Pop -1 off the max heap (representing F)
Since it's -1, don't add to queue

Max Heap = [-1]
Queue = [(-3, 9)]
time = 8
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F"

9)
Increment time by 1 (9)
Pop -1 off the max heap (reresenting G)
Since its -1, don't add to queue

MaxHeap = []

Note that we can pop the item off queue because 9 == 9, add back to the heap
next time is 9 + n = 11

MaxHeap = [-3]
Queue = []
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G"

10)
increment time by 1 (10)
Pop off max heap [-3],
remaining becomes -2, 12
Queue = [(-2, 12)]

Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A"

11)
Increment time by 1 (11)
There's nothing on max heap, this would be "idle"
MaxHeap = [-3]
Queue = []

Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A" -> "idle"

12) 
increment time to 12
12 == 12, pop off queue and add to max heap

MaxHeap = [(-2)]
Queue = []
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A" -> "idle" -> "idle"

13)
Increment time (13)
Pop off max heap
add to queue, remaining becomes -1, 15

MaxHeap = []
Queue = [(-1, 15)]
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A" -> idle -> idle -> "A""

14)
Increment time to 14
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A" -> idle -> idle -> "A" -> idle

15)
Increment time to 15
nothing on max heap
15 == 15, pop off queue and add to max heap

maxheap = [-1]
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A" -> idle -> idle -> "A" -> idle -> idle

16)
Increment time to 16
pop off max heap, don't add to queue since -1
Current process "A" -> "B" -> "C" -> "A" -> "D" -> "E" -> "A" -> "F" -> "G" -> "A" -> idle -> idle -> "A" -> idle -> idle -> "A"

Both empty, iteration ends

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Revisited 12/30/2025 with max heap and min heap solution. This time, I just
        stored on the frequency as an additional element on the tuple on the min heap

        Time Complexity: O(KLogK * N)
        where N is the length of the tasks array, K is the number of unique tasks (26 total since its uppercase letters A - Z)

        tasks max heap to store both the task and its frequency. This is a greedy approach
        where we always use up the most frequently occurring element if possible.
        use min heap to store tasks and the next time they can be used
        current time
        while (tasks)
            examine the tasks that are on the min heap
                see if top of the min heap, the current time > next time the task can be used
                    remove from min heap
                    put back onto the queue

            examine the tasks on the max heap
                pop off a task and place onto the min heap if the frequency - 1 > 0,
                storing the next time this can be used by taking
                current time + n
                decrement frequency

            increment current time
        return current time

        """
        from collections import Counter
        import heapq
        c = Counter(tasks)
        maxHeap = []
        minHeap = []
        currentTime = 0
        for key, value in c.items():
            heapq.heappush(maxHeap, (-value, key))
        while (maxHeap or minHeap):
            # if the cooldown time of the task on the top of the minheap
            # has passed, put it back onto the max heap for processing
            while (minHeap and minHeap[0][0] < currentTime):
                timeValue = heapq.heappop(minHeap)
                value = timeValue[1]
                freq = timeValue[2]
                heapq.heappush(maxHeap, (-freq, value))
            if maxHeap:
                freqValue = heapq.heappop(maxHeap)
                freq = -1 * freqValue[0]
                value = freqValue[1]  
                if (freq - 1 > 0):
                    heapq.heappush(minHeap, (currentTime + n, value, freq-1))
            currentTime += 1
        return currentTime

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Revisited 7/1/2025, I think I flipped the ordering of the min heap popping first and then the max heap after
        which led to a slightly different solution, where I needed to add 1 to the cooldown time
        
        We can use a max heap here since we keep track of the tasks that have the highest frequency,
        and prioritize scheduling those tasks
        We can also use a min heap to keep track of the cooldown for tasks, in order to keep track
        of the next time a task can be scheduled

        {A: 3, B: 3}
        n = 3

        curTime = 1
        maxHeap = [(3, A), (3, B)]
        minHeap = []
        pops out
        counter = {A:2, B:3}
        maxHeap((3, B))
        minHEap = [(5, A)]

        curTime = 2
        maxHeap = (3,B)
        minHeap = [(5, A)]

        pops out
        counter = {A:2, B:2}
        maxHeap = []
        minHeap = [(5, A), (6,B)]

        curTime = 3
        top of minHeap not ready to be popped out, nothing in the max heap to pop,
        so this is idle time

        """
        from collections import Counter
        import heapq
        c = Counter(tasks)
        maxHeap = []
        minHeap = []
        for key in c:
            heapq.heappush(maxHeap, (-c[key], key))
        currentTime = 0
        while (maxHeap or minHeap):
            # before popping from the max heap,
            # check to see if any tasks can be put back into the max heap
            if len(minHeap) > 0:
                if minHeap[0][0] == currentTime:
                    time, task = heapq.heappop(minHeap)
                    heapq.heappush(maxHeap, (-c[task], task))
            if len(maxHeap) > 0:
                time, task = heapq.heappop(maxHeap)
                # convert back to positive
                time = time * -1
                # decrement task count
                c[task] -= 1
                # add onto the min heap the next time the task is available if there are still
                # more quantity for that task
                if c[task] > 0:
                    heapq.heappush(minHeap, (currentTime + n + 1, task))
            currentTime += 1
        return currentTime
            
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Revisited on 2/20/2025 using 2 heaps, max heap to store the tasks based
        on the frequency and min heap to store the next time a task is available to process.
        
        X -> Y -> idle -> X -> Y

        num cycles = 0
        available tasks = [x, y]
        heap = []

        each iteration, take from available tasks
        place a tuple onto the heap, that contains the task,
        as well as the "next" time this task is available

        once the task is available again, we pop off the heap
        and put it back into available tasks

        we want to use a min heap to prioritize the tasks
        that are ready to be used again

        if the task amount has reached 0, do no push back onto the max heap

        maxHeap = [(-2, X), (-2, Y)]
        minHeap = []
        numCycles = 0

        pop out the max heap,
        maxHeap = [(-2, Y)]
        minHeap = [(2, (-1, X))]
        numCycles = 1

        pop out the max heap
        maxHeap = []
        minHeap = [(2, (-1, X)), (3, (-1, Y))]
        numCycles = 2

        nothing in the max heap
        min heap
        """
        from collections import Counter
        import heapq
        c = Counter(tasks)
        maxHeap = []
        minHeap = []
        for task in c:
            heapq.heappush(maxHeap, (-c[task], task))
        numCycles = 0
        while (maxHeap or minHeap):
            if len(maxHeap) > 0:
                amtRemaining, task = maxHeap[0]
                if (-1 * amtRemaining) > 0:
                    amtRemaining, task = heapq.heappop(maxHeap)
                    amtLeft = -1 * ((-1 * amtRemaining) - 1)
                    # push the next time this task is available, as well
                    # as the remaining count and the task
                    if (-1 * amtLeft) > 0:
                        heapq.heappush(minHeap, (numCycles + n, (amtLeft, task)))
            # if there's a task ready to be taken off the min heap,
            # put back onto the max heap
            if len(minHeap) > 0:
                time, taskTuple = minHeap[0]
                # if the task is available to be processed again,
                # pop it out of the min heap and push back to the max heap
                if time <= numCycles:
                    time, taskTuple = heapq.heappop(minHeap)
                    heapq.heappush(maxHeap, taskTuple)
            numCycles += 1
        return numCycles


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """      
        10/2/2024
        https://neetcode.io/problems/task-scheduling
        I was able to recall some of the solution and reverse engineer it.
        The time complexity: O(NLogN) + O(N * KLogN) , where K is the max frequency of a task and N 
        is the amount of tasks. O(NLogN) for building the max heap initially

        "A" "A" "A" "B" "C"
        n = 3
        a -> b -> c -> idle -> a -> idle -> idle -> idle -> a
        (idle because 3 tasks have already been done)

        For example, I pick A, so the next time I can pick A is currentTime + n
        I'd then remove A from the heap that tracks available tasks (call it heap #1), and place it
        on a different heap that tracks the next available time this task can be picked (heap #2). 
        And then increment currentTime by one. 
        Then in the next iteration, check to see if a task on heap #2 is available. If so, I can pop off
        heap #2 and put it back on heap #1

        Another key is picking the element that has the most frequencies first, so that
        you can pick the next most frequent element within the cooldown time period. Using a max heap
        would help for this, as the tasks that have the most frequencies always ends up in the front.
        """
        import heapq
        from collections import Counter
        counter = Counter(tasks)
        processing = []
        tasks = []
        # use a max heap so that the tasks that are the most frequently occurring are processed first
        for task in counter.keys():
            heapq.heappush(tasks, (-counter[task], task))   
        currentTime = 0
        while (len(counter) > 0):
            while (len(processing) > 0 and processing[0][0] == currentTime):
                time, task, amt = heapq.heappop(processing)
                if task in counter and counter[task] > 0:
                    heapq.heappush(tasks, (amt, task))    
            """
            find an available task on tasks. If there's no tasks that can be done,
            this would be considered "idle" time, so the currentTime gets incremented by one        
            if there's still more of this task, add the task
            onto the processing min heap, with currentTime + n, to show that this is the next time
            this task can be processed.
            decrement the counter to show one of these tasks has been processed
            """
            for amt, task in tasks:
                if counter[task] > 0:
                    # because tasks is a max heap, the amt is negative, so convert back to positive
                    # and decrement.
                    newAmt = (-1 * amt) - 1
                    heapq.heappush(processing, (currentTime + n + 1, task, -newAmt))
                    heapq.heappop(tasks)
                    counter[task] -= 1
                    if (counter[task] == 0):
                        del counter[task]
                    break
            currentTime += 1
        return currentTime

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        import heapq
        if n == 0:
            return len(tasks)
        counter = dict()
        for i in range(len(tasks)):
            if tasks[i] in counter:
                counter[tasks[i]] += 1
            else:
                counter[tasks[i]] = 1
        maxHeap = []
        for task in counter:
            maxHeap.append(-counter[task])
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while (maxHeap or q):
            time += 1
            if maxHeap:
                top = heapq.heappop(maxHeap)
                invertedAmt = top
                if invertedAmt + 1 < 0:
                    q.append((invertedAmt + 1, time + n))
            if q:       
                remainingTime, nextProcessingTime = q[0]
                if nextProcessingTime == time:
                    q.popleft()
                    heapq.heappush(maxHeap,remainingTime)
            
        return time
            
        