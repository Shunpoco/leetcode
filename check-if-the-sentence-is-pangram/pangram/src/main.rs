struct Solution {}

impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let start = 97usize; // a is 97 in UTF-8
        let noa = 26usize; // number of alphabets
        let sentence: Vec<char> = sentence.chars().collect();
        if sentence.len() < noa {
            return false;
        }
        
        let mut v = vec![0usize; noa];
        
        for c in sentence {
            v[(c as usize)-start] = 1;
        }
        
        
        v.iter().sum::<usize>() == noa
    }
}


fn main() {
    assert_eq!(Solution::check_if_pangram("thequickbrownfoxjumpsoverthelazydog".to_string()), true);
}
