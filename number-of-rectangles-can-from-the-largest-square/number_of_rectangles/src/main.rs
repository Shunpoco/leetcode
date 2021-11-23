struct Solution {}

impl Solution {
    pub fn count_good_rectangles(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut result = 0i32;
        
        let mut maxlen = 0i32;
        
        for rec in rectangles {
            let m = Solution::min(rec[0], rec[1]);
            if m > maxlen {
                result = 1;
                maxlen = m;
            } else if m == maxlen {
                result += 1;
            }
        }
        
        result
    }

    fn min(a: i32, b: i32) -> i32 {
        if a > b {
            return b;
        }
        
        a
    }
}

fn main() {
    assert_eq!(Solution::count_good_rectangles(vec![vec![5,8], vec![3,9], vec![5,12], vec![16,5]]), 3);
}
