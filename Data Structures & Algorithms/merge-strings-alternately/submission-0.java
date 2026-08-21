class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder x = new StringBuilder();
        int min = Math.min(word1.length(), word2.length());

        for (int i = 0; i < min; i++){
            x.append(word1.charAt(i));
            x.append(word2.charAt(i));
        }
        
        if (word1.length() > word2.length()){
            x.append(word1.substring(min));
            return x.toString();
        }
        x.append(word2.substring(min));
        return x.toString();
    }
}