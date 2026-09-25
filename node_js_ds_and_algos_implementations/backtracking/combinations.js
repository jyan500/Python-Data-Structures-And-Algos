class Solution {
    /**
     * @param {number} n
     * @param {number} k
     * @return {number[][]}
     */
    combine(n, k) {
        /* 
        Time Complexity: O(K * N!/(N-K)! * K!)
        Space: O(K * N!/(N-K)! * K!)

        The portion that involves the factorials represents the total amount of
        combinations that can be made given N and K
        
        keeping both the current index and current combination,
        we hold the current index and loop starting from that point,
        including each element into the current combination,
        until the current combination's length reaches the limit k
        */
        let res = []
        const search = (j, cur) => {
            if (cur.length === k){
               res.push(cur) 
               return
            }
            for (let i = j; i <= n; ++i){
                search(i+1, [...cur, i])
            }
        }
        search(1, [])
        return res
    }
}
