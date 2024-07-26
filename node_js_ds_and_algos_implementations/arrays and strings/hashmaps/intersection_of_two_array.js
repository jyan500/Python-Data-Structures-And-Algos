/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let n1 = new Set(nums1)
    let n2 = new Set(nums2)
    let res = []
    for (let element of n1){
        if (n2.has(element)){
            res.push(element)
        }
    }
    return res
};