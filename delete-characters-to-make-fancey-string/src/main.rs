struct Solution;
impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut result = String::from("");

        let mut count = 0;
        let mut prev: char = ' ';
        for c in s.chars() {
            if c == prev && count < 2 {
                count += 1;
                result.push(c);
            } else if c != prev {
                count = 1;
                prev = c;
                result.push(c);
            } 
        }

        result
    }
}

fn main() {
    let s = String::from("leeetcode");
    let got = Solution::make_fancy_string(s);

    assert!(&got == "leetcode");

    println!("{:?}", got);
}
