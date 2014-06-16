//clone.rs
// a vanilla unit struct
struct Foo;

// a unit struct that implements the Clone trait
#[deriving(Clone)]
struct Dolly;

fn destroy_string(string: String) {
}

fn main() {
    let string: &'static str = "Hello World";
}
