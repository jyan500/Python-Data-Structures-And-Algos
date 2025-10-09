class Solution:
    """
    O(N) Time
    O(N) Space
    Keep track of the current time that starts incrementing starting from the first customer in the list
    Also keep track of the customer's waiting time in an array
    The one edge case is that if the customer's arrival time > currentTime, we need to set the 
    currentTime = customerArrivalTime, since the chef cannot start cooking until the customer has arrived.

    customers = [[5,2],[5,4],[10,3],[20,1]]

    i = 0
    currentTime = 5
    customerArrivalTime = 5, timeToFinish = 2
    currentTime = 5 + 2 = 7
    waitingTime = 7 - 5 = 2

    currentTime = 7
    waitingTimes = [2]

    i = 1
    currentTime = 7
    customerArrivalTime = 5, timeToFinish = 4
    currentTime = 7 + 4 = 11
    waitingTime = 11 - 5 = 6
    
    currentTime = 11
    waitingTimes = [2, 6]

    i = 2
    currentTime = 11
    customerArrivalTime = 10, timeToFinish = 3
    currentTime = 11 + 3 = 14
    waitingTime = 14 - 10 = 4

    currentTime = 14
    waitingTimes = [2, 6, 4]

    i = 3
    This is the edge case, 
    currentTime = 14
    customerArrivalTime = 20, timeToFinish = 1
    we have to wait until time 20 since time is only 14, so just set currentTime = 20
    currentTime = 20

    also add in the timeToFinish
    currentTime = 20 + 1 = 21
    waitingTime = 21 - 20 = 1
    waitingTimes = [2, 6, 4, 1]

    Average = sum(waitingTimes)/len(waitingTimes) = 13/4 = 3.25
    """
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # start at the waiting time
        currentTime = customers[0][0]
        waitingTimes = []
        for customerArrivalTime, timeToFinish in customers:
            # if the customer arrives at a time > currentTime, need to set the currentTime
            # to the customerArrivalTime
            if customerArrivalTime > currentTime:
                currentTime = customerArrivalTime
            # add the amount of time it takes to finish the dish to the current time
            currentTime += timeToFinish
            # to get the waiting time, subtract the time the customer arrived with the current time after
            # the dish is finished
            waitingTimes.append(currentTime - customerArrivalTime)
        return sum(waitingTimes)/len(waitingTimes)