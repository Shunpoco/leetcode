
const EQUILATERAL: &'static str = "equilateral";
const ISOSCELES: &'static str = "isosceles";
const SCALENE: &'static str = "scalene";
const NONE: &'static str = "none";

struct Solution;
impl Solution {
    pub fn triangle_type(mut nums: Vec<i32>) -> String {
        if nums.len() != 3 {
            return "".to_string();
        }

        nums.sort();

        if nums[0] + nums[1] <= nums[2] {
            return NONE.to_string();
        }

        if nums[0] == nums[1] && nums[1] == nums[2] {
            EQUILATERAL.to_string()
        } else if nums[0] == nums[1] || nums[1] == nums[2] {
            ISOSCELES.to_string()
        } else {
            SCALENE.to_string()
        }
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let nums = vec![3, 3, 3];

        let result = Solution::triangle_type(nums);

        assert_eq!(result, EQUILATERAL.to_string());
    }

    #[test]
    fn second() {
        let nums = vec![5, 3, 3];
        
        let result = Solution::triangle_type(nums);

        assert_eq!(result, ISOSCELES.to_string());
    }

    #[test]
    fn third() {
        let nums = vec![3, 4, 5];

        let result = Solution::triangle_type(nums);

        assert_eq!(result, SCALENE.to_string());
    }

    #[test]
    fn forth() {
        let nums = vec![8, 4, 2];

        let result = Solution::triangle_type(nums);

        assert_eq!(result, NONE.to_string());
    }

    #[test]
    fn fifth() {
        let nums = vec![8, 4, 4];

        let result = Solution::triangle_type(nums);

        assert_eq!(result, NONE.to_string());
    }
}
