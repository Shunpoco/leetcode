struct Solution {}

impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let mut result = 0i32;
        
        let l = arr.len();
        for i in 0..l {
            let mut j = (i+1) as usize;
            while j <= l {
                result += arr[i..j].iter().sum::<i32>();
                
                j += 2;
            } 
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::sum_odd_length_subarrays(vec![1,4,2,5,3]), 58);
}
