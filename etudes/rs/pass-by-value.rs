use std::owned::Box;

fn destroy_box(boxed_int: Box<int>){
}

fn main(){
    let boxed_int = box 5;
    destroy_box(boxed_int);
    let invalid_dereference = *boxed_int;
}
