package main

import (
	"fmt"     // for standard output
	"strings" // for manipulating strings
)

func main() {
    url := "unix:///tmp/redis.sock"
    params := strings.Split(url, "//")
	fmt.Printf("%v \n", params[1])
}
