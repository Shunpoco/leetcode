struct Solution;

impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let l = nums.len();
        
        let mut counter = vec![0;21];
        for num in &nums {
            counter[(num+10) as usize] += 1;
        }
        
        let mut stack = vec![(vec![], counter)];
        let mut result = vec![];
                
        while stack.len() > 0 {
            let vs = stack.pop().unwrap();
            let now = vs.0;
            let cur_counter = vs.1;
            
            if now.len() == l {
                result.push(now);
                continue;
            }
            
            for i in 0..l {
                let num = nums[i];
                
                if (i == 0 || nums[i-1] != num) && cur_counter[(num+10) as usize] > 0 {
                    let mut t_now = now.clone();
                    t_now.push(num);
                    let mut t_cur_counter = cur_counter.clone();
                    t_cur_counter[(num+10) as usize] -= 1;
                    
                    stack.push((t_now, t_cur_counter));
                }
            }
            
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::permute_unique(vec![1,1,2]), vec![vec![2,1,1], vec![1,2,1], vec![1,1,2]]);
}
