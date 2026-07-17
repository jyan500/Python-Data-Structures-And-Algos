/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// Revisited 7/17/2026 with the same solution (updated time and space complexity)
// O(N*N!) time complexity, since N! is the number of permutations available, and we're doing O(N) work of slicing the arrays per recursive call
// O(N*N!) Space
var permute = function(nums) {
    let res = []
    var search = function(selection, cur){
        // if our selection space becomes 0, we don't have any more elements to choose,
        // so push our current array to res
        if (selection.length === 0){
            res.push(cur)
            return
        }
        // at each i, we want to pick selection[i], and then limit our selection space to be everything before i
        // and everything after i, so we pass in a smaller array into our next recursive call,
        // as well as the current array including selection[i]
        for (let i = 0; i < selection.length; ++i){
            search([...selection.slice(0, i), ...selection.slice(i+1, selection.length)], [...cur, selection[i]])
        }   
    }
    search([...nums], [])
    return res

};