struct Solution;
impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        if nums.len() == 1 {
            return;
        }
        
        let mut max = nums.len()-1;
        let mut idx = nums.len()-1;
        let mut swap = false;
        
        while idx > 0 {
            idx -= 1;
            
            if nums[max] > nums[idx] {
                let v = &mut nums[idx+1..];
                v.sort();
                for i in idx+1..nums.len() {
                    if nums[i] > nums[idx] {
                        let temp = nums[i];
                        nums[i] = nums[idx];
                        nums[idx] = temp;
                        swap = true;
                        break;
                    }
                }            
                break;
            }
            
            if nums[max] < nums[idx] {
                max = idx;
            }
        }
        
        if !swap {
            nums.sort();
        }
    }
}

fn main() {
    let mut v = vec![1,3,2];
    Solution::next_permutation(&mut v);
    assert_eq!(v, vec![2,1,3]);
}
