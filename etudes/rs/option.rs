//option.rs
fn division(dividend: int, divisor: int) -> int {
    if divisor == 0 {
        fail!("division by zero")
    } else {
        dividend / divisor
    }
}

fn checked_division(dividend: int, divisor: int) -> Option<int> {
    if divisor == 0 {
        None
    } else {
        Some(dividend / divisor)
    }
}

fn try_division(dividend: int, divisor: int) {
    match checked_division(dividend, divisor) {
        None => println!("{} / {} failed!", dividend, divisor),
        Some(quotient) => println!("{} / {} = {}", dividend, divisor, quotient)
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    let none: Option<int> = None;
    let optional_float = Some(0.0);

    let unwrapped_float = optional_float.unwrap();
    let runtime_failure = none.unwrap();
}
