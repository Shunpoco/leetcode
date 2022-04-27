struct Solution;
impl Solution {
    pub fn exist(mut board: Vec<Vec<char>>, word: String) -> bool {
        let ch: Vec<char> = word.chars().collect();
        let row = board.len() as i32;
        let col = board[0].len() as i32;
        
        for r in 0..row {
            for c in 0..col {
                if Self.e(&mut board, r, c, 0, &ch) {
                    return true;
                }
            }
        } 
        
        false
    }
    
    fn e(self, board: &mut Vec<Vec<char>>, row: i32, col: i32, idx: usize, chars: &Vec<char>) -> bool {
        if idx == chars.len() {
            return true;
        }
        
        if row < 0 || col < 0 || row as usize == board.len() || col as usize == board[0].len() {
            return false;
        }
        
        if board[row as usize][col as usize] != chars[idx] {
            return false;
        }
        
        let c = board[row as usize][col as usize];
        board[row as usize][col as usize] = '!'; 
        
        
        if Self.e(board, row+1, col, idx+1, chars) || Self.e(board, row-1, col, idx+1, chars) || Self.e(board, row, col+1, idx+1, chars) || Self.e(board, row, col-1, idx+1, chars) {
            return true;
        }
        
        board[row as usize][col as usize] = c;
        
        false
    }
}

// 2022-04-27
// impl Solution {
//     pub fn exist(mut board: Vec<Vec<char>>, word: String) -> bool {
//         let mut word: Vec<char> = word.chars().collect();
        
//         for i in 0..board.len() as i32 {
//             for j in 0..board[0].len() as i32 {
//                 if e(i, j, 0, &word, &mut board) {
//                     return true;
//                 }
//             }
//         }
        
//         false
//     }
// }

// fn e(i: i32, j: i32, mut idx: usize, word: &Vec<char>, board: &mut Vec<Vec<char>>) -> bool {
//     if idx == word.len() {
//         return true;
//     }
    
//     if i < 0 || j < 0 || i == board.len() as i32 || j == board[0].len() as i32 || board[i as usize][j as usize] != word[idx] {
//         return false;
//     }

//     let c = board[i as usize][j as usize];
//     board[i as usize][j as usize] = '!';
    
    
//     for &(di, dj) in vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter() {
//         let ni = i + di;
//         let nj = j + dj;
//         if e(ni, nj, idx+1, word, board) {
//             return true;
//         }
//     }
    
//     board[i as usize][j as usize] = c;
    
//     false
// }



fn main() {
    assert_eq!(
        Solution::exist(
            vec![vec!['A','B','C','E'],vec!['S','F','C','S'],vec!['A','D','E','E']],
            "ABCCED".to_string(),
        ),
        true,
    )
}
