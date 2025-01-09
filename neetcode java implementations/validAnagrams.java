class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> counter1 = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); ++i){
            if (counter1.get(s.charAt(i)) != null) {
                counter1.put(s.charAt(i), counter1.get(s.charAt(i)) + 1);
            }
            else {
                counter1.put(s.charAt(i), 1);
            }
        }
        for (int i = 0; i < t.length(); ++i){
            if (counter1.get(t.charAt(i)) != null){
                counter1.put(t.charAt(i), counter1.get(t.charAt(i)) - 1);
            }
            else {
                return false;
            }
        }
        for (int value: counter1.values()){
            if (value != 0){
                return false;
            }
        }
        return true;

    }
}
