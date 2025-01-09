/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null){
            List<List<Integer>> empty = new ArrayList<>();
            return empty;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> res = new ArrayList<>();
        while (!q.isEmpty()){
            int N = q.size();
            List<Integer> level = new ArrayList<Integer>();
            for (int i = 0; i < N; ++i){
                TreeNode node = q.poll();
                if (node != null){
                    if (node.left != null){
                        q.add(node.left);
                    }
                    if (node.right != null){
                        q.add(node.right);
                    }
                    level.add(node.val);
                }
            }
            res.add(level);
        }
        return res;
    }
}
