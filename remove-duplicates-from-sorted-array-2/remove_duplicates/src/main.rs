struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut current = nums[0];
        let mut count= 0usize;
        let mut result = nums.len();
        
        for i in 0..nums.len() {
            if nums[i] != current {
                for j in 1..count-1 {
                    nums[i-j] = -10001;
                    result -= 1;
                }
                current = nums[i];
                count = 1;
            } else {
                count += 1;
            }
        }
        if count > 2 {
            for i in 1..count-1 {
                let l = nums.len();
                nums[l-i] = -10001;
                result -= 1;
            }
        }
                
        for i in 0..nums.len() {
            if nums[i] == -10001 {
                for j in i+1..nums.len() {
                    if nums[j] != -10001 {
                        let temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                        break;
                    }
                    if j == nums.len()-1 {
                        return result as i32;
                    }
                }
            }
        }
        
        result as i32
    }
}


fn main() {
    let mut v = vec![1,1,1,2,2,3];
    let r = Solution::remove_duplicates(&mut v);

    assert_eq!(&v[..r as usize], &[1,1,2,2,3])
}
