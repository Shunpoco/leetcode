struct Solution;
impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut counter = vec![0;101];

        let mut result = vec![];
        for num in nums {
            counter[num as usize] += 1;
            if counter[num as usize] == 2 {
                result.push(num);
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
        let nums = vec![0, 1, 1, 0];
        let got = Solution::get_sneaky_numbers(nums);

        assert_eq!(got, vec![1, 0]);
    }

    #[test]
    fn second() {
        let nums = vec![0, 3, 2, 1, 3, 2];
        let got = Solution::get_sneaky_numbers(nums);

        assert_eq!(got, vec![3, 2]);
    }

    #[test]
    fn third() {
        let nums = vec![7,1,5,4,3,4,6,0,9,5,8,2];
        let got = Solution::get_sneaky_numbers(nums);

        assert_eq!(got, vec![4, 5]);
    }
}
