%% @author Young King <yanckin@gmail.com> [http://youngking.org]
%% @doc Functions for find gcd of two intergers
%% @copyright 2013 Young King
%% @version 0.1

- module(dijkstra).
- export([gcd/2]).

gcd(M, N) -> 
    if
        M == N -> M;
        M > N -> gcd(M-N, N);
        M < N -> gcd(M, N-M)
    end.
