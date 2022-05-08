struct Solution;
impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut memory = vec![0;1001];
        
        for num in &nums {
            for &n in num {
                memory[n as usize] += 1;
            }
        }
        
        let mut result = vec![];
        let l = nums.len();
        for (i, &m) in memory.iter().enumerate() {
            if m == l {
                result.push(i as i32);
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::intersection(vec![vec![1,2,3], vec![4,5,6]]), vec![]);
}
