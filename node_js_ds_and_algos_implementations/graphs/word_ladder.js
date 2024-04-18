/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
/* 
Approach:
https://www.youtube.com/watch?v=h9iTnkgv05E&ab_channel=NeetCode

1) Construct an adjacency list that's based on the "edit distance" between each word in the wordList. 
The method is that you use a "pattern", replacing each letter of word with an asterisk, as the "vertex"
of the adjacency list, and the edges are the words that fit this pattern.

for example:
[hit, hot, dot, dog, lot, log, cog]

hit -> h*t
       hi*
       *it
hot -> h*t
       ho*
       *ot
dot -> d*t
       do*
       *ot
lot -> ... 

You can see here that for dot and hot, they share the same pattern for *ot
so in the adjacency list,

*ot: [hot, dot]
h*t: [hit, hot]

2) After constructing the adjacency list, you can then apply a BFS, starting from the beginWord,
and then keeping track of the distance and the word as an object within the queue. Within the BFS,
you'd apply the same formula to figure out what all the patterns are for the word on the queue
(the string slicing + "*"), and then search for that pattern on the adjacency list to find the neighbor edges.

3) Track the global minimum distance, so once the current word that we popped === endWord, we update the minimum distance 
4) return global minimum distance if it's been updated

Time Complexity:
O(N^2 * M)
the maximum amount of edges is if every word is essentially connected to itself, so we might have to visit every
node within our BFS. Also, we need to iterate through the word of length m to find the pattern, so we can
search the pattern in our adjacency list

Space Complexity:
O(K-1*M), where K is the length of each word, there's K-1 different patterns for each word, and there's M words
*/
var ladderLength = function(beginWord, endWord, wordList) {
    if (!wordList.includes(endWord)){
        return 0
    }
    adjacency = {}
    wordList.push(beginWord)
    for (let word of wordList){
        for (let j = 0; j < word.length; ++j){
            pattern = word.slice(0, j) + "*" + word.slice(j+1, word.length)
            if (!(pattern in adjacency)){
                adjacency[pattern] = []
            }
            adjacency[pattern].push(word)
        }
    }
    let visited = new Set([beginWord])
    let q = [{"word": beginWord, "distance": 1}]
    let minDistance = Number.POSITIVE_INFINITY
    while (q.length > 0){
        let {word, distance} = q.shift()
        if (word === endWord){
            minDistance = Math.min(distance, minDistance)
        }
        for (let j = 0; j < word.length; ++j){
            pattern = word.slice(0, j) + "*" + word.slice(j+1, word.length) 
            for (neighbor of adjacency[pattern]){
                if (!visited.has(neighbor)){
                    visited.add(neighbor)
                    q.push({word: neighbor, distance: distance+1})
                }        
            }
        }
    }
    return minDistance !== Number.POSITIVE_INFINITY ? minDistance : 0
};