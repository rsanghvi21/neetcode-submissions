class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0;
        int j = 0;
        String temp = "";

        while (i < s.length() && j < t.length()){
            char s1 = s.charAt(i);
            char t1 = t.charAt(j);
            if (s1 == t1){
                temp += s1;
                i++;
            }
            j++;
        }
        return s.equals(temp);
    }
}