package main

import "fmt"

type Queue struct {
	items []int
}

func (q *Queue) Enqueue(i int) {
	q.items = append(q.items, i)
}

func (q *Queue) Dequeue() {
	if len(q.items) > 0 {
		q.items = q.items[1:]
	} else {
		fmt.Println("list is empty")
	}

}
func main() {
	q := Queue{}
	q.Enqueue(1)
	q.Enqueue(2)
	q.Enqueue(3)
	q.Enqueue(4)
	fmt.Println(q.items)
	q.Dequeue()
	q.Dequeue()
	q.Dequeue()
	q.Dequeue()
	q.Dequeue()
	fmt.Println(q.items)
}
