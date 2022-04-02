struct Solution;
impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_by(|a, b| b.cmp(a));
        
        nums[(k-1) as usize]
    }
}

fn main() {
    assert_eq!(Solution::find_kth_largest(vec![1,2,3,4], 2), 3);
}
