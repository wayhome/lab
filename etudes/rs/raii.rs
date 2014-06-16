fn create_box(){
    let function_box = box 3;
}

fn main(){
    let boxed_int = box 5;
    if true{
        let short_lived_box = box 4;
    }
    for _ in range(0, 1_000){
        create_box();
    }
}
