struct Solution {}

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        if nums.len() == 0 {
            return 0i32;
        }
        let mut left = 0usize;        
        let mut right = nums.len();
        
        while left < right {
            let v = nums[left];
            if v == val {
                nums[left] = nums[right-1];
                nums[right-1] = v;
                right -= 1;
            } else {
                left += 1;
            }
        }
        
        right as i32     
    }
}

fn main() {
    let mut v = vec![0,2,2,2,2,2];
    let k = Solution::remove_element(&mut v, 2);
    println!("{}", k);
    println!("{:?}", v);
}

#[test]
fn test_remove_element() {
    assert_eq!(Solution::remove_element(&mut vec![0,2,2,2], 2), 1);
}
