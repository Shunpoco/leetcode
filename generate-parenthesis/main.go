package main
import (
  "fmt"
)
func generateParenthesis(n int) []string {
    if n == 0 {
        return []string{""}
    }
    
    ans := []string{}
    
    for c:=0; c<n; c++ {
        for _, left := range generateParenthesis(c) {
            for _, right := range generateParenthesis(n-1-c) {
                ans = append(ans, fmt.Sprintf("(%s)%s", left, right))
            }
        }
    }
    
    return ans
}
func main() {
    fmt.Println(generateParenthesis(3))
}
