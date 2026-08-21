class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }
        
        Map<String, Integer> sMap = new HashMap<>();
        Map<String, Integer> tMap = new HashMap<>();


        for (int i = 0; i < s.length(); i++){
            String sChar = s.substring(i, i + 1);
            if (sMap.containsKey(sChar)){
                int val = sMap.get(sChar);
                val++;
                sMap.put(sChar, val);
            }
            else{
                sMap.put(sChar, 1);
            }

            String tChar = t.substring(i, i + 1);
            if (tMap.containsKey(tChar)){
                int val = tMap.get(tChar);
                val++;
                tMap.put(tChar, val);
            }
            else{
                tMap.put(tChar, 1);
            }          
        }

        return sMap.equals(tMap);


    }
}
