defmodule MyString do
    def printable_ascii(str), do: Enum.all?(str, &1 in ? ..?~)
end

IO.puts MyString.printable_ascii('abcdef')
IO.inspect MyString.printable_ascii('∂x/∂y')
