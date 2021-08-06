class Solution:
    ## O(N) Time, O(N) space solution
    ## handling three cases (all negative numbers), (all positive numbers), (both)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ## for a case with all negative numbers:
        ## check if the last element in the list is negative, in that case, all numbers
        ## before that will also be negative, so if we just take squares and reverse the list, and it'll be in sorted order, since the square of a negative is a positive
        ## for example, [-4,-2,-1]
        ## squares are [16,4,1]
        ## reverse is [1,4,16] which is correct
        if (nums[-1] < 0):
            for i in range(len(nums)):
                nums[i] = nums[i]**2
            ## return the reverse of the list
            return nums[::-1]
        ## for a case with all positives
        ## if the first element is positive, then all elements proceeding will be positive and in sorted order
        ## just get all the squares and return the list
        elif (nums[0] > 0):
            for i in range(len(nums)):
                nums[i] = nums[i]**2
            return nums
            
        ## for a case with positive and negative numbers:
        ## 1. apply linear scan to find the first positive number
        ## 2. everything beyond that point is already going to be sorted
        ##    so we don't need to resort that, so just place those numbers into an array
        ## 3. we can simply reverse all the numbers to the left of the first positive number
        ##    because these numbers will go from negative to positive, they're already going
        ##    to be in sorted order, so places these numbers in reverse order into an array
        ## 4. merge the two sorted lists together
        ## for example
        ## [-4,-1,0,3,10]
        ## split into [0,3,10]
        ## and [-4,-1]
        ## calculate the squares of the negatives
        ## [16,1]
        ## then reverse the list
        ## [1,16]
        ## then merge [1,16] with [0,3,10]
        ## 
        else:    
            first_positive_num_index = float(-inf)
            for i in range(len(nums)):
                if (nums[i] == 0 or nums[i] > 0):
                    first_positive_num_index = i
                    break
        
            all_positives = nums[i:]
            all_negatives = nums[:i]
            squares1 = []
            squares2 = []
            for i in range(len(all_positives)):
                squares1.append(all_positives[i] ** 2)
            for i in range(len(all_negatives)):
                squares2.append(all_negatives[i] ** 2)
            ## this will place the squares of each number into reverse order, which actually sorts them
            ## (see above example in the first nums[-1] < 0 case)
            squares2 = squares2[::-1]
            
            ## merge the two sorted arrays
            merged = []
            i = 0
            j = 0
            ## if one of the numbers in one list is less than the other
            ## we add the lesser number to our merged
            ## and only increment the pointer of our list that contained our lesser number
            ## this will continue until the number is no longer smaller,
            ## then we'll increment the pointer of the other list
            while (i < len(squares1) and j < len(squares2)):
                if (squares1[i] < squares2[j]):
                    merged.append(squares1[i])
                    i+=1
                elif (squares2[j] < squares1[i]):
                    merged.append(squares2[j])
                    j+=1
                else:
                    merged.append(squares1[i])
                    merged.append(squares2[j])
                    i+=1
                    j+=1
                
            ## if one of the lists is longer than the other, we need to append the remainder of the longer list
            ## if the lists were the same length, we're done, return merged
            if i == len(squares1) and j == len(squares2):
                return merged
            ## if i has reached the end of its list, but j has not reached the end, append the rest of j
            elif i == len(squares1) and j < len(squares2):
            ## if j has reached the end of its list, but i has not reached the end, append the rest of i
                return merged + squares2[j:]
            elif j == len(squares2) and i < len(squares1):
                return merged + squares1[i:]
            
            
                
        