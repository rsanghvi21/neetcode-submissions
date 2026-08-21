class Solution {
    public String mergeAlternately(String word1, String word2) {
        String x = "";
        int min = Math.min(word1.length(), word2.length());
        boolean word1Larger = word1.length() > word2.length();

        for (int i = 0; i < min; i++){
            x += word1.substring(i, i + 1);
            x += word2.substring(i, i + 1);
        }

        if (word1Larger){
            return x += word1.substring(min);
        }

        return x += word2.substring(min);


        
    }
}