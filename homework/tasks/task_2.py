async def magic_func() -> int:
    return 42


async def fix_this_code() -> int:
    # Используем await для ожидания завершения выполнения magic_func

    result = await magic_func()
    return result
