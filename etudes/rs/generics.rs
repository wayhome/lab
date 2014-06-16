//generics.rs

struct Pair<T> {
    first: T,
    second: T,
}

fn swap<T>(pair: Pair<T>) -> Pair<T> {
    let Pair {first: first, second: second} = pair;
    Pair {first: second, second: first}
}

struct Tuple2<T, U>(T, U);

fn main() {
    let pair_of_chars: Pair<char> = Pair {first: 'a', second: 'b'};
    let pair_of_ints =  Pair{ first: 1, second: 2};
    let tuple: Tuple2<char, int> = Tuple2('R', 2);
    let swapped_pair_of_chars = swap::<char>(pair_of_chars);
    let swapped_pair_of_ints = swap(pair_of_ints);
}
