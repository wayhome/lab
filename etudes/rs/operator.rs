// operator.rs
struct Foo;
struct Bar;

#[deriving(Show)]
struct FooBar;

#[deriving(Show)]
struct BarFoo;

impl Add<Bar, FooBar> for Foo{
    fn add(&self, rhs: &Bar) -> FooBar {
        println!("> Foo.add(&Bar) was called");
        FooBar
    }
}

impl Add<Foo, BarFoo> for Bar{
    fn add(&self, rhs: &Foo) -> BarFoo {
        println!("> Bar.add(&Foo) was called");
        BarFoo
    }
}

fn main(){
    println!("Foo + Bar = {}", Foo + Bar);
    println!("Bar + Foo = {}", Bar + Foo);

}
