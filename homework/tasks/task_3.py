import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Нужно выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'

    # Используем asyncio.gather для выполнения всех корутин
    results = await asyncio.gather(*coros)

    # Сортируем результаты по полю number
    sorted_results = sorted(results, key=lambda ticket: ticket.number)

    # Возвращаем строку, состоящую из склеенных полей key
    return ''.join(ticket.key for ticket in sorted_results)
