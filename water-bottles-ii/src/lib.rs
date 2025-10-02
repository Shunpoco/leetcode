struct Solution;
impl Solution {
    pub fn max_bottles_drunk(num_bottles: i32, mut num_exchange: i32) -> i32 {
        let mut result = num_bottles;
        let mut empty = num_bottles;

        while num_exchange <= empty {
            empty -= num_exchange;
            num_exchange += 1;
            result += 1;
            empty += 1;
        }

        result
    }
}   


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let num_bottles = 13;
        let num_exchange = 6;

        let got = Solution::max_bottles_drunk(num_bottles, num_exchange);

        assert_eq!(got, 15);
    }

    #[test]
    fn second() {
        let num_bottles = 10;
        let num_exchange = 3;

        let got = Solution::max_bottles_drunk(num_bottles, num_exchange);

        assert_eq!(got, 13);
    }
}
