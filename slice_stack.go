package main

import "fmt"

type stack struct {
	items []int
}

func (s *stack) push(i int) {
	s.items = append(s.items, i)
}

func (s *stack) pop() {
	s.items = s.items[:len(s.items)-1]
}

func main() {
	s := stack{}
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	fmt.Println(s.items)
	s.pop()
	fmt.Println(s.items)
}
