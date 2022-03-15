struct Solution;
impl Solution {
    pub fn simplify_path(path: String) -> String {
        let path:Vec<char> = path.chars().collect();
        
        let mut stack = vec![];
        stack.push(path[0]);
        let mut last = path[0];
        let mut idx = 1usize;
        let mut period = 0usize;
        while idx < path.len() {
            let c = path[idx];
            idx += 1;

            if c == '.' {
                if last == '/' {
                    period = 1;
                } else if period == 1 {
                    period = 2;
                } else {
                    period = 0;
                }                
            } else {
                if c == '/' && period > 0 {
                    if period == 1 {
                        stack.pop();
                        last = stack[stack.len()-1];
                    } else {
                        stack.pop();
                        stack.pop();
                        if stack.len() > 1 {
                            stack.pop();
                            while stack.len() > 1 && stack[stack.len()-1] != '/' {
                                stack.pop();
                            }                             
                        }
                        last = stack[stack.len()-1];
                    }
                }
                period = 0;
            }

            if c != '/' || last != c {
                stack.push(c);
            }
            
            last = stack[stack.len()-1];            
        }
        
        if period > 0 {
            if period == 1 {
                stack.pop();
            } else {
                stack.pop();
                stack.pop();
                if stack.len() > 1 {
                    stack.pop();
                    while stack.len() > 1 && stack[stack.len()-1] != '/' {
                        stack.pop();
                    }
                }
            }
        }
        
        while stack.len() > 1 && stack[stack.len()-1] == '/' {
            stack.pop();
        }        
        
        
        stack.iter().collect::<String>()
    }
}


fn main() {
    assert_eq!(Solution::simplify_path("/a//b////c/d//././/..".to_string()), "/a/b/c".to_string());
}
