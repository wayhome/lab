%% @author Young King <yanckin@gmail.com> [http://youngking.org]
%% @doc Functions for find gcd of two intergers
%% @copyright 2013 Young King
%% @version 0.1

- module(powers).
- export([raise/2]).

raise(_, 0) -> 1;
raise (X, N) when N > 0 ->
    raise(X, N, 1);
raise(X, N) when N < 0 ->  1.0 / raise(X, -N).

raise(_, 0, Accumulator) -> Accumulator;
raise(X, N, Accumulator) -> raise(X, N-1, X *Accumulator).


