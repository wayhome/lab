-module(drop).
-export([fall_velocity/1, drop/0]).

drop() ->
    receive
        {From, Planemo, Distance} ->
            From ! {Planemo, Distance, fall_velocity(Planemo, Distance)},
            drop()
    end.

fall_velocity({Planemo, Distance}) -> fall_velocity(Planemo, Distance).

fall_velocity(Planemo, Distance) when Distance >= 0 ->
    Gravity = case Planemo of
        earth -> 9.8;
        moon ->  1.6;
        mars ->  3.71
    end,

    try math:sqrt(2 * Gravity * Distance) of 
        Result -> Result
    catch
        error:Error -> {error, Error}
    end.
