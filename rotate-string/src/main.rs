struct Solution;
impl Solution {
    pub fn rotate_string(s: String, goal: String) -> bool {
        let mut chars: Vec<i32> = vec![0; 26];

        for c in s.chars() {
            chars[c as usize - 'a' as usize] += 1;
        }

        for c in goal.chars() {
            let idx = c as usize - 'a' as usize;
            chars[idx] -= 1;
        }

        for &c in chars.iter() {
            if c != 0 {
                return false;
            }
        }

        true
    }
}

fn main() {
    let s = String::from("abcde");
    let goal = String::from("cdeab");

    let got = Solution::rotate_string(s, goal);

    assert!(got);

    print!("{}", got);
}
