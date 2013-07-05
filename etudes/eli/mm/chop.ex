defmodule Chop do

  def guess(actual, low..high) when actual < div(low+high, 2) do
    pivot = div(low+high, 2)
    IO.puts "Is it #{pivot}"
    guess(actual, low..pivot)
  end

  def guess(actual, low..high) when actual > div(low+high, 2) do
    pivot = div(low+high, 2)
    IO.puts "Is it #{pivot}"
    guess(actual, pivot..high)
  end

  def guess(actual, low..high) when actual == div(low+high, 2) do
    pivot = div(low+high, 2)
    IO.puts "Is it #{pivot}"
    IO.puts pivot
  end
end
