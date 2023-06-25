package main

const mod = 100_000_000_7

func countRoutes(locations []int, start int, finish int, fuel int) int {
    dp := make([][]int, len(locations))
    for i := 0; i < len(locations); i++ {
        t := make([]int, fuel+1)
        for j := 0; j < len(t); j++ {
            t[j] = -1
        }
        dp[i] = t
    }

    return helper(dp, locations, start, finish, fuel)
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}

func helper(dp [][]int, locations []int, current int, finish int, fuel int) int {
    if fuel < 0 {
        return 0
    }

    if dp[current][fuel] >= 0 {
        return dp[current][fuel]
    }

    var ans int
    if current == finish {
        ans++
    }

    for next := 0; next < len(locations); next++ {
        if current != next {
            ans += helper(dp, locations, next, finish, fuel-abs(locations[current]-locations[next]))
            ans %= mod
        }
    }

    dp[current][fuel] = ans

    return ans
}

