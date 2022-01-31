struct Solution;

impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut candidates = candidates;
        candidates.sort();
        let mut stack = vec![(vec![], 0, target)];
        let mut result = vec![];
        
        while stack.len() > 0 {
            let v = stack.pop().unwrap();
            let current = v.0;
            let level = v.1;
            let current_target = v.2;
            
            let current_candidates = &candidates[level..];
            for i in 0..current_candidates.len() {
                let num = current_candidates[i];
                if i == 0 || num != current_candidates[i-1] {
                    if current_target - num == 0 {
                        let mut val = current.clone();
                        val.push(num);
                        result.push(val);
                    } else if current_target - num > 0 {
                        let mut val = current.clone();
                        val.push(num);
                        stack.push((val, level+i+1, current_target-num));
                    }                    
                }
            }
        }
        
        return result
    }
}


fn main() {
    assert_eq!(Solution::combination_sum2(vec![10,1,2,7,6,1,5], 8), vec![vec![2,6], vec![1,7], vec![1,2,5], vec![1,1,6]]);
}
