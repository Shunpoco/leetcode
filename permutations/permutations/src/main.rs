use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        let mut counter = HashMap::new();
        for num in &nums {
            *counter.entry(num).or_insert(0) += 1;
        }
        let mut current = vec![];
        let v:Vec<&i32> = counter.keys().cloned().collect();
        println!("{:?}", v);
        Solution::backtrack(&nums, &mut result, &mut current, &mut counter);
        
        result
    }
    
    fn backtrack(nums: &Vec<i32>, result: &mut Vec<Vec<i32>>, current: &mut Vec<i32>, counter: &mut HashMap<&i32, i32>) {
        if current.len() == nums.len() {
            result.push((*current).clone());
            return;
        }
        
        for num in nums {
            if *(counter.get(num).unwrap())-1 >= 0 {
                current.push(*num);
                *counter.get_mut(num).unwrap() -= 1;
                Solution::backtrack(nums, result, current, counter);
                current.pop();
                *counter.get_mut(num).unwrap() += 1;
            }            
        }
        
    }
}


fn main() {
    assert_eq!(
        Solution::permute(vec![1,2,3]),
        vec![
            vec![1,2,3],
            vec![1,3,2],
            vec![2,1,3],
            vec![2,3,1],
            vec![3,1,2],
            vec![3,2,1],
        ]
    );
}
