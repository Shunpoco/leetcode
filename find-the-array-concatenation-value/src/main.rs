struct Solution;
impl Solution {
    pub fn find_the_array_conc_val(nums: Vec<i32>) -> i64 {
        let mut result: i64 = 0;

        let mut l = 0 as i32;
        let mut r = (nums.len() - 1) as i32;

        while l <= r {
            if l == r {
                result += nums[l as usize] as i64;
            } else {
                let lv = nums[l as usize] as i64;
                let rv = nums[r as usize] as i64;

                let mut digits = 1;
                while digits <= rv {
                    digits *= 10;
                }

                result += lv * digits + rv;
            }

            l += 1;
            r -= 1;
        }

        result
    }
}

fn main() {
    let nums = vec![1];
    
    let got = Solution::find_the_array_conc_val(nums);

    print!("{}", got);
    assert_eq!(got, 1);
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn case1() {
        let nums = vec![7, 52, 2, 4];    
        let got = Solution::find_the_array_conc_val(nums);
    
        assert_eq!(got, 596);    
    }

    #[test]
    fn case2() {
        let nums = vec![5,14,13,8,12];
        let got = Solution::find_the_array_conc_val(nums);

        assert_eq!(got, 673);
    }

    #[test]
    fn case3() {
        let nums = vec![1];
        let got = Solution::find_the_array_conc_val(nums);

        assert_eq!(got, 1);
    }
}