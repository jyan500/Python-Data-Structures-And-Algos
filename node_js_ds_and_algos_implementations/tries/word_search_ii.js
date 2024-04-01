/*
https://www.youtube.com/watch?v=asbcE9mZz_U&t=1201s&ab_channel=NeetCode
Approach:
1) Use a trie, adding all words that we need to search for
2) Apply the word search algorithm from word search i, except
we check whether the current letter is in the trie. If so, we then pass
down the trie's children to the next recursive call

Optimization:
In order to pass Leetcode, you have to prune the trie
after you've found a word. See the youtube comments in
the neetcode video above for more information.

Time Complexity:
O((N * M * 4^s) + w*l), where N*M is the grid traversal, 4^s is each check on neighbors
for each node, and w*l is the time needed to construct the Trie
Space Complexity:
O(len(words) + O(N*M)), which is the grid + len of words
*/
var TrieNode = function(){
    this.children = {}
    this.endOfWord = false
    this.wordCount = 0
}

var Trie = function(){
    this.root = new TrieNode()   
}

Trie.prototype.insert = function(word){
    let cur = this.root
    for (let c of word){
        if (!(c in cur.children)){
            cur.children[c] = new TrieNode()
        }
        cur = cur.children[c]
        cur.wordCount++
    }
    cur.endOfWord = true
}

/* 
The purpose of prune word is to figure out whether any character
no longer represents a word in the trie, and remove that trie node from the 
trie

for example:

"oath", "oak"

if oath and oak are both in our trie,

o: {a: {k: {}}, t: h: {}}

at each level, it pushes the current trie node level and the character
onto a list

reverses the list, because we want to start removing the trie nodes
from the bottom (i.e starting from h, rather than from o) 

for example, h here no longer presents a word, since it has no children,
so the TrieNode h would get pruned.

t would also get pruned

however for "a", since we have the word "oak",
we can't prune "a", since "a" has another TrieNode of "k"

so the function would stop here

*/
Trie.prototype.pruneWord = function(word){
	let cur = this.root
	let nodeAndChildKey = []
	for (let c of word){
		nodeAndChildKey.push({cur: cur, char: c})
		cur = cur.children[c]
	}
	nodeAndChildKey.reverse()
	for (let nodeAndChild of nodeAndChildKey){
		let {cur, char} = nodeAndChild
		let targetNode = cur.children[char]
		if (Object.keys(targetNode.children).length === 0){
			delete cur.children[char]
		}
		else {
			return
		}
	}
}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
	let globalTrie = new Trie()
    for (let word of words){
        globalTrie.insert(word)
    }
    let cur = globalTrie
    let res = []
    let visited = new Set()
    
    var inBounds = function(i, j, board){
        return i >= 0 && i < board.length && j >= 0 && j < board[i].length
    }
    var search = function(i, j, trieNode, cur){
        let directions = [{x: 0, y: 1}, {x: 0, y: -1}, {x: -1, y: 0}, {x: 1, y: 0}]
        visited.add(`${i},${j}`)
        if (trieNode.endOfWord){
            res.push(cur)
            // setting endOfWord to false prevents us from adding the same word
            // twice (like "oa", "oaa" in one of the leetcode test cases)
            trieNode.endOfWord = false
            // find any nodes of the current word that don't have any children
            // and remove those nodes
            globalTrie.pruneWord(cur)

        }
        for (let d of directions){
            let {x, y} = d
            let newX = i + x
            let newY = j + y
            if (inBounds(newX, newY, board) && trie.wordCount !== 0 && !visited.has(`${newX},${newY}`) && board[newX][newY] in trie.children){
                search(newX, newY, trieNode.children[board[newX][newY]], cur + board[newX][newY])
            }
        }
        visited.delete(`${i},${j}`)
    }

    for (let i = 0; i < board.length; ++i){
        for (let j = 0; j < board[i].length; ++j){
            if (board[i][j] in cur.root.children){
                // pass in the next level of the trie, which is all
                // the children of the current letter
                search(i, j, cur.root.children[board[i][j]], board[i][j])

            }
        }
    }
    return res 
};