defmodule MyList do
  def mapsum(list, fun), do: _mapsum(list, 0, fun)

  defp _mapsum([], total, _), do: total
  defp _mapsum([head | tail], total, fun) do
    _mapsum(tail, fun.(head)+total, fun)
  end

  def mapsum2([], _), do: 0
  def mapsum2([head|tail], fun) do
    fun.(head) + mapsum2(tail, fun)
  end


  def max(list) , do: _max(list, 0)

  defp _max([], value), do: value
  defp _max([head | tail], value)  when head > value do
    _max(tail, head)
  end
  defp _max([head | tail], value) do
    _max(tail, value)
  end
end

