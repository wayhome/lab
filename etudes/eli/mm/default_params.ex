defmodule Example do

  def func(p1, p2 // 2, p3 // 3, p4) do
    IO.puts inspect [p1, p2, p3, p4]
  end

  def func(p1) do 
      IO.puts inspect [p1]
  end

end

Example.func("a", "b")             # => ["a",2,3,"b"]
Example.func("a", "b", "c")        # => ["a","b",3,"c"]
Example.func("a", "b", "c", "d")   # => ["a","b","c","d"]

