class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        https://leetcode.com/problems/maximize-distance-to-closest-person/
        
        [1, 0, 0, 0, 1, 0, 1]
        sitting at index 2 would result in the maximum distance between 1's (distance of 2)
        [0, 0, 0, 0, 1]
        sitting at index 0 would result in the maximum distance between 1's (distance of 4)
        
        [1, 0, 0, 1, 0]
        here, the answer would actually be 1 (And not 2), because no matter where you sit, 
        the closest distance to a value seats[i] == 1 is actually 1. Even at index 1,
        even though there's two spaces until index 3, someone is sitting at index 0, and the question
        states that you want to maximize the distance between the closest person
        
        distance would be considered the indices1 - indices2 here (don't need to add 1)
        
        Approach 1:
        iterate through seats array, finding seats[i] == 0
        iterate outwards from seats[i], using l and r, looking for the closest seats[l] == 0 and seats[r] == 0
        find the max distance between the two
        
        Time: O(N^2) since you repeat some work by looping through indices that you've previously visited
        Space: O(1)
        
        Approach 2:
        Store only the indices of the seats where seats[i] == 1 in an array
        in order to maximize the distance, you'd want to calculate the max distance between the two indices (l-r)//2, IF there's at least two seats[i] == 1. 
        However, there are some edge cases to consider when only storing the indices of the occupied seats:
        
            edge case #1:
            -------------
            if the first occupied seat is NOT the first seat, then you have to consider the distance
            between the leftmost unoccupied seat (index 0) and the first occupied seat
            
            edge case #2:
            -------------
            if the last occupied seat is NOT the last seat, then you have to consider the distance
            between the rightmost unoccupied seat (len(seats)-1) and the last occupied seat
            AS well as the halfway distance between the previous occupied seat and the current occupied seat
            which is (occupied[i]-occupied[i-1])//2.
            You would calculate both of these and then take the max between them.
                  
        If there's only one occupied seat (seat[i] == 1):
        then you can just pick either the distance between the leftmost seat and index 0 or the rightmost seat and len(seats)-1 depending on the distance
    
        Time: O(N)
        Space: O(N)
        """
        import math
        occupied = [i for i in range(len(seats)) if seats[i] == 1]
        res = 0
        if len(occupied) > 1:
            for i in range(len(occupied)):
                # edge case #1
                # if the occupied seat is not the first seat,
                # you have to account for the distance between the first un-occupied seat and the first occupied seat
                if i == 0 and occupied[i] != 0:
                    distance = occupied[i]
                # edge case #2
                # if the occupied seat is the last seat
                # you need to take the max between the halfway point of the previous and last seat,
                # as well as the last occupied seat and the LAST unoccupied seat on the right most side
                elif i == len(occupied)-1 and occupied[i] != len(seats)-1:
                    distance1 = len(seats) - occupied[i] - 1
                    distance2 =  distance = (occupied[i] - occupied[i-1])//2
                    distance = max(distance1, distance2)
                else:
                    distance = (occupied[i] - occupied[i-1])//2
                res = max(distance, res)
        else:
            # if the occupied seat is closer to the left, return the distance between the occupied seat and right most seat, otherwise
            # return the distance between the leftmost and the occupied seat
            res = len(seats) - 1 - occupied[0] if len(seats) - occupied[0] > occupied[0] else occupied[0]
            
        return res
            