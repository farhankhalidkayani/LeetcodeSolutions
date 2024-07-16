class Solution {
    public int largestAltitude(int[] gain) {
        ArrayList<Integer> res=new ArrayList<>();
        res.add(0);
        int total=0;
        for(int i=0;i<gain.length;i++){
            total+=gain[i];
            res.add(total);
        }
        return Collections.max(res);
    }
}