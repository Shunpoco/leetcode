use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn is_possible(target: Vec<i32>) -> bool {
        let mut sum = target.iter().sum::<i32>();
        
        let mut bp = BinaryHeap::new();
        for &num in target.iter() {
            bp.push(num);
        }
        
        while *bp.peek().unwrap() != 1 {
            let mut num = bp.pop().unwrap();
            sum -= num;
            if num <= sum || sum < 1 {
                return false;
            }
            num %= sum;
            sum += num;
            if num > 0 {
                bp.push(num);
            } else {
                bp.push(sum);
            }
        }        
        
        true
    }
}

fn main() {
    assert_eq!(Solution::is_possible(vec![9,3,5]), true);
}
