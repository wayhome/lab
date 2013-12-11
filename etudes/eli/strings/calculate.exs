defmodule Parse do

    def calculate(expression) do
      {n1, rest} = parse_number(expression)
      {op, rest} = rest |> skip_space |> parse_operator
      {n2, _} = rest |> skip_space |> parse_number
      op.(n1, n2)
    end

    defp parse_number(expression),  do: _parse_number(expression, 0)

    defp _parse_number([digit| tail], value) when digit in '0123456789' do
      _parse_number(tail, value*10 + digit - ?0)
    end
    defp _parse_number(rest, number), do:  {number, rest} 

    defp skip_space([? | rest]), do: skip_space(rest)
    defp skip_space(rest), do: rest


    defp parse_operator([?+| rest]), do: {&1 + &2, rest} 
    defp parse_operator([?-| rest]), do: {&1 - &2, rest} 
    defp parse_operator([?*| rest]), do: {&1 * &2, rest} 
    defp parse_operator([?/| rest]), do: {div(&1, &2), rest} 

end

IO.inspect Parse.calculate('23 + 45')
IO.inspect Parse.calculate('45 / 3')
IO.inspect Parse.calculate('45 * 3')
IO.inspect Parse.calculate('45 - 135')
