%% @author Young King <yanckin@gmail.com> [http://youngking.org]
%% @doc Functions for calculatings of geometric shapes
%% @copyright 2013 Young King
%% @version 0.1

-module(geom).
-export([area/1]).

%% @doc Caclcuates the area of a shape, given the tuple containing shape
%% and two of the dimensions. 

- spec(area({atom(), number(), number()}) -> number() ).

area({Shape, L, W}) -> area(Shape, L, W).


%% @doc Caclcuates the area of a shape, given the shape
%% and two of the dimensions. 

area(Shape, A, B) when A>=0, B>=0 ->
    Ratio = case Shape of 
        rectangle -> 1.0;
        triangle -> 0.5;
        ellipse -> math:pi()
    end,

    Ratio * A * B.
