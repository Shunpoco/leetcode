use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut hash:HashMap<i32, usize> = HashMap::new();
        
        for (i, &nums) in nums2.iter().enumerate() {
            hash.insert(nums, i);
        }
        
        let mut ans = vec![];
        
        for &num in nums1.iter() {
            let idx = hash.get(&num).unwrap();
            
            let mut v = -1;
            for n in &nums2[*idx..] {
                if *n > num {
                    v = *n;
                    break;
                }
            }
            
            ans.push(v);
        }
        
        ans
    }
}

fn main() {
    assert_eq!(Solution::next_greater_element(vec![4,1,2], vec![1,3,4,2]), vec![-1,3,-1]);
}
