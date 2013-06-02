-module(fact).
-export([factorial/1]).

factorial(N) -> factorial(1, N, 1).

factorial(Index, N, Accumulator)  when Index =< N ->
    NewAccumulator = Index * Accumulator,
    factorial(Index+1, N, NewAccumulator);
factorial(Index, N,  Accumulator) when Index > N -> Accumulator.
