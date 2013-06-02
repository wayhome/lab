%% @author Young King <yanckin@gmail.com> [http://youngking.org]
%% @doc Functions for find gcd of two intergers
%% @copyright 2013 Young King
%% @version 0.1

-module(pascal).
-export([add_row/1, add_row2/1]).

add_row(Initial) -> add_row(Initial, 0, []).

add_row([], Last, Final) -> 
    io:format("Processing ~w ~w ~w~n", [[],Last, Final]),
    [Last | Final];
add_row([H | T], Last, New) -> 
     io:format("Processing ~w ~w ~w~n", [[H | T], Last, New]) , 
     add_row(T, H, [Last+H | New]).
     


add_row2(Initial) -> add_row2(Initial, 0, []).
add_row2([], Last, Final) -> 
    io:format("Processing ~w ~w ~w~n", [[],Last, Final]),
    Final ++ [Last];
add_row2([H | T], Last, New) -> 
    io:format("Processing ~w ~w ~w~n", [[H | T], Last, New]) , 
     add_row2(T, H, New ++ [Last + H]).
