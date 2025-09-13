use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        let mut vowels_map = HashMap::new();
        let mut consonants_map = HashMap::new();

        for c in s.chars() {
            match c {
                'a' | 'e' | 'i' | 'o' | 'u' => {
                match vowels_map.get_mut(&c) {
                        Some(v) => {
                            *v += 1;
                        },
                        None => {
                            vowels_map.insert(c, 1);
                        },
                    }

                },
                _ => {
                    match consonants_map.get_mut(&c) {
                        Some(v) => {
                            *v += 1;
                        },
                        None => {
                            consonants_map.insert(c, 1);
                        }
                    }
                },
            }
        }

        let mut vowel= 0;
        for (_, v) in vowels_map.into_iter() {
            if v > vowel {
                vowel = v;
            }
        }

        let mut cons = 0;
        for (_, v) in consonants_map.into_iter() {
            if v > cons {
                cons = v;
            }
        }

        vowel + cons
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let s = String::from("successes");
        let got = Solution::max_freq_sum(s);

        assert_eq!(got, 6);
    }

    #[test]
    fn second() {
        let s = String::from("aeiaeia");
        let got = Solution::max_freq_sum(s);

        assert_eq!(got, 3);
    }
}
