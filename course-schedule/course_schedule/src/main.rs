struct Solution;
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let (graph, mut indegrees) = Self.build_graph(num_courses as usize, &prerequisites);
        let mut stack = vec![];
        
        // prevent infinity loop
        for (i, &degree) in indegrees.iter().enumerate() {
            if degree == 0 {
                stack.push(i);
            }
        }
        
        let mut cnt = 0i32;
        
        while let Some(v) = stack.pop() {
            cnt += 1;
            for &p in &graph[v] {
                indegrees[p] -= 1;
                if indegrees[p] == 0 {
                    stack.push(p);
                }
            }
        }
        
        cnt == num_courses
    }
    
    fn build_graph(self, n: usize, pre: &Vec<Vec<i32>>) -> (Vec<Vec<usize>>, Vec<usize>) {
        let mut graph = vec![vec![];n];
        let mut indegrees = vec![0;n];
        
        for p in pre {
            graph[p[1] as usize].push(p[0] as usize);
            indegrees[p[0] as usize] += 1;
        }
        
        (graph, indegrees)
    }
}

fn main() {
    assert_eq!(Solution::can_finish(4, vec![vec![1,2], vec![2,3], vec![3,1]]), false);
}
