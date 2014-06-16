use std::owned::Box;

fn main(){
    let x = 5;
    let y = x;
    println!("x is {}, and y is {}", x, y);
    let a = box 5;
    let b = a;
    println!("{} can not be used", a);
}
