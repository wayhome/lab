defmodule Geom do
  @moduledoc """
  Functions for calculating areas of geometric shapes.
  """
  @vsn 0.1

  @doc """
  Calculates the area of rectangle, given the length and width.
  Returns the production of its arguments. The default value for both
  arguments is 1.
  """
  def area({shape, dim1, dim2}) when dim1>=0 and dim2>=0 do
    case shape do
      :rectangle -> dim1 * dim2
      :triangle ->  dim1 * dim2 / 2.0
      :ellipse -> :math.pi * dim1 * dim2
    end
  end

end
