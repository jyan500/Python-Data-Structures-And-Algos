class Solution {
    public int findMin(int[] nums) {
        int peakIndex = this.findPeakIndex(0, nums.length-1, nums);
        return nums[peakIndex];
    }
    public int findPeakIndex(int left, int right, int[] nums){
        /*
        in rotated sorted array, there's an index where the element on the left
        is greater instead of less than, which is different from a normal sorted array. 
        Using Binary Search:
        If the left most element is greater,
        that means the rotation point would be on the right side
        If the right most element is less, 
        that means the rotation point would be on the right
        However, if the left most element i

        if left >= right, that means we've exhausted all the possible search options,
        so return mid
        */
        int mid = (left + (right - left)/2);
        if (left >= right){
            return mid;
        }
        // if the right most element is less, this isn't normal for a sorted array,
        // so we'd want to search the right side to find the rotation point
        if (nums[right] < nums[mid]){
            return this.findPeakIndex(mid+1, right, nums);   
        }
        else {
            return this.findPeakIndex(left, mid, nums);
        }
    }
}
