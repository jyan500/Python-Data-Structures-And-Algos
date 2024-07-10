class Solution {
    /**
     * @param {string[]} words
     * @returns {string}
     */
    foreignDictionary(words) {
        /*
        1) create adjacency list, keys are all characters in the words,
        and values are the characters that come after this particular key
        in the ordering
        2) Apply Topological sort, which is DFS with a visit dict, where
        we mark visit(char) as true and then false after that path has been visited 
        (similar to course schedule II). Remember to also keep a stack which stores the current letter
        after the path has been visited

        The bottleneck is the creation of the adjacency list, which is O(N*M), where M is the length
        of each word in the list, and N is the amount of words in the list. The topological sort
        should be the same time complexity as DFS, O(E + V)
        */
        let adjacency = {}
        // get the chars of each word as keys in hashmap
        for (let w of words){
            for (let c of w){
                adjacency[c] = new Set()
            }
        }
        for (let i = 0; i < words.length - 1; ++i){
            let w1 = words[i]
            let w2 = words[i+1]
            /* 
            first, if two words have the same prefix, but the length of the first word
            is bigger than the second,
            this is not a valid comparison to make since 
            a longer word cannot come before a shorter word in lexicographical ordering

            i.e [abcd, abc], the min length is 3, so looking at the prefix "abc",
            abcd is not less than abc, so this is an invalid ordering
            */
            let minLength = Math.min(w1.length, w2.length)
            if (w1.length > w2.length && w1.slice(0, minLength) === w2.slice(0, minLength)){
                return ""
            }

            /* compare the current word and next word,
            and try to match all chars until the 
            first differing character.

            abf
            abg

            for example, f and g are the first differing chars, which means
            that f comes before g in this specific ordering.
            */
            for (let j = 0; j < minLength; ++j){
                if (w1[j] !== w2[j]){
                    adjacency[w1[j]].add(w2[j])
                    break
                }
            }

        }
        let res = []
        let visited = {}
        /* 
        topological sort also checks for cycle detection,
        so if the function returns true, there's a cycle, which means
        there's no valid ordering
        */
        var dfs = function(c){
            if (c in visited){
                return visited[c]
            }
            // setting visited[c] to true means it's on the current path
            visited[c] = true
            for (let neighbor of adjacency[c]){
                if (dfs(neighbor)){
                    return true
                }
            }
            // setting visited[c] tp false means it's been visited, but not on the current path
            visited[c] = false   
            res.push(c)
        }
        for (let c of Object.keys(adjacency)){
            if (dfs(c)){
                return ""
            }
        }
        return res.reverse().join("")
    }
}
