package main

import (
	"fmt"
)

var k int

func main() {
	l := []string{"d", "r", "t", "y", "u"}
	for i := 0; i < len(l); i++ {
		fmt.Println(l[i])
		l = append(l, "i did")
		if i == 10 {
			break
		}

	}

}
