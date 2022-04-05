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

fn main() {
    assert_eq!(
        Solution::exist(
            vec![vec!['A','B','C','E'],vec!['S','F','C','S'],vec!['A','D','E','E']],
            "ABCCED".to_string(),
        ),
        true,
    )
}
