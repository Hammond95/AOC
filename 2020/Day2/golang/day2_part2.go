package main
	
import (
    "bufio"
    "fmt"
    "os"
	"strings"
	"strconv"
)

func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
	lines, _ := readLines("../input.txt")

	validPswCount := 0
	for _, line := range lines {
		lineSlice := strings.Split(line, ":")

		boundaries := strings.Split(lineSlice[0], " ")[0]
		pos1, _ := strconv.Atoi(string(strings.Split(boundaries, "-")[0]))
		pos2, _ := strconv.Atoi(string(strings.Split(boundaries, "-")[1]))
		
		letter := strings.Split(lineSlice[0], " ")[1]
		password := strings.TrimSpace(lineSlice[1])

		validPos1 := string(password[pos1-1]) == letter
		validPos2 := string(password[pos2-1]) == letter

		if(validPos1 != validPos2){
			validPswCount = validPswCount + 1;
		}
	}

	fmt.Printf("Valid Passwords Count: %d.\n", validPswCount)
}