/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var interchangeableRectangles = function(rectangles) {
    /*
        1) store the frequency of each width/height ratio in hashmap
        2) the pattern is, given n amount of rectangles with the same ratio,
        the amount of unique pairs is the sum of consecutive numbers up to n
        2 = 1 pair (1)
        3 = 3 pairs (2 + 1)
        4 = 6 pairs (3 + 2 + 1)
        5 = 10 pairs (4 + 3 + 2 + 1)
        
        the way to calculate the sum of consecutive numbers is 
        (n * (n-1))/2

        Time: O(N)
        Space: O(N)
    */
    let ratios = {}
    for (let [width, height] of rectangles){
        let ratio = width/height
        if (ratio in ratios){
            ratios[ratio]++
        }
        else {
            ratios[ratio] = 1
        }
    }
    let pairs = 0
    for (let ratio in ratios){
        let freq = ratios[ratio]
        if (freq >= 2){
            let numUnique = (freq * (freq - 1))/2
            pairs += numUnique
        }
    }
    return pairs
};