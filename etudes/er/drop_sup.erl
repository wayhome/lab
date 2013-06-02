-module(drop_sup).
-behaviour(supervisor).
-export([start_link/0]).
-export([init/1]).
-define(SERVER, ?MODULE).

%%% convenience method for startup
start_link() ->
    supervisor:start_link({local, ?SERVER}, ?MODULE, []).

%%% supervisor callback
init([]) ->
    RestartStrategy = one_for_one,
    MaxRestarts = 1, % one restart every
    MaxSecondsBetweenRestarts = 5, % five seconds

    SupFlags = {RestartStrategy, MaxRestarts, MaxSecondsBetweenRestarts},

    Restart = permanent,
    Shutdown = 2000,
    Type = worker, % could also be supervisor

    Drop = {otpdrop, {otpdrop, start_link, []},
                   Restart, Shutdown, Type, [otpdrop]},

    {ok, {SupFlags, [Drop]}}.



