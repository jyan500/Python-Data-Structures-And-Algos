class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        arr = [3,2,4,1]
        flip at k = 2
        arr = [2,3,4,1]
        flip at k = 3
        arr = [4,3,2,1]
        flip at k = 4
        arr = [1,2,3,4]
        whenever we flip at k, everything before k reverses itself
        
        
        
        Concept: 
        Time complexity: O(N*k), but for each number we make 2 extra operations, and we're also performing
        reverse operations within slices of the array, we'll denote the length of the slice as k
        Space Complexity: O(N), to keep track of the elements array
        
        flip such that the smallest element in the list is at the back
            -initially, flip where our smallest element is, that will bring to the front
            -append k to our result
            -then, we flip k = arr.length, that will bring to the back
            -append k to our result
            -we remove the smallest element from our elements list, and find the smallest again
        continue to flip the next element greater than our smallest, at k = arr.length - 1
        repeat for the next element at k = arr.length - 2
        until our biggest element is at k = 1
        then we just flip the last element to reverse the whole thing and return our answer
    
        Test case
        elements = [4,3,1,2]
        arr = [4,3,1,2]
        placement = 4
        first iteration
        -----------------------------------------
        Our smallest element so far is 1, which is at index 2 (k = 3, since k is one indexed)
        so we flip at k = 3
        reverse [4,3,1] = [1,3,4]
        arr = [1,3,4] + [2] = [1,3,4,2]
        we append k = 3 to our list
        Now that the smallest element is at the front, we bring it to the back (this is denoted by the value placement) by flipping at k = 4 (or i = 3)
        flip at k = 4
        reverse [1,3,4,2] = [2,4,3,1]
        arr = [2,4,3,1]
        we append k = 4 to our list
        we need to remove 1 from elements, and find the index of the new smallest element within arr (which is 2)
        elements = [4,3,2]
        arr = [2,4,3,1], so min_element_index is now 0

        we also decrement placement by 1, since we know our smallest element is at the back, the next smallest element will
        be placed one before that (so arr.length - 1)

        second iteration 
        -----------------------------------------
        min element is now 2
        2,4,3,1

        since our smallest element is already at the front, we don't need to perform a flip to bring it to the front
        flip at k = 3 to bring it to placement (which is now 3, i = 2)
        3,4,2,1

        third iteration
        ------------------------------------------
        min element is now 3

        since our smallest element is already at the front, we don't need to perform the flip to bring it to the front
        flip at k = 2 to bring it to placement (which is now 2, i = 1)
        4,3,2,1

        third iteration
        -----------------------------------------
        min element is now 4

        since our smallest element is already at the front, we don't need to perform the flip to bring it to the front
        flip at k = 4
        1,2,3,4
        
        arr = [4,1,3,2]
        1,4,3,2
        2,3,4,1
        4,3,2,1
        '''
        
        min_element = min(arr)
        max_element = max(arr)
        elements = arr
        min_element_index = elements.index(min_element)
        max_element_index = elements.index(max_element)
        # print(min_element_index)
        results = []
        placement = len(arr)
        while (elements):  
            ## print(arr)
           
            ## bring to the front
            # print('bring to front')
            # print('------------------')
            # print('reversed : ', arr[:min_element_index+1][::-1])
            # print('past: ', arr[min_element_index+1:])

            ## if our min element is already at the front, we don't need to perform this operation to try and bring it to the front
            if (min_element_index != 0):
                arr = arr[:min_element_index+1][::-1] + arr[min_element_index+1:]
                results.append(min_element_index+1)
            ## bring the element to the end of the array by reversing the list
            ## after that, it would be one before the end of the array (k-1)
            ## (k-2)
            # print('result: ', arr)
            # print('bring to placement')
            # print('---------------------')
            # print('reversed: ', arr[:placement][::-1])
            # print('past: ', arr[placement:])
            arr = arr[:placement][::-1] + arr[placement:]
            # print('to placement: ', arr)
            results.append(placement) 
            placement -= 1
            
            elements.remove(min_element)
            if (elements):
                min_element = min(elements)
                min_element_index = arr.index(min_element)
        ## once we get it to a configuration where its just a reversed list
        ## all we would need to do is just reverse, so flip at k = arr.length
        results.append(len(arr))
        return results
        
        
        
        
        