struct Solution {}

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut result = vec![];
        
        let l = nums.len();
        
        let mut t = vec![];
        
        for i in 0..l {
            let v = nums[i];
            if i != 0 && v != nums[i-1]+1 {
                if t.len() == 1 {
                    result.push(format!("{}", t[0]));
                } else {
                    result.push(format!("{}->{}", t[0], t[t.len()-1]));
                }
                t.clear();
            }
            t.push(v);
        }
        
        if t.len() == 1 {
            result.push(format!("{}", t[0]));
        } else if t.len() > 1 {
            result.push(format!("{}->{}", t[0], t[t.len()-1]));
        }
        
        result
    }
}

fn main() {
    assert_eq!(Solution::summary_ranges(vec![0,1,2,4,5,7]), vec!["0->2".to_string(), "4->5".to_string(), "7".to_string()]);
}
