/* 
Note these are function prototypes which act as classes
When creating "methods", you can do <Name>.prototype.<Name of Method> = () => {
	
}

And you also have access to the "this" variables that you defined in the declaration
of your function prototype

The idea of a trie is an object where the key is the character,
and the value is a TrieNode, that contains another object which contains more keys, 
and more TrieNodes as values, as well as an "endOfWord" boolean that indicates
whether this is the end of a word

For example in "apple", each obj here is a trienode
		< children: {"a": <>} endOfWord: false>
	<children: {"p": <>} endOfWord: false>
	<children: {"p": <>} endOfWord: false>
	<children: {"l": <>} endOfWord: false>
	<children: {"e": <>} endOfWord: true>

Now if we wanted to insert "apples",
we'd notice that "a" is already in our root node, so we go down the children of "a",
which would be "p", we'd get all the way down to e (since it's the same word except with the
additional letter "s"), and then we'd see that there's no child with value "s", so we'd insert it.
And since there's no more characters after s, we'd also set "endOfWord" to be true.

<children: {"s": <>, endOfWord: true}

When searching, we can follow a similar process, checking to see if each character in the word 
is in our TrieNode. If so, we continue down that path, otherwise it's not present if the character
is not found. If we found all the characters, but the last character has "endOfWord" set to false,
this is not considered found. Although for the prefix search "startsWith", this would be considered
to be found as it's a prefix and not the whole word.

Time Complexity: O(N), it should be relatively fast to find a specific word, since each lookup per letter
of the word is O(1), done N times
Space Complexity: O(N), holding N levels on the Trie depending on the amount of the characters

*/ 
var TrieNode = function() {
    this.children = {}
    this.endOfWord = false
}

var Trie = function() {
    this.trieNode = new TrieNode()
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    /*
    {"a": {"p": {}, "d": {}} } ...
    */
    let root = this.trieNode
    for (let c of word){
        if (c in root.children){
            root = root.children[c]
        }
        else {
            root.children[c] = new TrieNode()
            root = root.children[c]
        }
    }
    root.endOfWord = true
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let root = this.trieNode
    for (let c of word){
        if (c in root.children){
            root = root.children[c]
        }
        else {
            return false
        }
    }
    return root.endOfWord
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let root = this.trieNode
    for (let c of prefix){
        if (c in root.children){
            root = root.children[c]
        }
        else {
            return false
        }
    }
    return true
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */