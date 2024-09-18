from queue import PriorityQueue, Empty
from loguru import logger


class Task:
    def __init__(self, fn, args=None):
        self._fn = fn
        self._args = args or ()

    def exec(self):
        self._fn(*self._args, delay=False)

    def __lt__(self, o):
        return True


class MemoryPriorityQueue:

    def __init__(
            self,
            max_size: int = 0
    ) -> None:
        self.queue = PriorityQueue(max_size)

    def len(self) -> int:
        return self.queue.qsize()

    def push_batch(self, tasks) -> None:
        for task in tasks:
            self.push_task(task)

    def push_task(self, task: tuple, priority: int = 0) -> None:
        self.queue.put((priority, task))

    def push(self, fn: callable, args: tuple = None, priority: int = 0) -> None:
        self.queue.put((priority, Task(fn, args)))

    def pop(self):
        try:
            score, task = self.queue.get_nowait()
            return task
        except Empty:
            pass

    def exec(self):
        for _ in range(len(self)):
            logger.info("---start-queue-task---")
            score, task = self.queue.get_nowait()
            task.exec()

    def __len__(self):
        return self.queue.qsize()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            score, task = self.queue.get_nowait()
            return task
        except Empty:
            raise StopIteration


if __name__ == '__main__':
    def test(*args):
        return args


    q = MemoryPriorityQueue()
    q.push(test, (111, 222), 3)
    for func, func_args in q:
        print(func(*func_args))
