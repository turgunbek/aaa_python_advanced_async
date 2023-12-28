import asyncio
from typing import Coroutine


async def limit_execution_time(
        coro: Coroutine,
        max_execution_time: float
        ) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить,
    # однако иногда она выполняется слишком долго.
    # Это время ограничиваем переданным на вход количеством секунд.

    try:
        await asyncio.wait_for(coro, timeout=max_execution_time)
    except asyncio.TimeoutError:
        pass  # Обработка случая, когда корутина выполняется слишком долго


async def limit_execution_time_many(
        *coros: Coroutine,
        max_execution_time: float
        ) -> None:
    # Функция эквивалентна limit_execution_time,
    # но корутин на вход приходит несколько.

    tasks = [limit_execution_time(coro, max_execution_time) for coro in coros]
    await asyncio.gather(*tasks)
