package main

import (
    "fmt"
    "os"
    "log"
    "bufio"
    "math"
    "strconv"
)

func main() {
    file, err := os.Open("../input/day1.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    sum := 0
    for scanner.Scan() {
        i1, err := strconv.Atoi(scanner.Text())
        if err == nil {
            sum += fuelRecursion(i1, 0)
        }

    }
    fmt.Println(sum)
}

func fuelRecursion(i int, currentSum int) int {
    computed := compute(i)
    if computed <= 0 {
        return currentSum
    }
    // fmt.Printf("computed %d, current sum: %d\n", computed, currentSum)
    currentSum += computed
    return fuelRecursion(computed, currentSum)
}
func compute(i int) int {
	return int(math.Floor(float64(i) / 3) - 2)
}