use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let n = arr.len();
        let mut result = vec![0; n];

        let mut memo = HashMap::new();

        for i in 0..n {
            if !memo.contains_key(&arr[i]) {
                memo.insert(arr[i], vec![i]);
            } else {
                let mut v = memo.get_mut(&arr[i]).unwrap();
                v.push(i);
            }
        }

        let mut keys = Vec::new();
        for &key in memo.keys() {
            keys.push(key);
        }

        keys.sort();

        for i in 0..keys.len() {
            let vals = memo.get(&keys[i]).unwrap();
            for &idx in vals.iter() {
                result[idx] = (i + 1) as i32;
            }
        }

        result
    }
}

fn main() {
    let arr = vec![40, 10, 20, 30];

    let got = Solution::array_rank_transform(arr);

    println!("{:?}", got);
    assert_eq!(got, vec![4, 1, 2, 3]);
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let arr = vec![40, 10, 20, 30];

        let got = Solution::array_rank_transform(arr);

        assert_eq!(got, vec![4, 1, 2, 3]);
    }

    #[test]
    fn case2() {
        let arr = vec![100, 100, 100];

        let got = Solution::array_rank_transform(arr);

        assert_eq!(got, vec![1, 1, 1]);
    }
}