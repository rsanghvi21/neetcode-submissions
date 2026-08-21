class Solution {
    public String longestCommonPrefix(String[] strs) {
        int index = 0;
        String x = "";
        int i = 0;
        int min = strs[0].length();

        for (String s : strs){
            if (s.length() < min){
                min = s.length();
            }
        }

        while(i < min){
            for (int j = 0; j < strs.length; j++){
                char c = strs[0].charAt(index);
                if (c != strs[j].charAt(index)){
                    return x;
                }
                if (j == strs.length - 1){
                    x += c;
                    index++;
                }
            }
            i++;
        }
        return x;
    }
}