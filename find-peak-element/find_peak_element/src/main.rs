struct Solution;
impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        Self.search(&nums, 0, nums.len()-1)
    }
    
    fn search(self, nums: &Vec<i32>, l: usize, r: usize) -> i32 {
        if l == r {
            return l as i32;
        }
        
        let mid = (l+r)/2;
        
        if nums[mid] > nums[mid+1] {
            return Self.search(nums, l, mid);
        }
        Self.search(nums, mid+1, r)
    }
}


fn main() {
    assert_eq!(Solution::find_peak_element(vec![1,2,1,3,5,4]), 4);
}
