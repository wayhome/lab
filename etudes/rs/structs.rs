//structs.rs
struct Nil;

struct Pair(int, f64);

struct Point {
    x: f64,
    y: f64,
}

struct Rectangle{
    p1: Point,
    p2: Point
}

fn main(){
    let point: Point = Point {x: 0.3, y: 0.4};
    println!("point coordinates: ({}, {})", point.x, point.y);
    let Point {x: my_x, y: my_y} = point;
    let rectangle = Rectangle {
        p1: Point {x: my_y, y:my_x},
        p2: point
    };

    let nil = Nil;
    let pair = Pair(1, 0.1);
    let Pair(integer, decimal) = pair;

    println!("pair contains {} and {}", integer, decimal);
}
