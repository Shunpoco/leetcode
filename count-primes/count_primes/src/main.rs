struct Solution;
impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        let n = n as usize;
        if n <= 1 {
            return 0;
        }
        
        let mut nums = vec![true;n];
        nums[0] = false;
        nums[1] = false;
        
        let mut result = vec![];
        let mut idx = 2;
        while idx*idx < n {
            if nums[idx] {
                result.push(idx);
                let mut v = 1;
                while idx*v < n {
                    nums[idx*v] = false;
                    v += 1;
                }
            }
            idx += 1;
        }
        
        for (i, &v) in nums.iter().enumerate() {
            if v {
                result.push(i);
            }
        }
        
        result.len() as i32
    }
}

fn main() {
    assert_eq!(Solution::count_primes(10), 4);
}
