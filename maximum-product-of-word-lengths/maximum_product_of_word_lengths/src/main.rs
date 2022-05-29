struct Solution;
impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        let mut result = 0i32;
        for i in 0..words.len()-1 {
            for j in i+1..words.len() {
                if is_not_share(&words[i].chars().collect::<Vec<_>>(), &words[j].chars().collect::<Vec<_>>()) {
                    let t = (words[i].len() * words[j].len()) as i32;
                    if t > result {
                        result = t;
                    }
                }
            }
        }
        
        result
    }
}

fn is_not_share(w1: &Vec<char>, w2: &Vec<char>) -> bool {
    let mut v = vec![0;26];
    
    for &c in w1.iter() {
        v[c as usize - 'a' as usize] += 1;
    }
    for &c in w2.iter() {
        if v[c as usize - 'a' as usize] > 0 {
            return false;
        }
    }
    true
}


fn main() {
    assert_eq!(
        Solution::max_product(
            vec!["abcw","baz","foo","bar","xtfn","abcdef"]
                .iter()
                .map(|s| s.to_string())
                .collect::<Vec<_>>(),
            ),
            16,
        );
}
