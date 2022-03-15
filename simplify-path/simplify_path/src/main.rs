struct Solution;
impl Solution {
    pub fn simplify_path(path: String) -> String {
        let path:Vec<&str> = path.split("/").collect();
        let mut stack = vec![];
        stack.push("/".to_string());

        for &s in path.iter() {
            if s == "" || s == "." {
                continue;
            } else if s == ".." {
                if stack.len() > 1 {
                    stack.pop();
                    stack.pop();
                }
            } else {
                stack.push(s.to_string());
                stack.push("/".to_string());
            }
        }
        
        
        while stack.len() > 1 && stack[stack.len()-1] == "/".to_string() {
            stack.pop();
        }
        
        stack.join("")
    }
}

fn main() {
    assert_eq!(Solution::simplify_path("/a//b////c/d//././/..".to_string()), "/a/b/c".to_string());
}
