/*
if theres no wildcard, then it's an O(N) search, where N is the length of the word,
 since it relies on hashmap for O(1) operations
If theres wildcard, we factor in an additional O(N*26^k), where k is the amount of wildcard characters

Space complexity is O(N), N is the amount of words in the word dictionary
*/

/*
Example Execution:

root = TrieNode(endOfWord = false, children = {})

adding "dad"

    d
  a
 d
 
the last d is the end of word

adding "bad"

    b      d 
  a      a 
d     d

searching for ".ad"

In this algorithm, whenever we see ".", we push all the different 
children at this level to a stack. We continue to pop until we visit all 
possibilities

note the full tree is 
b: {a: {d: endOfWord}}, d: {a: {d: endOfWord}}

stack = [{root: {b: {a: {d: endOfWord}}, d: {a: {d: endOfWord}}}, word: ".ad"}]

while (stack...)
pops out stack, node = {b: {a: {d: endOfWord}}, d: {a: {d: endOfWord}}}, word = ".ad"
word[0] === ".", takes all children in root, appends child node
and word[1: ] to the stack

stack = [{root: {b: {a: {d: endOfWord}}}, word: "ad"}, {root: {d: {a: {d: endOfWord}}}, word:"ad"}]

next iteration
pops out stack, node = {b: {a: {d: endOfWord}}}, word = "ad"

word[0], a is in the children of b, so
add children of a to the stack

stack = [{root: {d: {a: {d: endOfWord}}}, word: "ad"}, {root: {a: {d: endOfWord}}, word: "d"}]

next iteration
pops out stack, node = {d: {a: {d: endOfWord}}}, word = "ad"

word[0], a is in the children of d, so
add children of a to the stack

stack = [{root: {root: {a: {d: endOfWord}}, word: "d"}, {root: {a: {d: endOfWord}}, word: "d"}]

next iteration
pops out stack, node = {a: {d: endOfWord}} word = "d"

word[0], d is in the children of a,
so add children of a to the stack

stack = [ {root: {a: {d: endOfWord}}, word: "d"}, {root: {d: endOfWord}, word: ""}]

next iteration
pops out stack, node = {a: {d: endOfWord}} word = "d"

word[0], "d" is in the children of a,
add children of a to the stack

stack = [{root: {d: endOfWord}, word: ""}, {root: {d: endOfWord}, word: ""}]

next iteration
pops out stack, note that word is "", so
we check if the current node {d: endOfWord} is the endOfWord,
which is true

in this case, we break out the loop and return true


*/
var TrieNode = function(){
    this.children = {}
    this.endOfWord = false
}

var WordDictionary = function() {
    this.root = new TrieNode()    
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    let cur = this.root
    for (let c of word){
        if (!(c in cur.children)){
            cur.children[c] = new TrieNode()
        }
        cur = cur.children[c]
    }
    cur.endOfWord = true
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    let stack = [{root: this.root, value: word}]
    let n = word.length
    while (stack.length){
        let {root: node, value: word} = stack.pop()
        if (!word){
            if (node.endOfWord){
                return true
            }
        }
        else if (word[0] === "."){
           for (let childNode of Object.values(node.children)){
               stack.push({root: childNode, value: word.slice(1, n)})
           } 
        }
        else if (word[0] in node.children){
            let next = node.children[word[0]]
            stack.push({root: next, value: word.slice(1, n)})
        }
    }
    return false
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */