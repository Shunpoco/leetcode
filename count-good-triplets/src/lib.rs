struct Solution;

impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let mut result = 0;

        for i in 0..arr.len()-2 {
            for j in i+1..arr.len()-1 {
                for k in j+1..arr.len() {
                    if (arr[i]-arr[j]).abs() <= a && (arr[j]-arr[k]).abs() <= b && (arr[i]-arr[k]).abs() <= c {
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
        let arr = vec![3, 0, 1, 1, 9, 7];
        let a = 7;
        let b = 2;
        let c = 3;

        let result = Solution::count_good_triplets(arr, a, b, c);
        assert_eq!(result, 4);
    }

    #[test]
    fn second() {
        let arr = vec![1, 1, 2, 2, 3];
        let a = 0;
        let b = 0;
        let c = 1;

        let result = Solution::count_good_triplets(arr, a, b, c);
        assert_eq!(result, 0);
    }
}
