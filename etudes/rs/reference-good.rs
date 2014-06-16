struct Book{
    //`String` is a heap allocated string
    title: String,
    author: String,
    year: uint,
}

fn get_title<'a >(book: &'a Book) -> &'a str {
    // as_slice will return a reference to the string (&str)
    book.title.as_slice()
}

fn main(){
    let geb = Book{
        author: String::from_str("Douglas Hofstadter"),
        title: String::from_str("Godel, Escher, Bach"),
        year: 1979,
    };

    let title: &str = get_title(&geb);

    println!("I just read {}", title);
}
