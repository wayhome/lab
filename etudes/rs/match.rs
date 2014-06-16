//match.rs
fn main(){
    let number = 5;
    match number {
        // match single value
        1 => println!("One!"),
        // match server values
        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
        13..19 => println!("A teen"),
        x if x % 2 == 1 =>println!("An odd one"),
        x => println!("{} ain't special", x),
    }

    let pair = (2, 3);
    match pair{
        (x, y) if x==y => println!("These are twins"),
        (x, y) if x + y ==0 => println!("Antimatter, kaboom"),
        (x, _) if x % 2 ==1 => println!("The first is odd"),
        _ => println!("No correlation ... ")
    }

    let big_number = match number {
        0 => 9000,
        x if x < 10 => {
            let y = x * x;
            let z = x * x * x;
            x + y + z
        },
        x => x
    };

   println!("{}", big_number)
}
