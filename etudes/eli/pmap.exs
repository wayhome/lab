defmodule Parallel do
  def pmap(collection, fun) do
    me = self
    collection 
    |> 
    Enum.map(fn (elem) ->
      spawn_link fn -> ( me <- {self, fun.(elem)}) end
             end)
    |>
    Enum.map( fn (pid) ->
      receive do {^pid, result} -> result end
    end)
  end

end

result = Parallel.pmap 1..1000, &1 * &1
IO.puts result
