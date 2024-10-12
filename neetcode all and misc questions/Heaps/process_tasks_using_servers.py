class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/process-tasks-using-servers

        Time Complexity: each server can get pushed and popped off the heap multiple times depending on how long
        each task takes.
        Assuming one server is popped in and out of a min heap for each task, where each task only takes one second,
        then the time complexity would be O(NLogK), where N is the amount of tasks, and K is the amount of servers
        on the heap
        Space: O(N), where N is the amount of tasks  
        servers - server weights
        tasks - time needed to process task
        
        tasks are assigned to servers using a task queue
        second j, jth task inserted into queue
        as long there are free servers and task is not empty, front of the queue gets assigned to
        free server with smallest weight
        
        in case of a tie, (i.e two servers with the same weight), server with the smaller index is chosen
        
        if no free servers, and queue is not empty, we idle until a server becomes free again. If multiple servers
        become free, multiple tasks from queue get pulled out, assigned based on order of insertion based on server weight/index
        
        server next available time based on j at second t is t + tasks[j]
        
        Return an array of length M, where each index is the server the jth task will be assigned to
        
        res = []
        servers = 3 3 2
        tasks = 1 2 3 2 1 2
        time 0: task 0 is added (which takes 1 second to process). Server 2 is used first since it has the smallest weight (res = [2])
        time 1: server 2 becomes free, task 1 is added and server 2 will process it, server 2 is now occupied until second 3 (res = [2,2])
        time 2: task 2 is added, processed by server 0 (note that server 0 and server 1 have the same weight, but server 0 is preferred), 
        server 0 is now occupied until time = 5 (2 + 3) (res = [2,2,0])
        time 3: server 2 becomes free. Task 3 is added and processed using server 2 until second 5 (res = [2,2,0,2])
        time 4: task 4 is added and processed by server 1 because the other servers are busy, server 1 is occupied until time 5 (res = [2,2,0,2,1])
        time 5: all servers become free, task 5 is added and processed using server 2 until second 7 (res = = [2,2,0,2,1,2])
        
        in this example:
        servers = 3 3 2
        tasks = 1 1 1
        if there were 3 tasks, all taking one second each, the server 2 would be assigned and then freed up the following second
        
        servers = 3 3 2
        tasks = 2 2 2
        in this case, first server 2 would get assigned, so the next available time for server 2 would be t = 2
        at t = 1, server 0 gets assigned
        at t = 2, server 2 is freed up, so server 2 gets assigned here
        
        what if all the tasks are queued up and there's no more free servers? instead of incrementing time by one,
        we would set the time when the next server is freed up
        
        
        """
        import heapq
        from collections import deque
        # create a min heap that contains all available servers. As a server is chosen, it gets popped off, 
        # and then stored in a different min heap to show that it's processing a task, ordered by completion time ascending.
        freeServers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(freeServers)
        busyServers = []
        # stores the events that are queued up but haven't been selected by a server yet
        processingQueue = deque()
        t = 0
        res = []
        i = 0
        while (i < len(tasks) or processingQueue):
            # if a task is complete, pop it off
            while (busyServers and busyServers[0][0] == t):
                _, serverWeight, index = heapq.heappop(busyServers)
                heapq.heappush(freeServers, (serverWeight, index))
            # add the task at task[i] to the processing queue
            if (i < len(tasks)):
                processingQueue.append(tasks[i])
                i+=1 
            # if there are freeServers, continue popping and assigning the most recent task
            # on the processing queue, storing the current time t + processingTime, serverWeight and index
            # onto the busyServer min heap
            while (freeServers and processingQueue):
                serverWeight, index = heapq.heappop(freeServers)
                processingTime = processingQueue.popleft()
                heapq.heappush(busyServers, (t + processingTime, serverWeight, index))
                res.append(index)
            # if there all tasks are queued up already and no more free servers,
            # set the time to when the next server is freed up (i.e the top of busy servers)
            if i == len(tasks) and not freeServers:
                t = busyServers[0][0]
            # otherwise, increment time by one to indicate that the next task will be queued up
            # at the following second
            else:
                t+=1
        return res
        
        