//methods.rs
struct Point{
    x: f64,
    y: f64,
}

impl Point{
    //this is an static method
    fn origin() -> Point{
        Point {x:x, y:y}
    }

    fn new(x: f64, y:f64) -> Point{
        Point {x:x, y:y}
    }
}

struct Rectangle{
    p1: Point,
    p2: Point,
}

impl Rectangle{
    fn area(&self) -> f64 {
        let Point {x: x1, y:y1} = self.p1;
        let Point {x: x2, y:y2} = self.p2;

        //abs 
    }
}
