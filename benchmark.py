import secrets
from timeit import timeit

from queuelib.queue import *


def use_queue(queue):
    for _ in range(10**3):
        queue.push(secrets.token_hex(16).encode())
    while len(queue):
        queue.pop()


def test_fifo_disk_queue():
    queue = FifoDiskQueue("fifo-disk")
    use_queue(queue)


def test_fifo_dbm_queue():
    queue = FifoDBMQueue("fifo-dbm")
    use_queue(queue)


def test_lifo_disk_queue():
    queue = LifoDiskQueue("lifo-disk")
    use_queue(queue)


def test_lifo_dbm_queue():
    queue = LifoDBMQueue("lifo-dbm")
    use_queue(queue)


print("fifo disk queue:", timeit(test_fifo_disk_queue, number=10))
print("fifo dbm queue: ", timeit(test_fifo_dbm_queue, number=10))
print("lifo disk queue:", timeit(test_lifo_disk_queue, number=10))
print("lifo dbm queue: ", timeit(test_lifo_dbm_queue, number=10))
