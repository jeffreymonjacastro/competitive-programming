class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;

        int l = 0;
        int r = x / 2;

        while (l <= r) {
            int m = l + (r - l)/2;

            if ((long)m * m > x) {
                r = m - 1;
            } else if ((long)m * m < x) {
                l = m + 1;
            } else {
                return m;
            }
        }

        return r;
    }
}
