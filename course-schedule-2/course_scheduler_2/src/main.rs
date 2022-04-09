use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut paths = HashMap::new();
        for pre in prerequisites {
            paths.entry(pre[1]).or_insert(vec![]);
            paths.get_mut(&pre[1]).unwrap().push(pre[0]);
        }
        let mut access = vec![0;num_courses as usize];
        let mut stack = vec![];
        let mut is_possible = true;
        
        for i in 0..num_courses {
            if access[i as usize] == 0 {
                is_possible &= dfs(i, &paths, &mut access, &mut stack);
            }
        }
        
        if is_possible {
            stack.reverse();
            return stack;
        } else {
            return vec![];
        }
    }
}

fn dfs(idx: i32, paths: &HashMap<i32, Vec<i32>>, access: &mut Vec<i32>, stack: &mut Vec<i32>) -> bool {
    access[idx as usize] = 1;
    
    let mut is_possible = true;
    
    match paths.get(&idx) {
        None => {},
        Some(path) => {
            for &p in path {
                if access[p as usize] == 1 {
                    is_possible &= false;
                } else if access[p as usize] == 0 {
                    is_possible &= dfs(p, paths, access, stack);
                }
            }
        },
    }
    
    
    // println!("{} {} {:?}", idx, is_possible, stack);
    
    access[idx as usize] = 2;
    stack.push(idx);
    
    is_possible
}

fn main() {
    assert_eq!(Solution::find_order(2, vec![vec![1,0], vec![0,1]]), vec![]);
}
