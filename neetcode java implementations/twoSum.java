class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; ++i){
            int other = target - nums[i];
            if (map.get(other) != null){
                int index = map.get(other);
                if (index < i){
                    result[0] = index;
                    result[1] = i;
                }
                else {
                    result[0] = i;
                    result[1] = index;
                }
                return result;
            }
            else {
                map.put(nums[i], i);
            }
        }
        return result;
    }
}
