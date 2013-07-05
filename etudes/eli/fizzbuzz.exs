fizzbuzz = function do
   0, 0, _ -> "FizzBuzz"
   0, _, _  -> "Fizz"
   _, 0, _ -> "Buzz"
   _, _, c -> c
end

my_rem = function do
  n -> fizzbuzz.(rem(n, 3), rem(n, 5), n)
end


Enum.map 10..17, fn(num) -> IO.puts my_rem.(num) end

prefix = fn pre -> ( fn name -> "#{pre} #{name}" end) end

mrs = prefix.("Mrs")
IO.puts mrs.("Smith")
IO.puts prefix.("Elixir").("Rocks")

