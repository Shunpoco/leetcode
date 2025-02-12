use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut result = -1;

        for &num in nums.iter() {
            let mut v = 0;
            let mut t = num;

            while t > 0 {
                v += t % 10;
                t /= 10;
            }

            match map.get_mut(&v) {
                Some(n2) => {
                    let sum = num + *n2;
                    if sum > result {
                        result = sum
                    }

                    *n2 = if num > *n2 { num } else { *n2 };
                },
                None => {
                    map.insert(v, num);
                },
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let nums = vec![18, 43, 36, 13, 7];
        let got = Solution::maximum_sum(nums);

        assert_eq!(54, got);
    }

    #[test]
    fn two() {
        let nums = vec![10, 12, 19, 14];
        let got = Solution::maximum_sum(nums);

        assert_eq!(-1, got);
    }
}
