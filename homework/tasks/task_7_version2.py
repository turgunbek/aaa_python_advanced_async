import abc
import asyncio


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model

    async def handle_request(self) -> None:
        # Модель выполняет некий тяжёлый код (в файле тестов),
        # добились его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request
        # не слишком сильно отличается от времени исполнения нескольких таких
        # корутин, запущенных конкурентно.

        # Получение текущего цикла событий (event loop) для текущего потока
        loop = asyncio.get_event_loop()

        # Запуск синхронной функции self._model.compute в отдельном
        # потоке с помощью run_in_executor. Здесь None 1м аргументом означает
        # использование дефолтного ThreadPoolExecutor
        task = loop.run_in_executor(None, self._model.compute)
        # run_in_executor возвращает объект asyncio.Future,
        # который затем можно ожидать в асинхронном коде

        # Ожидание завершения задачи
        await task
