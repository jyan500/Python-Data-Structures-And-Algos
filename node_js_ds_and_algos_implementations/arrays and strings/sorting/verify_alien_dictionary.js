class Solution {
    /**
     * @param {string[]} words
     * @param {string} order
     * @return {boolean}
     */
    isAlienSorted(words, order) {
        /*
        custom sorting
        create a dictionary mapping each character to an index
        when sorting the words dictionary, write a custom sorting 
        function based on the dictionary mapping 
        */
        const alienMap = {}
        for (let i = 0; i < order.length; ++i){
            alienMap[order[i]] = i
        }

        function alienSort(word1, word2){
            let i = 0
            let j = 0
            while (i < word1.length && j < word2.length){
                let order1 = alienMap[word1[i]]
                let order2 = alienMap[word2[j]]
                if (order1 === order2){
                    ++i
                    ++j
                }
                else if (order1 < order2){         
                    return -1
                }
                else {
                    return 1
                }

            }
            // if characters were the same up to this point,
            // pick the shorter word
            if (word1.length < word2.length){
                return -1
            }
            else if (word1.length > word2.length){
                return 1
            }
            return 0
        }
        let temp = [...words]
        temp.sort(alienSort)
        // check if the elements are the same after sorting
        for (let i = 0; i < temp.length; ++i){
            if (temp[i] !== words[i]){
                return false
            }
        }
        return true

    }
}
