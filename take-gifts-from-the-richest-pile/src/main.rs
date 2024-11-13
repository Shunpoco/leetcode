use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    pub fn pick_gifts(gifts: Vec<i32>, k: i32) -> i64 {
        let mut heap = BinaryHeap::new();
        for &num in gifts.iter() {
            heap.push(num);
        }

        for _ in 0..k {
            let v = heap.pop().unwrap();

            heap.push(Solution::get_square_root_floor(v));
        }

        let mut result = 0;
        while heap.len() > 0 {
            let v = heap.pop().unwrap();

            result += v as i64;
        }

        result
    }

    fn get_square_root_floor(num: i32) -> i32 {
        let mut result = 1;

        while result * result < num {
            result += 1;
        }

        if result*result != num {
            result -= 1;
        }

        result
    }
}

fn main() {
    let gifts = vec![25, 64, 9, 4, 100];
    let k = 4;

    let got = Solution::pick_gifts(gifts, k);

    println!("{}", got);
    assert_eq!(got, 29);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let gifts = vec![25, 64, 9, 4, 100];
        let k = 4;

        let got = Solution::pick_gifts(gifts, k);

        assert_eq!(got, 29);
    }

    #[test]
    fn case2() {
        let gifts = vec![1, 1, 1, 1];
        let k = 4;

        let got = Solution::pick_gifts(gifts, k);

        assert_eq!(got, 4);
    }
}