class Solution {
    public boolean isAnagram(String s, String t) {
        char[] string=s.toCharArray();
        Arrays.sort(string);
        String str1=new String(string);
        string=t.toCharArray();
        Arrays.sort(string);
        String str2=new String(string);
        return str1.equals(str2);

    }
}