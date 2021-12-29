struct Solution {}

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut result = 0i32;
        let mut left = 0usize;
        let mut right = height.len()-1;
        
        while left < right {
            let hl = height[left];
            let hr = height[right];
            
            let h: i32;
            if hl < hr {
                h = hl;
            } else {
                h = hr;
            }
            
            let w = (right - left) as i32;
            
            let area = w * h;
            
            if area > result {
                result = area;
            }
            
            if hl < hr {
                left += 1;
            } else {
                right -= 1;
            }
        }        
        result
    }
}


fn main() {
    assert_eq!(Solution::max_area(vec![1,8,6,2,5,4,8,3,7]), 49);
}
