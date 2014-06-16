// trait.rs
struct Dog {
    name: String,
}

struct Sheep {
    naked: bool,
    name: String,
}

// traits are collections of methods
trait Animal {
    // static method, Self refers to the implementor type
    fn new(name: String) -> Self;

    //instance methods, only signatures
    fn name<'a>(&'a self) -> &'a str;
    fn noise(&self) -> &'static str;

    // trait can provide method definitions
    fn talk(&self) {
        // trait method can access methods available in the same trait
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Animal for Dog {
    fn new(name: String) -> Dog{
        Dog { name: name}
    }

    fn name<'a>(&'a self) -> &'a str{
        self.name.as_slice()
    }

    fn noise(&self) -> &'static str{
        "woof"
    }
}

impl Dog {
    fn wag_tail(&self) {
        // struct methods can access trait methods
        println!("{} wags tail", self.name());
    }
}


impl Animal for Sheep {
    fn new(name: String) -> Sheep {
        Sheep {name: name, naked: false}
    }

    fn name<'a>(&'a self) -> &'a str{
        self.name.as_slice()
    }

    fn noise(&self) -> &'static str{
        if self.is_naked() {
            "baaah!"
        } else{
            "baaaaaaaah!"
        }
    }
}

impl Sheep {
    fn is_naked(&self) -> bool{
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            println!("{} is already naked!", self.name());
        } else {
            println!("{} gets a haircut", self.name());
            self.talk();
            self.naked = true;
        }
    }
}

fn main() {
    let mut dolly: Sheep = Animal::new(String::from_str("Dolly"));
    let spike: Dog = Animal::new(String::from_str("Spike"));

    spike.wag_tail();
    dolly.shear();

    // dolly and spike can be borrowed as &Animal
    let animals: [&Animal, ..2] = [&spike as &Animal, &dolly as &Animal];

    animals[0].talk();
    animals[1].talk();
}
