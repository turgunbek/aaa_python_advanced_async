"""Версия без глобальных переменных
"""


from functools import wraps


class ExecutionOrderTracker:
    """Вспомогательный класс для отслеживания очередности
    """
    def __init__(self):
        self.order = []

    def get_execution_order(self):
        return ''.join(map(lambda x: str(x), self.order))


def track_execution(value):
    def decorator(func):
        @wraps(func)
        async def wrapper(tracker, i):
            tracker.order.append(value)
            await func(tracker, i)

        return wrapper
    return decorator


@track_execution(1)
async def task_1(tracker, i):
    if i == 0:
        return
    if i > 5:
        await task_2(tracker, i // 2)
    else:
        await task_2(tracker, i - 1)


@track_execution(2)
async def task_2(tracker, i):
    if i == 0:
        return
    if i % 2 == 0:
        await task_1(tracker, i // 2)
    else:
        await task_2(tracker, i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отслеживаем порядок исполнения корутин при заданном i (например, 42)
    #  и возвращаем число, соответствующее ему.
    #
    # Когда поток управления входит в task_1, добавляем к результату цифру 1,
    # а когда он входит в task_2, то добавляем цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212

    tracker = ExecutionOrderTracker()
    await task_1(tracker, i)

    result = tracker.get_execution_order()
    return int(result)


if __name__ == '__main__':
    import asyncio

    async def main():
        result = await coroutines_execution_order(7)
        print(result)

    asyncio.run(main())
