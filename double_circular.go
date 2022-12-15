package main

import "fmt"

type Node struct {
	prev  *Node
	value int
	next  *Node
}
type DoubleCircular struct {
	head *Node
	tail *Node
	size int
}

func (dc *DoubleCircular) addLast(val int) {
	newNode := &Node{value: val}
	if dc.size == 0 {
		newNode.next = newNode
		dc.head = newNode
		dc.head.prev = newNode
	} else {
		newNode.next = dc.tail.next
		dc.tail.next = newNode
		newNode.prev = dc.tail
	}
	dc.tail = newNode
	dc.size++
}

func (dc *DoubleCircular) display() {
	ptr := dc.head
	for i := 0; i < dc.size; i++ {
		fmt.Printf("%v--->", ptr)
		ptr = ptr.next
	}
	fmt.Println()
}

func (dc *DoubleCircular) addFirst(val int) {
	newNode := &Node{value: val}
	if dc.size == 0 {
		newNode.next = dc.head
		dc.head = newNode
		dc.head.prev = newNode
	} else {
		dc.tail.next = newNode
		newNode.next = dc.head
		newNode.prev = dc.tail
		dc.head = newNode

	}
	dc.size++
}

func (dc *DoubleCircular) addBetween(val, pos int) {
	newest := &Node{value: val}
	ptr := dc.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	newest.next = ptr.next
	newest.prev = ptr
	ptr.next = newest

	dc.size++
}

func (dc *DoubleCircular) delFirst() {
	if dc.size == 0 {
		fmt.Println("list is empty.")
	} else {
		dc.tail.next = dc.head.next
		dc.head = dc.head.next
		dc.head.prev = dc.tail
	}
	dc.size--
}

func (dc *DoubleCircular) delLast() {
	ptr := dc.head
	if dc.size == 0 {
		fmt.Println("list is empty.")
	} else {
		for i := 0; i < dc.size; i++ {
			ptr = ptr.next
		}
		dc.head.prev = ptr.next
		ptr.next = dc.head
	}
	dc.size--
}

func main() {
	dc := DoubleCircular{}
	dc.addLast(1)
	dc.display()
	dc.addLast(2)
	dc.display()
	dc.addLast(3)
	dc.display()
	dc.addLast(4)
	dc.display()
	// dc.addFirst(0)
	// dc.display()
	// dc.addBetween(33, 3)
	// dc.display()
}
