class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        similar concept to meeting rooms II

        should sort the trips list based on the start location
        put the end time of the trip on a min heap
        while the top of the min heap's end time is less than the current trip's start time,
            this means we are not overlapping, therefore:
                pop off the min heap, and also decrement the capacity,
                since that means we would've "dropped off" the passengers at the top of the min heap
                since we've already passed that end point.

        otherwise, this means we are overlapping an interval, which means
        check if the capacities can be added together, and append the trip onto the min heap
        
        Time: O(NLogN)
        Space: O(N)
        """
        import heapq
        trips.sort(key=lambda x: x[1])
        minHeap = []
        numPassengers, start, end = trips[0]
        heapq.heappush(minHeap, (end, start, numPassengers))
        curCapacity = numPassengers
        if curCapacity > capacity:
            return False
        for i in range(1, len(trips)):
            curPassengers, start, end = trips[i]
            while (len(minHeap) > 0 and start >= minHeap[0][0]):
                prevEnd, prevStart, prevPassengers = heapq.heappop(minHeap)
                curCapacity -= prevPassengers
            curCapacity += curPassengers
            if curCapacity > capacity:
                return False
            heapq.heappush(minHeap, (end, start, curPassengers))
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Neetcode's Heap Solution:
        1) Sort the trips array by the starting location
        2) Keep a min heap that tracks the dropoff location
        3) if the top of the minheap's dropoff location <= current pickup location,
        this means we could've dropped these passengers off, so continue dropping off before picking up new passengers
        Time: O(NLogN) + O(NLogK)
        Space: O(N)

        The key pattern with these problems (and the CPU/task scheduling problems) is rather than incrementing
        time/location by one to see what the state is at each time, we can jump to a specific time, and then check if a particular condition
        is met to pop off a heap/queue (for example, we jump from one pickup location to the next, and then check if the current pickup location > dropoff location,
        rather than incrementing a location variable by one until we reach a dropoff, and then dropoff, or pickup if location == pickup, as that could create many idle states)
        """
        import heapq
        trips.sort(key=lambda x: x[1])
        dropoffs = [] # pick up location, capacity
        curCapacity = capacity
        for t in trips:
            amt, start, end = t
            # if dropoff location <= current pickup location, continue dropping
            # passengers off
            while (dropoffs and dropoffs[0][0] <= start):
                _, dropoffAmt = heapq.heappop(dropoffs)
                curCapacity += dropoffAmt
            if curCapacity - amt >= 0:
                heapq.heappush(dropoffs, [end, amt])
                curCapacity -= amt
            else:
                return False
        return True
            
        """
        My first accepted solution using similar concept to meeting rooms II:
        car
        A - - - - - - - - B
          from       to
        trips = [[2,1,5], [3,3,7]] capacity = 4
        at 1, pick up 2 passengers, capacity is now 2
        at 3, pick up 3 passengers, capacity is now -1 which is invalid
        
        trips = [[2,1,5], [3,3,7]] capacity = 5
        at 1, pick up 2 passengers, capacity is now 2
        at 3, pick up 3 passengers, capacity is now 5
        at 5, drop off 2 passengers, capacity is now 3
        at 7, drop off 3 passengers, capacity is now 7
        
        This is actually very similar to meetings room II in concept,
        where you separate out the pickup and dropoff locations, and then track two pointers where you check if the dropoff <= pickup, then you increment the dropoff pointer instead of the pickup pointer. Except you would
        also store the capacity as a tuple of (pickUpAmt, pickupLocation) or 
        (dropOffAmt, dropoffLocation)
        
        Time: O(NLogN)
        Space: O(N)
        """
        """
        pickups = [(trips[i][0], trips[i][1]) for i in range(len(trips))]
        dropoffs = [(trips[i][0], trips[i][2]) for i in range(len(trips))]
        pickups.sort(key=lambda x: x[1])
        dropoffs.sort(key=lambda x: x[1])
        curCapacity = capacity
        pickUpPointer = 0
        dropOffPointer = 0
        while (pickUpPointer < len(pickups) and dropOffPointer < len(dropoffs)):
            pickUpAmt, pickUpLocation = pickups[pickUpPointer] 
            dropOffAmt, dropOffLocation = dropoffs[dropOffPointer]
            # if our current pick up location <= dropoff, that means
            # we could've dropped off one set of passengers, so drop these passengers off and increment the drop off pointer
            if dropOffLocation <= pickUpLocation:
                curCapacity += dropOffAmt
                dropOffPointer+=1
                # note that if we're dropping off the same time as we pick up
                # passengers, we need to pick up these passengers after dropping off
                if (dropOffLocation == pickUpLocation):
                    if (curCapacity - pickUpAmt >= 0):
                        curCapacity -= pickUpAmt
                        pickUpPointer += 1
                    else:
                        return False               
            else:
                if (curCapacity - pickUpAmt >= 0):
                    curCapacity -= pickUpAmt
                    pickUpPointer += 1
                else:
                    return False
        return True
        """
        
        

        
        