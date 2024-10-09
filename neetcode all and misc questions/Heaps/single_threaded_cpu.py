class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        tasks = [[1,2],[2,4],[3,2],[4,1]]
        subarray[0] is enqueue time
        subarray[1] is processing time
        priority is based on shortest processing time, and then based on the smaller index (whichever element comes first in the list)
        
        things to track:
        What is in the processing queue (what is ready to process), you'd want to use a min heap for this
        since you want the elements with the least processing time needed
        What is actually processing (you can only process one thing at a time), also when this task is finished processing,
        based on the current time + processing time
        
        My original solution:
        Originally, we set the time to be the enqueue time of the first task in our availableTasks min heap, which is sorted based on enqueue time

        if there are still tasks on availableTasks, and tasks have an enqueue time <= currentTime, which means these tasks are ready to be processed,
        we would append to our min heap.

        if the min heap was empty (meaning the processing time already finished before the next
        task can be queued up into the min heap), we would reset the current time to be the new enqueue time so we don't remain
        idling while waiting for the next task.

        Otherwise, we would pop off the min heap, process the task and save the index. Also setting the current time to be time + processing time
        on the current task
        
        The solution below was my first passing attempt, but Neetcode has a similar approach (except he sorts the tasks list instead of 
        putting onto a separate heap, which is more memory efficient, but I found it a bit easier to reason about the problem by putting the 
        available tasks on the separate heap)
        Neetcode: https://youtu.be/RR1n-d4oYqE
        
        Time Complexity: O(NLogN)
        Space: O(N)
        
        Note that this problem and task scheduler are quite similar in concept. 
        
        """
        import heapq
        minHeap = []
        availableTasks = []
        # include the index onto tasks, since if two tasks have the same
        # enqueue and processingTime, the lower index takes precedence
        # originally, we push the tasks such that the heap will be ordered by enqueueTime
        for i in range(len(tasks)):
            enqueueTime, processingTime = tasks[i]
            heapq.heappush(availableTasks, [enqueueTime, processingTime, i])
        minHeap = []
        res = []
        time = availableTasks[0][0]
        while (availableTasks or minHeap):
            # if a task is ready to be processed, pop out of available tasks
            # and push onto minHeap
            while (len(availableTasks) > 0 and availableTasks[0][0] <= time):
                enqueueTime, processingTime, index = heapq.heappop(availableTasks)
                nextProcessingTime = enqueueTime
                heapq.heappush(minHeap, [processingTime, index])
            # if there's no element to process because a task just processed, but the time is not ready
            # for the next task to get pushed on, set the time to the next enqueue time on availableTasks
            if len(minHeap) == 0:
                time = availableTasks[0][0]
            else:
                processingTime, index = heapq.heappop(minHeap)
                res.append(index)
                time += processingTime
        return res
        
            
            
                