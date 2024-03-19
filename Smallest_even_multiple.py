class Solution {
    public int smallestEvenMultiple(int n) {
        int k = n;
        while(k >= n){
            if (k % n ==0 && k % 2==0){
                return k;
            }
            k +=1;
        }
        return -1;
    }
}
// But my solution consumes large time and space due to the while loop since there is very simple way to solve the problem
