use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let mut uf = UnionFind::new(n as usize);

        for edge in edges.iter() {
            uf.unite(edge[0] as usize, edge[1] as usize);
        }
        for i in 0..n {
            uf.root(i as usize);
        }

        let mut hm = HashMap::new();
        for &v in uf.parents.iter() {
            if hm.contains_key(&v) {
                let mut c = hm.get_mut(&v).unwrap();
                *c += 1;
            } else {
                hm.insert(v, 1);
            }
        }

        let mut result = 0;
        let mut cur = 0;
        for (_, &count) in hm.iter() {
            result += cur * count;
            cur += count;
        }

        result
    }
}


struct UnionFind {
    parents: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> UnionFind {
        let mut p = vec![0;n];
        for i in 0..n {
            p[i] = i;
        }

        UnionFind { parents: p }
    }

    fn root(&mut self, x: usize) -> usize {
        if self.parents[x] == x {
            x
        } else {
            let v = self.root(self.parents[x]);
            self.parents[x] = v;
            v
        }
    }

    fn unite(&mut self, x: usize, y: usize) {
        let mut rx = self.root(x);
        let mut ry = self.root(y);
        if rx == ry {
            return;
        } else {
            if rx > ry {
                let t = ry;
                ry = rx;
                rx = t;
            }
            self.parents[ry] = rx;
        }
    }
}

fn main() {
    println!("{}", Solution::count_pairs(3, vec![vec![0,1], vec![0,2], vec![1,2]]));
}
