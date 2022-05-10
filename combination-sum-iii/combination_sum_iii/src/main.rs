struct Solution;
// impl Solution {
//     pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
//         let mut stack = vec![vec![]];
        
//         let mut output = vec![];
//         while stack.len() > 0 {
//             let cur = stack.pop().unwrap();
//             if cur.len() as i32 == k {
//                 if cur.iter().sum::<i32>() == n {
//                     output.push(cur.clone());
//                 }
//                 continue;
//             }
//             let start = if cur.len() > 0 { cur[cur.len()-1] } else { 0 };
//             for i in start+1..10 {
//                 let mut t = cur.clone();
//                 t.push(i);
//                 stack.push(t);
//             }
//         }
        
//         output
//     }
// }


impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut stack = vec![(vec![], n);1];
        let mut result = vec![];
        
        while stack.len() > 0 {
            let v = stack.pop().unwrap();
            
            if v.0.len() as i32 == k {
                if v.1 == 0 {
                    result.push(v.0.clone());                    
                }
                continue;
            }
            
            let from = if v.0.len() == 0 { 1 } else { v.0[v.0.len()-1]+1 };
            for i in from..10 {
                if v.1 >= i {
                    let mut t = v.0.clone();
                    t.push(i);
                    stack.push((t, v.1-i));
                }
            }
        }
        
        result
    }
}


fn main() {
    assert_eq!(Solution::combination_sum3(3, 7), vec![vec![1,2,4]]);
}
