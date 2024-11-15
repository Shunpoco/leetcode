struct Solution;
impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut fives = 0;
        let mut tens = 0;
        let mut twenties = 0;

            
        for &bill in bills.iter() {
            if bill == 5 {
                // Just add
                // We don't need to add mut keyword here.
                fives += 1;
            } else if bill == 10 {
                if fives <= 0 {
                    return false;
                }

                fives -= 1;
                tens += 1;
            } else {
                if tens == 0 && fives <= 2 || fives == 0 {
                    return false;
                } else if tens == 0 {
                    fives -= 3;
                } else {
                    tens -= 1;
                    fives -= 1;
                }
            }
        }

        true
    }
}

fn main() {
    let bills = vec![5, 5, 5, 10, 20];

    let got = Solution::lemonade_change(bills);

    println!("{got}");
    assert!(got);
}


#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn case1() {
        let bills = vec![5, 5, 5, 10, 20];

        let got = Solution::lemonade_change(bills);

        assert!(got);
    }

    #[test]
    fn case2() {
        let bills = vec![5, 5, 10, 10, 20];

        let got = Solution::lemonade_change(bills);

        assert!(!got);
    }
}