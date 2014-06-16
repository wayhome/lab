fn main(){
    let mut integer = 5;
    if true{
        let ref_to_integer = &integer;
        integer = 4;
    }
    integer = 4;
}
