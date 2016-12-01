import sys
from functools import partial
import curio

READ_SIZE = 20000

async def main(source_port, dest_host, dest_port):
    main_task = await curio.current_task()
    bound_cb = partial(proxy, dest_host, dest_port, main_task)
    await curio.tcp_server("localhost", source_port, bound_cb)

async def proxy(dest_host, dest_port, main_task, source_sock, addr):
    await main_task.cancel()
    dest_sock = await curio.open_connection(dest_host, dest_port)
    async with dest_sock:
        await copy_all(source_sock, dest_sock)

async def copy_all(source_sock, dest_sock):
    while True:
        data = await source_sock.recv(READ_SIZE)
        if not data:  # EOF
            return
        await dest_sock.sendall(data)

if __name__ == "__main__":
    try:
        args = [int(sys.argv[1]), sys.argv[2], int(sys.argv[3])]
    except Exception:
        print("Usage: {} SOURCE_PORT DEST_HOST DEST_PORT".format(__file__))
    else:
        curio.run(main(*args))
