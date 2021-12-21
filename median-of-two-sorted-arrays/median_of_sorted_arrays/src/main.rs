struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let l1 = nums1.len();
        let l2 = nums2.len();
        let ls = l1 + l2;
        let mut v = vec![0i32; ls];
        let mut i = 0usize;
        let mut i1 = 0usize;
        let mut i2 = 0usize;
        
        while i1 < l1 && i2 < l2 {
            if nums1[i1] < nums2[i2] {
                v[i] = nums1[i1];
                i1 += 1;
            } else {
                v[i] = nums2[i2];
                i2 += 1;
            }
            i += 1;
        }
        
        while i1 < l1 {
            v[i] = nums1[i1];
            i1 += 1;
            i += 1;
        }
        
        while i2 < l2 {
            v[i] = nums2[i2];
            i2 += 1;
            i += 1;
        }
        
        if ls % 2 == 0 {
            return (v[ls/2-1] + v[ls/2]) as f64 / 2.;
        }
        
        
        v[ls/2] as f64
    }
}


fn main() {
    assert_eq!(Solution::find_median_sorted_arrays(vec![1,2], vec![3,4]), 2.5);
}
