use std::collections::VecDeque;

struct Solution;
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let _len_pres: usize = prerequisites.len();
        let (graph, mut indegrees) = Self::build_graph(num_courses as usize, &prerequisites);
        let mut queue: VecDeque<usize> = VecDeque::new();
        
        for (idx, &degree) in indegrees.iter().enumerate() {
            if degree == 0 {
                queue.push_back(idx);
            }
        }
        
        let mut cnt = 0;
        while let Some(cur) = queue.pop_front() {
            cnt += 1;
            if let Some(nxts) = graph.get(cur) {
                for &nxt in nxts {
                    indegrees[nxt] -= 1;
                    if indegrees[nxt] == 0 {
                        queue.push_back(nxt);
                    }
                }
            };
        }
        
        println!("{}, {:?}", cnt, indegrees);
        cnt == num_courses
    }
    
    fn build_graph(n: usize, pres: &Vec<Vec<i32>>) -> (Vec<Vec<usize>>, Vec<i32>) {
        let mut graph: Vec<Vec<usize>> = vec![vec![];n];
        let mut indegrees: Vec<i32> = vec![0;n];
        
        for edge in pres.iter() {
            let ready = edge[0];
            let pre = edge[1];
            
            graph[pre as usize].push(ready as usize);
            indegrees[ready as usize] += 1;
        }
        (graph, indegrees)
    }
}

fn main() {
    assert_eq!(Solution::can_finish(4, vec![vec![1,2], vec![2,3], vec![3,1]]), false);
}
