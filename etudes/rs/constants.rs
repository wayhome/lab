//constants.rs
static LANGUAGE: &'static str = "Rust";
static THREHOLD: int = 10;

fn is_big(n: int) -> bool {
    // access constant in some function
    n > THREHOLD
}

fn main() {
    let n = 16;

    // access constant in the main loop
    println!("This is {}", LANGUAGE);
    println!("The threhold is {}", THREHOLD);
    println!("{} is {}", n, if is_big(n) {"big"} else {"small"});

    if true {
        // string literals are references to read-only memory
        let static_string: &'static str = "In read-only memory";
    }

}
