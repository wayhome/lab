// c-like.rs
enum Day {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

impl Day{
    fn mood(&self) {
        println!("{}", match *self{
            Friday => "it's friday!",
            Saturday | Sunday => "weekend :-)",
            _ => "weekday ... "
        })
    } 
}

enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}

fn main() {
    let today = Monday;

    today.mood();

    println!("roses are \\#{:06x}", Red as int);
    println!("violets are \\#{:06x}", Blue as int);
}
