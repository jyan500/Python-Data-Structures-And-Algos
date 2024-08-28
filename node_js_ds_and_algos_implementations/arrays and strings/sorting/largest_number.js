/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    /*
    the idea is that you write a custom sorting function that compares to numbers based on
    whether the ordering would result in a bigger number
    
    for example when sorting 3 and 30
    in the comparator a = 3 and b = 30
    you would check if a + b > b + a or vice versa
    i.e 330 > 303 ?
    
    if yes, then return 1
    if no, return -1
    if the same, return 0
    
    eventually, the number that creates the "biggest" number would end up in the back,
    or you can reverse the orderings (i.e if a > b, return -1) to end up with reverse sort
    
    there's also an edge case where if every number is a 0, we should just return 0
    */
    
    if (nums.every((x) => x === 0)){
        return "0"
    }
    
    let sortKey = function(a, b) {
        let resA = parseInt(a.toString() + b.toString())
        let resB = parseInt(b.toString() + a.toString())
        if (resA > resB){
            return -1
        }
        else if (resA < resB){
            return 1
        }
        return 0
    }
    nums.sort(sortKey)
    let res = nums.reduce((acc, num) => {
        return acc + num.toString()
    }, "")
    return res
    
};