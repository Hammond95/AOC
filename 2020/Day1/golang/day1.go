package main
	
import (
    "bufio"
    "fmt"
    //"io"
    //"io/ioutil"
    "os"
    "strconv"
    "sort"
    "flag"
)

func readLines(path string) ([]int, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []int
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        convertedLine, _ := strconv.Atoi(scanner.Text())
        lines = append(lines, convertedLine)
    }
    return lines, scanner.Err()
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func getSumPair(elements []int, search int) (int, int) {
    size := len(elements)
    fmt.Printf("size = %d\n", size)
    pairedPosFirst := -1
    pairedPosSecond := -1
    for i, element := range elements {
        fmt.Printf("#%d %d\n", i, element)
        paired := search - element
        pivot := size/2
        upperBound := size-1
        lowerBound := i
        stayIn := true
        for (stayIn && (upperBound-lowerBound > 1)) {
            if (elements[pivot] == paired){
                stayIn = false
                pairedPosFirst = i
                pairedPosSecond = pivot
            } else if (elements[pivot] < paired) {
                lowerBound = pivot
                pivot = (pivot + upperBound)/2
            } else {
                upperBound = pivot
                pivot = (lowerBound + pivot)/2
            }
            fmt.Printf("pivot = %d, lb = %d, ub = %d\n", pivot, lowerBound, upperBound)
        }
        if (pairedPosSecond != -1){ break }
        fmt.Printf("#%d %d\n", i, element)
    }

    if (pairedPosSecond != -1){
        return elements[pairedPosFirst], elements[pairedPosSecond]
    } else {
        return -1, -1
    }
}

func main() {
    var search int
    flag.IntVar(&search ,"search", 2020, "search sum integer.")
    flag.Parse()

	lines, _ := readLines("../input.txt")
    sort.Ints(lines)

    num1, num2 := getSumPair(lines, search)

    if (num1 != -1 && num2 != -1){
        fmt.Print("\n\n")
        fmt.Printf("Magic Numbers: %d + %d = %d.\n", num1, num2, num1+num2)
        fmt.Printf("The solution is: %d x %d = %d.\n", num1, num2, num1*num2)
    } else {
        fmt.Println("No valid Pair found.")
    }


}