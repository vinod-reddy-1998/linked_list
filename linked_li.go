package main

import (
	"fmt"
)

type Node struct {
	value int
	next  *Node
}

type LinkedList struct {
	head *Node
	tail *Node
	len  int
}

func (l *LinkedList) Insert(val int) {
	n := Node{}
	n.value = val

	if l.head == nil {
		l.head = &n
	} else {
		l.tail.next = &n
	}
	l.tail = &n
	l.len++
	return
}

func (l *LinkedList) addFirst(val int) {
	newNode := Node{value: val}
	if l.head == nil {
		l.head = &newNode
		l.tail = &newNode
	} else {
		newNode.next = l.head
		l.head = &newNode
	}
	l.len++

}

func (l *LinkedList) insertAny(val, pos int) {
	newNode := &Node{value: val}
	ptr := l.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	newNode.next = ptr.next
	ptr.next = newNode
	l.len++

}

func (l *LinkedList) display() {
	if l.len == 0 {
		fmt.Println("linked list is empty...")
	} else {
		ptr := l.head
		for i := 0; i < l.len; i++ {
			fmt.Printf("%d-->", ptr.value)
			ptr = ptr.next
		}
		fmt.Println()

	}
}

func (l *LinkedList) delFirst() {
	// fmt.Println(l.head)
	// fmt.Println((l.head.next))
	l.head = (l.head.next)
	fmt.Println(l.head)
	l.len--
}
func (l *LinkedList) delAny(pos int) {
	p := l.head
	for i := 1; i < pos-1; i++ {
		p = p.next
	}
	p.next = p.next.next
	l.len--
}

func (l *LinkedList) delLast() {
	p := l.head
	for i := 1; i < l.len-1; i++ {
		p = p.next
		// fmt.Println(p)
	}
	p.next = nil
	l.len--

}

func main() {
	l := LinkedList{}
	l.Insert(78)
	l.Insert(87)
	l.Insert(90)
	l.display()
	// fmt.Println(strings.Repeat("#", 20))
	// l.addFirst(34)
	// l.display()
	// fmt.Println(strings.Repeat("#", 20))
	l.insertAny(33, 2)
	l.display()
	// fmt.Println(strings.Repeat("#", 20))
	// l.delFirst()
	// l.display()
	// fmt.Println(strings.Repeat("#", 20))
	// // l.delAny(3)
	// l.delLast()
	l.display()
	fmt.Println("the length of list is:", l.len)

}
