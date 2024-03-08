/*
O(N) Approach
1) Use the same algorithm as construct binary tree from preorder and inorder traversal, except:
	a) Because the tree can have multiple nodes with the same value,
	we need to change the TreeNode definition to allow for a unique ID in order to differentiate these nodes.
	b) When doing the preorder traversal, use Math.random() as a unique ID (uuid() would be a better choice if possible)
		- keep generating a new random number until it doesn't appear in our random set
		- when inserting into the preorder/inorder traversals, push an object containing both the value and ID
	c) Keep the list of the inorder traversals, but this time using the ID that was set during the preorder traversal
	d) Put both the preorder and inorder traversals into an object and JSON stringify it

	When de-serializing,
	a) call JSON parse on the input string to deserialize back into the object
	b) perform the same algorithm as construct binary tree from preorder and inorder traversal,
	except you need to use findIndex() since we're looking for an object, and check for matching ID's
	this time instead of matching values 

*/
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
function TreeNode(val){
    this.id = null
    this.val = val
    this.left = this.right = null
}

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    let preorder = []
    let inorder = []
    let randomIds = new Set()
    var preSearch = function(root){
        if (root){
            let randId = Math.random()
            while (randomIds.has(randId)){
                randId = Math.random()
            }
            root.id = randId
            preorder.push({id: root.id, val: root.val})
            preSearch(root.left)
            preSearch(root.right)
        }
    }
    var inSearch = function(root){
        if (root){
            inSearch(root.left)
            inorder.push({id: root.id, val: root.val})
            inSearch(root.right)
        }
    }
    preSearch(root)
    inSearch(root)
    return JSON.stringify({"preorder": preorder, "inorder": inorder})
};


/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    var construct = function(preorder, inorder){
        if (preorder.length > 0){
            let root = preorder[0]
            let rootIndex = inorder.findIndex((obj) => obj.id === root.id)
            // left subtree is everything to the left of the root
            let leftSub = inorder.slice(0, rootIndex)
            // right subtree is everything to the right of the root
            let rightSub = inorder.slice(rootIndex+1, inorder.length)
            // the left subtree in the preorder list is determined by 
            // getting the length of the "leftSub" variable    
            let preLeftSub = preorder.slice(1, 1+leftSub.length)
            // the right subtree in the preorder list is determined by
            // the range of 1 after the leftSub.length (plus an additional one) to the end
            // of the preorder list
            let preRightSub = preorder.slice(leftSub.length+1, preorder.length)
            let left = construct(preLeftSub, leftSub)
            let right = construct(preRightSub, rightSub)
            let newRoot = new TreeNode(root.val)
            newRoot.left = left
            newRoot.right = right
            return newRoot
        }   
        return null
    }
    let obj = JSON.parse(data)
    let root = null
    if (obj.preorder && obj.preorder.length > 0 && obj.inorder && obj.inorder.length > 0){
        root = construct(obj.preorder, obj.inorder)
    }
    return root
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */