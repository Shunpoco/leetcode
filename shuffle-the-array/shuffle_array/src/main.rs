struct Solution {}

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let n = n as usize;
        if nums.len() != 2*n {
            return vec![];
        }
        let n1 = &nums[..n];
        let n2 = &nums[n..];
        
        let mut result = vec![];
        
        for (v1, v2) in n1.iter().zip(n2.iter()) {
            result.push(*v1);
            result.push(*v2);
        }
        
        result
    }
}

fn main() {
    println!("{:?}", Solution::shuffle(vec![1,2,3,1,2,3], 3));
}
 