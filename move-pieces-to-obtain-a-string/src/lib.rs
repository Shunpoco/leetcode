struct Solution;
impl Solution {
    pub fn can_change(start: String, target: String) -> bool {
        let mut idx = 0;

        let start: Vec<char> = start.chars().collect();

        for (i, c) in target.chars().enumerate() {
            if c == 'L' {
                if idx == start.len() {
                    return false;
                }

                while idx < start.len() {
                    if start[idx] == 'R' {
                        return false;
                    } else if start[idx] == '_' {
                        idx += 1;
                        if idx == start.len() {
                            return false;
                        }
                    } else {
                        if idx < i {
                            return false;
                        }
                        idx += 1;
                        break;
                    }
                }
            } else if c == 'R' {
                if idx == start.len() {
                    return false;
                } 
                
                while idx < start.len() {
                    if start[idx] == 'L' {
                        return false;
                    } else if start[idx] == '_' {
                        idx += 1;
                        if idx == start.len() {
                            return false;
                        }
                    } else {
                        if idx > i {
                            return false;
                        }
                        idx += 1;
                        break;
                    }    
                }                
            }
        }

        while idx < start.len() {
            if start[idx] != '_' {
                return false;
            }
            idx += 1;
        }

        true
    }
}


#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn case1() {
        let start = String::from("_L__R__R_");
        let target = String::from("L______RR");

        let got = Solution::can_change(start, target);

        assert!(got);
    }

    #[test]
    fn case2() {
        let start = String::from("R_L_");
        let target = String::from("__LR");

        let got = Solution::can_change(start, target);

        assert!(!got);
    }

    #[test]
    fn case3() {
        let start = String::from("_R");
        let target = String::from("R_");

        let got = Solution::can_change(start, target);

        assert!(!got);
    }

    #[test]
    fn case4() {
        let start = String::from("_L__R__R_L");
        let target = String::from("L______RR_");

        let got = Solution::can_change(start, target);

        assert!(!got);
    }

    #[test]
    fn case5() {
        let start = String::from("_");
        let target = String::from("L");

        let got = Solution::can_change(start, target);

        assert!(!got);
    }
}
