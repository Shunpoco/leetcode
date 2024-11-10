struct Solution;
impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let ss: Vec<&str> = sentence.split(" ").collect();

        for i in 0..ss.len() {
            if ss[i].chars().nth(ss[i].len()-1) != ss[(i+1)%ss.len()].chars().nth(0) {
                return false;
            }
        }

        true
    }
}

fn main() {
    let sentence = String::from("leetcode exercises sound delightful");

    let got = Solution::is_circular_sentence(sentence);

    assert!(got);

    print!("{}", got);
}
