struct Solution;
impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        for i in 1..num/2+2 {
            if i*i == num {
                return true;
            } else if i*i > num {
                break;
            }
        }
        
        false
    }
}

fn main() {
    assert_eq!(Solution::is_perfect_square(16), true);
}
