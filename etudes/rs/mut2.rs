struct Book{
    author: &'static str,
    title: &'static str,
    year: uint,
}

fn borrow_book(book: &Book){
    println!("I borrowed {} {} edithion", book.title, book.year);
}

fn new_edition(book: &mut Book){
    book.year = 2014
}

fn main(){
    let geb = Book {
        author: "Douglas Hofstadter",
        title: "Godel, Escher, Bach",
        year: 1979,
    };

    borrow_book(&geb);
    borrow_book(&geb);

    let mut mutable_geb = geb;
    new_edition(&mut mutable_geb);

    borrow_book(&mutable_geb);
}
