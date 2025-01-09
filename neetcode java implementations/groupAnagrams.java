class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> anagrams = new HashMap<String, ArrayList<String>>();
        List<List<String>> res = new ArrayList<List<String>>();
        for (int i = 0; i < strs.length; ++i){
            String s = strs[i];
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);
            ArrayList<String> inner;
            if (anagrams.get(sortedString) != null){
                inner = anagrams.get(sortedString);         
            }
            else {
                inner = new ArrayList<String>();
            }
            inner.add(strs[i]);
            anagrams.put(sortedString, inner);
        }
        for (List<String> inner : anagrams.values()){
            res.add(inner);
        }
        return res;
    }
}
