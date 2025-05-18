use std::collections::HashMap;

const MOD: i32 = 1_000_000_007;

struct Solution;

impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;

        let mut valid = HashMap::new();
        let mask_end = 3i32.pow(m as u32);

        for mask in 0..mask_end {
            let mut color = Vec::new();
            let mut mm = mask;

            for _ in 0..m {
                color.push(mm % 3);
                mm /= 3;
            }

            let mut check = true;
            for i in 0..m-1 {
                if color[i] == color[i+1] {
                    check =false;
                    break;
                }
            }

            if check {
                valid.insert(mask, color);
            }
        }

        let mut adjacent = HashMap::new();
        for (&mask1, color1) in &valid {
            for (&mask2, color2) in &valid {
                let mut check = true;
                for i in 0..m {
                    if color1[i] == color2[i] {
                        check = false;
                        break;
                    }
                }

                if check {
                    adjacent.entry(mask1).or_insert(Vec::new()).push(mask2);
                }
            }
        }

        let mut f = HashMap::new();
        for &mask in valid.keys() {
            f.insert(mask, 1);
        }

        for _ in 1..n {
            let mut g = HashMap::new();
            for &mask2 in valid.keys() {
                let mut total = 0;
                if let Some(list) = adjacent.get(&mask2) {
                    for &mask1 in list {
                        total = (total + f.get(&mask1).unwrap_or(&0)) % MOD;
                    }
                }
                g.insert(mask2, total);
            }
            f = g;
        }

        let mut result = 0;
        for &num in f.values() {
            result += num;
            result %= MOD;
        }

        result
    }
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first() {
        let result = Solution::color_the_grid(1, 1);

        assert_eq!(result, 3);
    }

    #[test]
    fn second() {
        let result = Solution::color_the_grid(1, 2);

        assert_eq!(result, 6);
    }
}
