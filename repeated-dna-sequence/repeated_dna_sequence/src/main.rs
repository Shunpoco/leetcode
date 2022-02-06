use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        let s:Vec<char> = s.chars().collect();
        let l = s.len();
        if l < 11 {
            return vec![];
        }
        
        let bits = HashMap::from([
            ('A', 0),
            ('C', 1),
            ('G', 2),
            ('T', 3),
        ]);
        let mut memory = HashMap::new();
        let mut result = vec![];
        
        let mut bit = 0i32;
        let bit_mask:i32 = (1<<20)-1;
        
        for i in 0..10 {
            let v = bits.get(&s[i]).unwrap();
            bit = bit << 2 | v;
        }
        *memory.entry(bit).or_insert(0) += 1;

        for i in 10..l {
            let val = bits.get(&s[i]).unwrap();
            bit = ((bit << 2) & bit_mask) | val;
            match memory.get(&bit) {
                Some(v) => {
                    if *v == 1 {
                        let c: String = (&s[i-9..i+1]).iter().collect();
                        result.push(c);
                    }
                },
                None => {},
            }
            *memory.entry(bit).or_insert(0) += 1;
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT".to_string()), vec!["AAAAACCCCC","CCCCCAAAAA"]);
}
