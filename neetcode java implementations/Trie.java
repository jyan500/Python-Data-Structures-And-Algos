class TrieNode {
    public Map<Character, TrieNode> children;
    public boolean endOfWord;
    TrieNode(){
        this.children = new HashMap<>();
        this.endOfWord = false;
    }
}
class PrefixTree {
    TrieNode root;
    public PrefixTree() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = this.root;
        for (Character c: word.toCharArray()){
            if (cur.children.get(c) == null){
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
        }
        cur.endOfWord = true;
    }

    public boolean search(String word) {
        TrieNode cur = this.root;
        for (Character c: word.toCharArray()){
            if (cur.children.get(c) == null){
                return false;
            }
            cur = cur.children.get(c);
        }
        return cur.endOfWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode cur = this.root;
        for (Character c: prefix.toCharArray()){
            if (cur.children.get(c) == null){
                return false;
            }
            cur = cur.children.get(c);
        }
        return true;
    }
}
