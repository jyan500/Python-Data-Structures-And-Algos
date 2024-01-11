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
            
        