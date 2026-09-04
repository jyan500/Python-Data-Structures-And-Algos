/* 
Note in this problem,
nums1 always contains the amount of elements
m + n, padded with zeroes to contain the right amount after 
merging nums2

nums1 = [10,20,20,40,0,0], m = 4
nums2 = [1,2], n = 2

In this algorithm, we use two pointers but rather than relying on the
"merge sort" approach where you start from the front and return a new array,
you start merging from the BACK of nums1 instead.
so the problem actually requires a third pointer called "last", which indicates
the position that needs to be overwritten in nums1

for example
last starts at m + n - 1, which is 5
initially you would compare 40 and 2 (which is m-1 and n-1)
since 40 > 2, you would then overwrite index 5 on nums1 with 40

nums1[5] = 40
decrement last, so last = 4
decrement m, so m is now 3

you would then compare m -1 and n-1 again, so nums1[2] with nums2[1]
20 > 2, so overwrite nums1[last] with 20

should now have [10,20,20,40,20,40] (notice the last two spots are filled)
this continues until you get
[10,20,10,20,20,40], once m reaches 0. 
notice how the last 4 spots are properly sorted, and only 

the last part is to fill in the last two spots with the remaining elements in nums2

[10,2,10,20,20,40], so index 1 becomes 2
[1,2,10,20,20,40], index 0 becomes 1

O(N+M) Time
O(1) Space

*/

class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1, m, nums2, n) {
        let last = m + n - 1
        while (m > 0 && n > 0){
        	if (nums1[m-1] > nums2[n-1]){
        		nums1[last] = nums1[m-1]	
        		--m
        	}	
        	else {
        		nums1[last] = nums2[n-1]
        		--n
        	}
        	--last
        }
        while (n > 0){
        	nums1[last] = nums2[n-1]
        	--n
        	--last
        }
    }
}
