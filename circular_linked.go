package main

import (
	"fmt"
	"strings"
)

type Node struct {
	value int
	next  *Node
}

type CircularLinked struct {
	head *Node
	tail *Node
	len  int
}

func (c *CircularLinked) addLast(val int) {
	newNode := &Node{value: val}
	if c.head == nil {
		newNode.next = newNode
		c.head = newNode

	} else {
		newNode.next = c.tail.next
		c.tail.next = newNode
		// fmt.Println(c.tail.next)
		// fmt.Println(newNode)
	}
	c.tail = newNode
	c.len++
}

func (c *CircularLinked) addFirst(val int) {
	newNode := &Node{value: val}
	if c.len == 0 {
		newNode.next = newNode
		c.head = newNode
	} else {
		c.tail.next = newNode
		newNode.next = c.head
		c.head = newNode
	}
	c.len++
}

func (c *CircularLinked) insertAny(val, pos int) {
	newNode := &Node{value: val}
	ptr := c.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	newNode.next = ptr.next
	ptr.next = newNode
	c.len++
}

func (c *CircularLinked) display() {
	p := c.head
	for i := 0; i < c.len; i++ {
		fmt.Println(p.value)
		p = p.next
	}
}

func (c *CircularLinked) delLast() {
	ptr := c.head
	for i := 0; i < c.len-1; i++ {
		ptr = ptr.next
	}
	ptr.next = c.head
	c.len--
}
func (c *CircularLinked) delFirst() {
	c.tail.next = c.head.next
	c.head = c.head.next
	c.len--
}

func (c *CircularLinked) delAny(pos int) {
	ptr := c.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	ptr.next = ptr.next.next
}

func main() {
	c := CircularLinked{}
	c.addLast(1)
	c.addLast(2)
	c.addLast(3)
	c.addLast(4)
	c.display()
	fmt.Println(strings.Repeat("$", 30))
	c.addFirst(-1)
	c.addFirst(-2)
	c.display()
	fmt.Println(strings.Repeat("//", 30))
	c.insertAny(0, 3)
	c.display()
	fmt.Println(strings.Repeat("*", 30))
	c.delLast()
	c.display()
	fmt.Println(strings.Repeat("#", 30))
	c.delFirst()
	c.display()
	fmt.Println(strings.Repeat("()", 30))
	c.delAny(3)
	c.display()
}
