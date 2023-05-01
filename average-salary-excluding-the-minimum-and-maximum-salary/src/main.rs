struct Solution;
impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let mut sum: i32 = salary.iter().sum();
        sum -= salary.iter().max().unwrap() + salary.iter().min().unwrap();

        (sum as f64) / ((salary.len() - 2) as f64)
    }
}

fn main() {
    println!("{}", Solution::average(vec![100, 200, 300]));
}


#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn test_1() {
        let input = vec![4000,3000,1000,2000];
        let output = 2500.00000;

        assert_eq!(Solution::average(input), output);
    }

    #[test]
    fn test_2() {
        let input = vec![1000,2000,3000];
        let output = 2000.00000;

        assert_eq!(Solution::average(input), output);
    }
}
