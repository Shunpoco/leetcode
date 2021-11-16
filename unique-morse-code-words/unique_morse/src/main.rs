use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        
        let mut results = vec![];
        
        for word in words {
            let word:Vec<char> = word.chars().collect();
            let mut morse = "".to_string();
            for c in word {
                let m = Solution::morse(c);
                morse = format!("{}{}", morse, m);
            }
            results.push(morse);
        }
        
        results.into_iter().collect::<HashSet<String>>().len() as i32
    }
    
    
    fn morse(c: char) -> String {
        let morses = vec![".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        morses[c as usize - 97].to_string()
    }
}


fn main() {
    assert_eq!(Solution::unique_morse_representations(vec!["gin","zen","gig","msg"].into_iter().map(String::from).collect()), 2)
}
