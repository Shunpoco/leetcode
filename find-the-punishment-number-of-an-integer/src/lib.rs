struct Solution;
impl Solution {
    pub fn punishment_number(n: i32) -> i32 {
        let mut result = 0;

        for i in 1..=n {
            let v = i * i;

            if is_punishment(i, v, 0) {
                println!("{:?}", i);
                result += v;
            }
        }

        result
    }
}

fn is_punishment(i: i32, v: i32, cur: i32) -> bool {
    if cur > i {
        return false;
    }

    if v + cur == i {
        return true;
    }

    let mut d = 10;
    while d <= v {
        if is_punishment(i, v /d, cur + v % d) {
            return true
        }

        d *= 10;
    }

    false
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let n = 10;
        let got = Solution::punishment_number(n);

        assert_eq!(182, got);
    }

    #[test]
    fn second() {
        let n = 37;
        let got = Solution::punishment_number(n);

        assert_eq!(1478, got);
    }

    #[test]
    fn third() {
        let n = 1000;
        let got = Solution::punishment_number(n);

        assert_eq!(10804657, got)
    }
}
