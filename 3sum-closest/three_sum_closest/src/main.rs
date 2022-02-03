struct Solution;

impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums;
        nums.sort();
        
        let mut closest = 100000;
        
        let mut stack = vec![(vec![], 0)];
        
        while stack.len() > 0 {
            let v = stack.pop().unwrap();
            let vs = v.0;
            
            if vs.len() == 3 {
                let temp = vs[0]+vs[1]+vs[2];
                let mut v1 = target - temp;
                if v1 < 0 {
                    v1 *= -1;
                }
                let mut v2 = target - closest;
                if v2 < 0 {
                    v2 *= -1;
                }
                if v1 < v2 {
                    closest = temp;
                }
                continue;
            }
            
            let current = v.1;
            let ns = &nums[current..];
            
            for i in 0..ns.len() {
                if i == 0 || ns[i] != ns[i-1] {
                    let mut temp = vs.clone();
                    temp.push(ns[i]);
                    stack.push((temp, current+i+1));
                }
            }
        }
        
        closest        
    }
}


fn main() {
    assert_eq!(Solution::three_sum_closest(vec![0,0,0], 1), 0);
}
