import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (Character c: s.toCharArray()){
            if (stack.size() > 0){
                if (
                    (stack.peek() == '(' && c == ')') || 
                    (stack.peek() == '[' && c == ']') ||
                    (stack.peek() == '{' && c == '}')
                ){
                        stack.pop();
                        continue;
                    }
            }
            stack.push(c);
        }
        return stack.size() == 0;
    }
}