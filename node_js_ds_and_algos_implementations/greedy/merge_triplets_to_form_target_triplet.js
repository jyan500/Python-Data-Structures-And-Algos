/**
 * @param {number[][]} triplets
 * @param {number[]} target
 * @return {boolean}
 */
var mergeTriplets = function(triplets, target) {
    /*
    Brute Force
    Time: O(N)
    Space: O(1)
    1) filter the triplets such that each number a, b, c is <= x, y, z of the target. This way,
    we ensure that doing the max() operation while merging triplets will not create an invalid triplet.
    2) store the first triplet in a variable "choices", and then for each remaining triplet,
    take the max between choices[0], choices[1], choices[2], and the triplet that we're looking at.
    3) After looping through, if each value of the choices triplet === target triplet, this means it is possible
    to merge the triplets to create the target.
    */
    let [x,y,z] = target
    let validChoices = triplets.filter((triplet) => {
        let [a,b,c] = triplet
        return (a <= x && b <= y && c <= z)
    })
    if (validChoices.length === 0){
        return false
    }
    let choices = validChoices[0]
    for (let i = 0; i < validChoices.length; ++i){
        let [a,b,c] = validChoices[i]
        choices[0] = Math.max(choices[0], a)
        choices[1] = Math.max(choices[1], b)
        choices[2] = Math.max(choices[2], c)
    }
    return choices[0] === x && choices[1] === y && choices[2] === z
    
};