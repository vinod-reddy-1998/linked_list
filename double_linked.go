package main

import (
	"fmt"
	"strings"
)

type Node struct {
	value int
	next  *Node
	prev  *Node
}

type DoubleLinked struct {
	head *Node
	tail *Node
	len  int
}

func (d *DoubleLinked) addLast(val int) {
	newNode := &Node{value: val}
	if d.len == 0 {
		d.head = newNode
		d.head.prev = nil
	} else {
		d.tail.next = newNode
		newNode.prev = d.tail
	}
	d.tail = newNode
	d.len++
}

func (d *DoubleLinked) display() {
	ptr := d.head
	for i := 0; i < d.len; i++ {
		fmt.Println(ptr.value)
		ptr = ptr.next
	}
}

func (d *DoubleLinked) addFirst(val int) {
	node := &Node{value: val}
	if d.len == 0 {
		d.head = node
	} else {
		node.next = d.head
		d.head.prev = node
		d.head = node
	}
	d.len++
}

func (d *DoubleLinked) insertAny(val, pos int) {
	node := &Node{value: val}
	ptr := d.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	node.prev = ptr
	node.next = ptr.next
	ptr.next = node
	d.len++
}

func (d *DoubleLinked) delFirst() {
	if d.len == 0 {
		fmt.Println("list is empty")
	} else {
		d.head = d.head.next
		d.head.prev = nil
	}
	d.len--
}
func (d *DoubleLinked) delLast() {
	ptr := d.head
	for i := 1; i < d.len; i++ {
		ptr = ptr.next
	}
	ptr.next = nil
	fmt.Println(ptr)
	d.len--
}
func (d *DoubleLinked) delAny(pos int) {
	ptr := d.head
	for i := 1; i < pos-1; i++ {
		ptr = ptr.next
	}
	ptr.next = ptr.next.next
	ptr.next.prev = ptr
	d.len--
}

func main() {
	d := DoubleLinked{}
	d.addLast(1)
	d.addLast(2)
	d.addLast(3)
	d.addLast(4)
	d.display()
	fmt.Println(strings.Repeat("$", 30))
	d.addFirst(0)
	d.display()
	fmt.Println(strings.Repeat("$", 30))
	d.delFirst()
	d.display()
	fmt.Println(strings.Repeat("$", 30))
	d.insertAny(99, 3)
	d.delLast()
	d.display()
	fmt.Println(strings.Repeat("$", 30))
	d.delAny(3)
	d.display()
}
