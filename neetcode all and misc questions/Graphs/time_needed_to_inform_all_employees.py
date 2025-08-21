'''
https://leetcode.com/problems/time-needed-to-inform-all-employees/

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

https://www.youtube.com/watch?v=NWZzo6m40kY&ab_channel=CatRacket

Time complexity of O(N+M), where N is the number of managers and M is the number of employees
Space complexity of O(N), where N is the number of employees on the queue 

Concept:
1) This is graph problem, use BFS, create an adjacency list (list of lists), where the index of the inner list
represents the manager, and the items within the inner list represents its employees
2) In our BFS, within the queue, store the current employee node, as well as the amount of time taken so far to reach this employee
3) we want to have a global max that gets updated whenever we pop from the queue, and compare the time taken so far to our max
4) at the end, the time taken to inform all employees is essentially this global max, as the amount of time taken to inform
all employees will always be "bottlenecked" by the employee tha takes the longest to inform. 

(You can see this in the breakdown of test case #4) 
Two important concepts that I missed while doing this problem was that:
1) I didn't understand what the informTime array meant,
whenever we calculate the amount of time taken to inform the next employee, its always 
the (total time taken so far + informTime[manager]), where informTime[manager] is the amount of time needed for this manager 
to inform its employees

2) I didn't realize that the time needed to inform all employees is essentially the max amount of time needed
to reach any employee (since for any time_so_far < max_time, this employee would've already been informed by the time the 
last employee was informed). Also, this is not necessarily the employee in the lowest level of the tree, as depending on the 
informTime values, the employee in the lowest level isn't necesarily the employee that takes the longest to inform.
'''

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        Revisited 8/20/2025
        BFS problem with queue
        (The tricky part is figuring out how to construct the adjacency list)

        create an adjacency list, mapping each index of the manager array to its employee
        append (current employee, inform time so far) on the queue
        perform BFS with the inner for loop

        (similar concept to rotting oranges BFS problem)
        """
        from collections import deque
        adj = {}
        for i in range(len(manager)):
            adj[i] = []
        for i in range(len(manager)):
            if manager[i] != -1:
                # map the manager to the employee
                if i in adj:
                    adj[manager[i]].append(i)
        maxTime = 0
        q = deque()
        q.append((headID, 0))
        while (q):
            N = len(q)
            for i in range(N):
                employee, timeSoFar = q.popleft()
                maxTime = max(timeSoFar, maxTime)
                for subordinate in adj[employee]:
                    q.append((subordinate, timeSoFar + informTime[employee]))
        return maxTime

class Solution:
    from collections import deque
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        Test Case #1
        --------------------------------
        n = 7
        headID = 6
        manager = [1,2,3,4,5,6,-1]
        employee = 0,1,2,3,4,5,6 
        
        6
          5
            4
              3
                2
                  1
                    0
        
        Test Case #2
        --------------------------------
        n = 7 headID = 0
        manager = [-1, 0, 0, 1, 1, 2, 2]
        employees.  0, 1, 2, 3, 4, 5, 6
        informTime = [1,3,2,0,0,0,0]
        alternate informTime? = [1,1,2,1,3,1,1,0,0,0,0,0,0,0,0]
        0
      1   2
    3 4        5 6
    
        Test Case #3
        --------------------------------
        n = 4
        headID = 2
        manager = [3,3,-1,2]
        employee= [0, 1, 2, 3]
        informTime = [0,0,162,914]
        
        2
          3
        0  1
        
        Test case #4
        --------------------------------
        n=11
        headID = 4
        manager = [5,9,6,10,-1,8,9,1,9,3,4]
        employee   0,1,2,3,4,5,6,7,8,9,10
        informTime = [0,213,0,253,686,170,975,0,261,309,337]
        
        4
          10 
            3   
              9  
             1  6  8  
             7  2  5 
                   0
        
          
        '''
        ## build adjacency list, where we map the manager to its employees
        adj_list = []
        for i in range(len(manager)):
            adj_list.append([])
        for i in range(len(manager)):
            m = manager[i]
            employee = i
            ## if not the head manager
            if (manager[i] != -1):
                ## map the manager to its employees, where the manager is manager[i]
                ## and the employee is i
                adj_list[m].append(employee)
        ## find the head, we're given the headID
        queue = deque()
        queue.append((headID, 0))
        max_time = 0
        
        while (queue):
            print(queue)
            for i in range(len(queue)):
                cur_manager, time_so_far = queue.popleft()
                max_time = max(max_time, time_so_far)
                ## find the employees of the given manager and add them to the queue
                for employee in adj_list[cur_manager]:
                    ## the important point is that the total inform Time needed to reach all employees
                    ## is essentially the max_time needed to reach a specific employee
                    ## as that employee is the "bottleneck", since we could've informed everyone else
                    ## except this employee
                    queue.append((employee, time_so_far + informTime[cur_manager]))

        return max_time
        ## the following solution does not use an adjacency list, as a result
        ## there's an extra O(N) overhead to find the employees of a given manager
        ## resulting in a O(N*(N+M)) time complexity
        # queue = deque()
        # queue.append((headID, 0))
        # max_time = 0
        # while (queue):
        #     print(queue)
        #     for i in range(len(queue)):
        #         new_head, time_so_far = queue.popleft()
        #         max_time = max(max_time, time_so_far)
        #         ## find subordinates and add them to the queue
        #         for j in range(len(manager)):
        #             if (manager[j] == new_head):
        #                 queue.append((j, time_so_far + informTime[new_head]))
        # return max_time
    
    '''
    Breakdown of Test case #4
    --------------------------------
     n=11
        headID = 4
        manager = [5,9,6,10,-1,8,9,1,9,3,4]
        employee   0,1,2,3,4,5,6,7,8,9,10
        informTime = [0,213,0,253,686,170,975,0,261,309,337]
        4
          10  
            3   
              9  
             1  6  8  
             7  2  5 (the employee that takes the longest to inform is 2, with 2560 total time)
                   0
    queue = [(4,0)]
    first iter
    new_head, time_so_far = queue.popleft() = 4, 0
    max_time = max(0, 0) = 0
    manager[10] == 4 (true),
    queue.append(10, 0 + 686) (takes 686 to inform 10 so far)
    
    second iter
    new_head, time_so_far = queue.popleft() = 10, 686
    max_time = max(0, 686) = 686
    manager[3] == 10 (true),
    queue.append(3, 686 + informTime[new_head] = 686 + 337 = 1023) (takes 1023 seconds to inform up to employee 3)
    
    third iter
    new_head, time_so_far = queue.popleft() = 3, 1023
    max_time = max(686, 1023) = 1023
    manager[9] == 3
    queue.append(9, 1023 + informTime[9] = 1023 + 253 = 1276) (takes 1276 seconds to inform up to employee 9)
    
    fourth iter
    new_head, time_so_far = queue.popleft() = 9, 1276
    max_time = max(1023, 1276) = 1276
    manager[1] = 9, manager[6] == 9, manager[8] == 9, at informTime[9], we know it will take 309 to inform all three of these employees (1,6,8)
    queue.append(1, 1276+309=1585), queue.append(6, 1276+309=1585), queue.append(8,  1276+309=1585)
    
    fifth iter
    first queue iter
        since we have 3 items in the queue now, we need to loop an additional 3 times
        new_head, time_so_far = queue.popleft() = 1, 1585
        max_time = max(1276, 1585)

        manager[7] == 1, queue.append(7, 1585 + informTime[1] = 1585+213=1798) (it will take 1798 to inform employee 7)
    second queue iter
        new_head, time_so_far = queue.popleft() = 6, 1585
        max_time = max(1276, 1585)
        manager[2] == 6, queue.append(2, 1585 + informTime[6] = 1585 + 975 = 2560) (it will take 2560 to inform employee 2)
    third queue iter
        new_head, time_so_far = queue.popleft() = 8, 1585
        max_time= max(1276, 1585)
        manager[5] == 8, queue.append(5, 1585 + informTime[8] = 1585 + 261 = 1846) (it will take 1846 to inform employee 5)
        
    sixth iter
    first queue iter
        we have 3 items in the queue again
        new_head, time_so_far = queue.popleft() = 7, 1798
        max_time = max(1585, 1798) = 1798
        7 is not a manager, no queue items added
    second queue iter
        new_head, time_so_far = queue.popleft() = 2, 2560
        max_time = max(1798, 2560) = 2560
        2 is not a manager of anyone, no queue items added
    third queue iter
        new_head, time_so_far = queue.popleft() = 5, 1846
        max_time = max(2560, 1846) = 2560 
        manager[0] == 5
        queue.append(0, 1846 + 170 = 2016) (it will take 2016 to inform 0)
    
    seventh iter
        new_head, time_so_Far = queue.popleft() = 0,2016
        max_time = max(2560, 2016) = 2560
        0 is not a manager of anyone
        
    we can see at the end, we return 2560 as this is the max time taken to get to an employee,
    which represents the total amount of time taken to reach all employees
    
    '''
            