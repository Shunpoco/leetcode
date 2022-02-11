struct Solution;
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut lo = 0 as i32;
        let mut hi = (n-1) as i32;
        
        while lo < hi {
            let mid = (lo+hi)/2;
            if nums[mid as usize] > nums[hi as usize] {
                lo = mid+1;
            } else {
                hi = mid;
            }
        }
        
        let rot = lo as usize;
        lo = 0;
        hi = (n-1) as i32;
        
        while lo <= hi {
            let mid = (lo+hi)/2;
            let real_mid = (mid as usize+rot)%n;
            
            if nums[real_mid] == target {
                return real_mid as i32;
            }
            
            if nums[real_mid] < target {
                lo = mid+1;
            } else {
                hi = mid-1;
            }
        }
        
        -1
    }
}

fn main() {
    assert_eq!(Solution::search(vec![4,5,6,7,0,1,2], 0), 4);
} 
