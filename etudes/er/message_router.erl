-module(message_router).
-compile(export_all).

start() ->
    spawn(message_router, route_message, []).

stop(RouterPid) ->
    RouterPid ! shutdown.

send_chat_message(RouterPid, Addressee, MessageBody) ->
    RouterPid ! {send_chat_msg, Addressee, MessageBody}.

route_message() ->
    receive
        {send_chat_msg, Addressee, MessageBody}  ->
            Addressee ! {recv_chat_msg, MessageBody},
            route_message();
        {recv_chat_msg, MessageBody} ->
            io:format("Received: ~p~n", [MessageBody]),
            route_message();
        shutdown ->
            io:format("Shutting down~n");
        Oops ->
            io:format("Warning! Received: ~p~n", [Oops]),
            route_message()
    end.
