"""Версия с глоабальной переменной tracker
"""


def track_execution(func):
    async def wrapper(i):
        tracker = globals()['tracker']
        tracker['order'].append(int(func.__name__[-1]))
        await func(i)

    return wrapper


@track_execution
async def task_1(i):
    if i == 0:
        return
    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


@track_execution
async def task_2(i):
    if i == 0:
        return
    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отслеживаем порядок исполнения корутин при заданном i (например, 42)
    # и возвращаем число, соответствующее ему.
    #
    # Когда поток управления входит в task_1, добавляем к результату цифру 1,
    # а когда он входит в task_2, то добавляем цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212

    global tracker  # глобальная переменная для трекинга очередности
    tracker = {'order': []}
    await task_1(i)
    return int(''.join(map(str, tracker['order'])))


if __name__ == '__main__':
    import asyncio

    async def main():
        result = await coroutines_execution_order(7)
        print(result)

    asyncio.run(main())
