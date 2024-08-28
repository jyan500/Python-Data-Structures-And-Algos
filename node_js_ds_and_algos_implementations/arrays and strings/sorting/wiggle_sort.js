var wiggleSort = function(nums){
	/*
        https://youtu.be/vGsyTE4s34w
        Note, there's a way to do this in O(N) Time which is the most optimized,
        see the neetcode link above.
        
        O(NLogN) Time
        O(1) Space
        sort the array in place first
        swap elements in pairs, starting on index i = 1
        until the last element nums.length - 1

        i.e
        1 2 3 4 5 6
        swaps index i = 1 and i = 2
        jumps to the following pair at i = 3
        1 3 2 4 5 6
        swaps i = 3 and i = 4
        1 3 2 5 4 6
        this is actually a valid answer because
        nums[0] <= nums[1] >= nums[2] <= nums[3] , etc
    */ 
	nums.sort((a,b) => {
		if (a > b){
			return 1
		}
		else if (a < b){
			return -1
		}
		return 0
	})
	let i = 1
	while (i < nums.length - 1){
		// save the value of nums[i] and nums[i+1]
		let temp = nums[i]
		let temp2 = nums[i+1]
		// set the values of nums[i] equal to the original value of nums[i+1]
		// and nums[i+1] equal to the original value of nums[i]
		nums[i] = temp2
		nums[i+1] = temp
		i+=2
	}
}