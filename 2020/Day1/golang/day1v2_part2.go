package main
	
import (
    "bufio"
    "fmt"
    "os"
    "strconv"
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

func getSumPair(elements []int, search int, posMap map[int]int, exclude int) (int, int) {
    var num1 int = -1
    var num2 int = -1
    for i, element := range elements {
        if(i == exclude) { continue };
        num2 = search - element
        val, ok := posMap[num2]
        if ok && val != exclude {
            num1 = element
            break
        }
    }

    return num1, num2
}

func main() {
    var search int
    flag.IntVar(&search ,"search", 2020, "search sum integer.")
    flag.Parse()

	lines, _ := readLines("../input.txt")

    var posMap map[int]int
    posMap = make(map[int]int)
    for i, element := range lines {
        posMap[element] = i
    }

    var num1 int = -1
    var num2 int = -1
    var num3 int = -1
    for i, element := range lines {
        subSearch := search - element
        num1, num2 = getSumPair(lines, subSearch, posMap, i)
        if (num1 != -1 && num2 != -1){
            num3 = element
            break
        }
    }

    if (num3 != -1){
        fmt.Printf("Magic Numbers: %d + %d + %d = %d.\n", num1, num2, num3, num1+num2+num3)
        fmt.Printf("The solution is: %d x %d x %d = %d.\n", num1, num2, num3, num1*num2*num3)
    } else {
        fmt.Println("No valid Tris found.")
    }

}