%% @author Young King <yanckin@gmail.com> [http://youngking.org]
%% @doc Functions for find gcd of two intergers
%% @copyright 2013 Young King
%% @version 0.1

- module(ask).
- export([line/0]).

line() ->
    Planemo = get_planemo(),
    Distance = get_distance(),
    drop:fall_velocity({Planemo, Distance}).


char_to_planemo(Char) ->
    if
        [Char] == "1" -> earth;
        Char == $2 -> moon;
        Char == 51 -> mars
    end.

get_planemo() ->
    io:format("Where are you?~n"),
    io:format("1. Earth ~n"),
    io:format("2. Earth's Moon~n"),
    io:format("3. Mars ~n"),
    Answer = io:get_line("Which? >"),

    Value = hd(Answer),
    char_to_planemo(Value).

get_distance() ->
    Input = io:get_line("How far? (meters) >"),
    Value = string:strip(Input, right, $\n),
    {Distance, _} = string:to_integer(Value),
    Distance.
