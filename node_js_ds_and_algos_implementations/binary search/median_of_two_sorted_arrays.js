/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    /*
    Neetcode O(Log(N+M)) solution:
    https://www.youtube.com/watch?v=q6IEA26hvXc&ab_channel=NeetCode
    
    median is the middle number
    A = [1,2,3,4]
    B = [1,2,3,4,5,6,7,8]
    
    total = 12
    half = 6
    
    l = 0
    r = len(A)-1 = 3

    i = (l + r)//2 = (3//2) = 1
    j = half - i - 2 = 6 - 1 - 2 = 3
    
    ALeft = A[i] = A[1] = 2
    ARight = A[i+1] = A[2] = 3
    
    BLeft = B[j] = B[3] = 4
    BRight = B[j+1] = B[4] = 5
    
    ALeft <= BRight (2 <= 5), true BLeft <= ARight (4 <= 3, FALSE)
    
    since ALeft < Bright, we need to do r = i + 1
    
    l = 1 + 1 = 2
    
    Next iteration
    i = 2 + 3 = 5//2 = 2
    j = half - i - 2 = 6 - 2 - 2 = 2
    
    ALeft = A[i] = A[2] = 3
    ARight = A[i+1] = A[3] = 4
    
    BLeft = B[j] = B[2] = 3
    BRight = B[j+1] = B[3] = 4
    
    ALeft <= BRight (3 <= 4) and BLeft <= ARight (3 <= 4, TRUE)
    
    12 % 2 == 0, so this is even
    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
    (4+3)/2 = 3.5
    
    as proof, the merged array:
    1 1 2 2 3 3 4 4 5 6 7 8
    
    (3+4)/2 = 3.5
    
    */
    const posInf = Number.POSITIVE_INFINITY
    const negInf = Number.NEGATIVE_INFINITY
    let A = nums1
    let B = nums2
    let total = nums1.length + nums2.length
    let half = Math.floor(total/2)
    // make sure A is always the shorter list by swapping the values
    if (B.length < A.length){
        let temp = A
        let temp2 = B
        B = temp
        A = temp2
    }
    let l = 0
    let r = A.length - 1
    while (true){
        i = Math.floor((r+l)/2)
        j = half - i - 2
        let ALeft = i >= 0 ? A[i] : negInf
        let ARight = i + 1 < A.length ? A[i+1] : posInf
        let BLeft = j >= 0 ? B[j] : negInf
        let BRight = j + 1 < B.length ? B[j+1] : posInf
        if (ALeft <= BRight && BLeft <= ARight){
            if (total % 2 !== 0){
                return Math.min(ARight, BRight)
            }
            return (Math.min(ARight, BRight) + Math.max(ALeft, BLeft)) / 2
        }
        else if (ALeft > BRight){
            r = i - 1
        }
        else {
            l = i + 1
        }
    }
};