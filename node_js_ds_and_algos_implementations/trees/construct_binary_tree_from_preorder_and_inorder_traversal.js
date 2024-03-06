/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    /*
        inorder tells you the left and right subtrees
        preorder tells you the order of the roots
        so preorder[0] is the root of the tree
        when we search for preorder[0] in the inorder list,
        we see that 9 and (15, 20, 7) are the left and right subtrees
        
        to determine how much we need to slice from preorder list,
        we have to take the length of the slices for the left and right subtrees from the inorder list
        
        for the left subtree, in preorder list, we need to slice
        from anything past the root (index 1), to 1 + length of the left slice
        for the right subtree, in preorder list, we need to lsice
        from anything past the left preorder slice (1 + length of the left slice), to the end of the preorder list
        
        
    */
    if (preorder.length > 0){
        let root = preorder[0]
        let rootIndex = inorder.indexOf(preorder[0])
        let leftSub = inorder.slice(0, rootIndex)
        let rightSub = inorder.slice(rootIndex+1, inorder.length)
        let preorderLeftSlice = preorder.slice(1, 1+leftSub.length)
        let preorderRightSlice = preorder.slice(1+leftSub.length, preorder.length)
        let left = buildTree(preorderLeftSlice, leftSub)
        let right = buildTree(preorderRightSlice, rightSub)
        return new TreeNode(root,left,right)
    }
};