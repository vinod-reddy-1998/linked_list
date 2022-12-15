package main

import "fmt"

type Node struct {
	value int
	next  *Node
}
type LinkedStack struct {
	top  *Node
	size int
}

func (ls *LinkedStack) push(e int) {
	newest := &Node{value: e}
	if ls.size == 0 {
		ls.top = newest
	} else {
		newest.next = ls.top
		ls.top = newest
	}
	ls.size++
}
func (ls *LinkedStack) pop() {
	if ls.size == 0 {
		fmt.Printf("linked stack is empty..")
	} else {
		fmt.Println(ls.top.value)
		ls.top = ls.top.next
	}
	ls.size--
}

func (ls *LinkedStack) display() {
	ptr := ls.top
	for i := 0; i < ls.size; i++ {
		fmt.Printf("%v-->", ptr.value)
		ptr = ptr.next
	}
}

func (ls *LinkedStack) first() {
	if ls.size == 0 {
		fmt.Printf("linked stack is empty..")
	} else {
		fmt.Println(ls.top.value)
	}
}

func main() {
	ls := LinkedStack{}
	ls.push(1)
	ls.push(2)
	ls.push(3)
	ls.display()
	ls.pop()
	ls.display()

}
