struct Solution;

impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut result = 0;

        for i in 1..=n {
            for j in 1..=n {
                for k in j..=n {
                    if i*i + j*j == k*k {
                        result += 1;
                    }
                }
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
        let n = 5;
        let result = Solution::count_triples(n);

        assert_eq!(result, 2);
    }

    #[test]
    fn second() {
        let n = 10;
        let result = Solution::count_triples(n);

        assert_eq!(result, 4);
    }
}
