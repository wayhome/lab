struct Point{
    x: int,
    y: int,
}

fn main(){
    let point = Point {x:0, y:0};
    let copy_of_x:int = {
        let Point {x:ref ref_to_x, y:_} = point;
        *ref_to_x
    };

    let mut mutable_point = point;

    if true{
        let Point {x:_, y:ref mut mut_ref_to_y} = mutable_point;
        *mut_ref_to_y = 1;
    }

    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);
}
