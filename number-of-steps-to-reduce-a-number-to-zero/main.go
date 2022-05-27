package main

func numberOfSteps(num int) int {
    counter := 0
    for num > 0 {
        switch {
        case num%2 == 0:
            counter++
        case num == 1:
            counter++
        default:
            counter += 2
        }
        num /= 2
    }
    
    return counter
}
