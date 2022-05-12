use std::collections::HashMap;

struct Solution;
// 2022/05/12
impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        let mut memory = vec![0;21];
        for &num in nums.iter() {
            memory[(num+10) as usize] += 1;
        }
        
        // println!("{:?}", memory);
        
        backtrack(&mut vec![], nums.len(), &mut result, &mut memory);
        
        result
    }
}

fn backtrack(t: &mut Vec<i32>, n: usize, result: &mut Vec<Vec<i32>>, memory: &mut Vec<usize>) {
    if t.len() == n {
        result.push(t.clone());
        return;
    }
    
    for i in 0..memory.len() {
        if memory[i] > 0 {
            memory[i] -= 1;
            t.push(i as i32 - 10);
            backtrack(t, n, result, memory);
            t.pop();
            memory[i] += 1;
        }
    }
}


// Backtrack
// impl Solution {
//     pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
//         let l = nums.len();
//         let mut counter = HashMap::new();
//         for num in &nums {
//             *counter.entry(num).or_insert(0) += 1;
//         }
//         let keys:Vec<&i32> = counter.keys().cloned().collect();
//         let mut result = vec![];
//         Solution::backtrack(l, &keys, &mut result, &mut vec![], &mut counter);
        
//         result
//     }
    
//     fn backtrack(length: usize, nums: &Vec<&i32>, result: &mut Vec<Vec<i32>>, current: &mut Vec<i32>, counter: &mut HashMap<&i32, i32>) {
//         if length == current.len() {
//             result.push((*current).clone());
//             return;
//         }
        
//         for num in nums {
//             if *counter.get(*num).unwrap() -1 >= 0 {
//                 *counter.get_mut(*num).unwrap() -= 1;
//                 current.push(**num);
//                 Solution::backtrack(length, nums, result, current, counter);
//                 current.pop();
//                 *counter.get_mut(*num).unwrap() += 1;
//             }
//         }
//     }
// }



// impl Solution {
//     pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
//         let mut nums = nums;
//         nums.sort();
//         let l = nums.len();
        
//         let mut counter = vec![0;21];
//         for num in &nums {
//             counter[(num+10) as usize] += 1;
//         }
        
//         let mut stack = vec![(vec![], counter)];
//         let mut result = vec![];
                
//         while stack.len() > 0 {
//             let vs = stack.pop().unwrap();
//             let now = vs.0;
//             let cur_counter = vs.1;
            
//             if now.len() == l {
//                 result.push(now);
//                 continue;
//             }
            
//             for i in 0..l {
//                 let num = nums[i];
                
//                 if (i == 0 || nums[i-1] != num) && cur_counter[(num+10) as usize] > 0 {
//                     let mut t_now = now.clone();
//                     t_now.push(num);
//                     let mut t_cur_counter = cur_counter.clone();
//                     t_cur_counter[(num+10) as usize] -= 1;
                    
//                     stack.push((t_now, t_cur_counter));
//                 }
//             }
            
//         }
        
//         result
//     }
// }

fn main() {
    assert_eq!(Solution::permute_unique(vec![1,1,2]), vec![vec![1,1,2], vec![1,2,1], vec![2,1,1]]);
}
