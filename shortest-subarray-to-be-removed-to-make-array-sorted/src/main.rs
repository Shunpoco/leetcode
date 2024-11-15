struct Solution;
impl Solution {
    pub fn find_length_of_shortest_subarray(arr: Vec<i32>) -> i32 {
        let mut r = arr.len() - 1;

        while r > 0 && arr[r] >= arr[r-1] {
            r -= 1;
        }

        let mut result = r;
        let mut l = 0;

        while l < r && (l == 0 || arr[l-1] <= arr[l]) {
            while r < arr.len() && arr[l] > arr[r] {
                r += 1;
            }

            result = if r - l - 1 < result { r - l - 1 } else { result };
            l += 1;
        }

        result as i32
    }
}

fn main() {
    let arr = vec![1, 2, 3, 10, 4, 2, 3, 5];

    let got = Solution::find_length_of_shortest_subarray(arr);

    assert_eq!(got, 3);

    println!("{}", got);
}


#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn case1() {
        let arr = vec![1, 2, 3, 10, 4, 2, 3, 5];

        let got = Solution::find_length_of_shortest_subarray(arr);

        assert_eq!(got, 3);
    }

    #[test]
    fn case2() {
        let arr = vec![5, 4, 3, 2, 1];

        let got = Solution::find_length_of_shortest_subarray(arr);

        assert_eq!(got, 4);
    }

    #[test]
    fn case3() {
        let arr = vec![1, 2, 3];

        let got = Solution::find_length_of_shortest_subarray(arr);

        assert_eq!(got, 0);
    }
}