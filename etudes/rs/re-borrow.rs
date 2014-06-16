struct Point {
    x: int,
    y: int,
    z: int,
}

fn main(){
    let mut point = Point { x:0, y:0, z:0};
    if true{
        let borrowed_point = &point;
        let another_borrow = &point;

        println!("Point has coordinates: ({}, {}, {})", 
                 borrowed_point.x,
                 another_borrow.y,
                 point.z);
    }

    if true{
        let mutable_borrow = &mut point;
        mutable_borrow.x = 5;
        let copied_point = point;
    }

    println!("Point now has coordinates:({}, {}, {})",point.x,
    point.y, point.z);
}

