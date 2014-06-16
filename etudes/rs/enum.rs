// enum.rs
use std::owned::Box;

enum Node{
    // data, [] -> next_node
    Cons(uint, Box<Node>),
    Nil,
}

impl Node{
    fn new() -> Node {
        Nil
    }

    // consume list, and return the same list with a new element appended
    fn append(self, elem: uint) -> Node {
        Cons(elem, box self)
    }

    // return the head of the list
    fn head(&self) -> Option<uint> {
        match *self {
            // head gets copied, copy is rentured wrapped in Some
            Cons(head, _) => Some(head),
            // if the list is empty, return None
            Nil => None,
        }
    }

    fn len(&self) -> uint{
        match *self {
            Cons(_, ref tail) => 1 + tail.len(),
            Nil => 0
        }
    }

    fn tail(self) -> Option<Node> {
        match self{
            Nil => None,
            Cons(_, box tail) => Some(tail),
        }
    }

}


fn main(){
    // linkded list: 3, [] -> 2, [] -> 1, [] -> Nil
    let mut list = Node::new();
    list = list.append(1);
    list = list.append(2);
    list = list.append(3);

    println!("list size {}", list.len());

    loop {
        let head = list.head();

        list = match list.tail() {
            // if list is empty, break this loop
            None => break,
            // unwrap tail
            Some(tail) => {
                // show the list head
                println!("list head: {}", head.unwrap());
                tail
            },
        }
    };

}
