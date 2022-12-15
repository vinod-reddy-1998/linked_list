package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

type LinkedQueue struct {
	head *Node
	tail *Node
	size int
}

func (lq *LinkedQueue) enqueue(val int) {
	newest := &Node{value: val}
	if lq.size == 0 {
		lq.head = newest

	} else {
		lq.tail.next = newest
	}
	lq.tail = newest
	lq.size++
}

func (lq *LinkedQueue) dequeue() {
	if lq.size == 0 {
		fmt.Println("queue is empty..")
	} else {
		fmt.Println("first out is :", lq.head.value)
		lq.head = lq.head.next
		lq.size--
	}

}
func (lq *LinkedQueue) display() {
	ptr := lq.head
	for i := 0; i < lq.size; i++ {
		fmt.Printf("%v-->", ptr.value)
		ptr = ptr.next
	}

}

func main() {
	lq := LinkedQueue{}
	lq.enqueue(1)
	lq.enqueue(2)
	lq.enqueue(3)
	lq.enqueue(4)
	lq.dequeue()
	lq.display()

}
