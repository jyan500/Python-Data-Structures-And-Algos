'''
https://leetcode.com/problems/find-k-closest-elements/
'''

class Solution: 
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        '''
        https://leetcode.com/problems/find-k-closest-elements/discuss/780121/Python-Easy-to-Understand-Solution
        https://leetcode.com/problems/find-k-closest-elements/discuss/565833/Clean-Python-Solution
        figure out the distance of each arr element to x
        
        
        [1,2,3,4,5], x = 3
        distance between 1 and 3 is 2
        distance between 2 and 3 is 1
        distance between 3 and 3 is 0
        distance between 4 and 3 is 1
        distance between 5 and 3 is 2
        we pick 1,2,3,4 because although 2 and 3 are equally distant, and 1 and 5 are equally distant
        between 1 and 5, 1 < 5 so we pick 1
        
        -1 0 [1,2,3,4,5]
        distance between 1 and -1 = 2
        distance between -1 and 2 = 3
        ...
        distance between -1 and 5 = 6
        k = 4, so pick the first 4
        
        Concept: 
        Time complexity: O(N)
        space complexity: O(N)
        
        if the length of our array remains greater than k
        we calculate the distances between the first element to x and the last element to x of the array
        called dist1 and dist2
        if the first element is closer to x than the last element is, we pop the last element off
        if the last element is closer to x than the first element is, we pop the first element off
        both operations will decrease the length of the array until == k
        
        at that point we just return our result
        
        
        
        '''
        if (len(arr) == k):
            return arr
        res = arr
        while (len(res) > k):
            ## get the distance between x and first element of the array
            dist1 = abs(arr[0]-x)
            ## get the distance between x and last element of the array
            dist2 = abs(arr[-1]-x)
            ## if first element is closer to x than the last element, pop the last element off the array
            ## also handles the case when the distance is equal, we prefer to keep the smaller 
            ## element which will be the lower index item in the list since its sorted ascending
            if (dist1 <= dist2):
                res.pop()
            ## if the last element is closer to x that the first, pop the first element off the array
            else:
                res.pop(0)
        return res
        
        '''
        Test Cases
        
        [1,2,3,4,5], k = 4, x = -1
        -------------------------------
        1st iteration
        dist1 = abs(1-(-1))=2
        dist2 = abs(5-(-1))=6
        dist1 < dist2, so pop off the last element
        [1,2,3,4]
        
        len(res) == 4 == k, so we're done
        
        [1,2,3,4,5], k = 2, x = -1
        -------------------------------
        1st iteration
         dist1 = abs(1-(-1))=2
        dist2 = abs(5-(-1))=6
        dist1 < dist2, so pop off the last element
        [1,2,3,4]
        
        2nd iteration
        dist1 = abs(1-(-1))=2
        dist2 = abs(4-(-1))=5
        dist1 < dist2, so pop off the last element
        [1,2,3]
        
        3rd iteration
        dist1 = abs(1-(-1))=2
        dist2 = abs(3-(-1))=4
        dist1 < dist2, so pop off the last element
        [1,2]
        len([1,2]) == k, we're done
        
        result = [1,2]
        
        [1,3,4,5,8,9], k = 3, x = 4
        1st iteration
        dist1 = abs(1-4)=3
        dist2 = abs(9-4)=5
        dist1 < dist2, pop off the last element
        [1,3,4,5,8]
        
        2nd iteration
        dist1 = abs(1-4)=3
        dist2 = abs(8-4)=4
        dist1 < dist2, pop off the last element
        [1,3,4,5]
        
        3rd iteration
        dist1 = abs(1-4)=3
        dist2 = abs(5-4)=1
        dist2 < dist1, pop off the first element
        [3,4,5]
        
        len([3,4,5]) == k, we're done
        result = [3,4,5]
        '''
        
            
        