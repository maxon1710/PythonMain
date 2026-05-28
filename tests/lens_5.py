def filter_long_strings(strings: list[str]) -> list[str]:
    # Возвращаем только те строки, где длина len(s) строго больше 5
    return [s for s in strings if len(s) > 5]


# Проверка работы функции
words = ["яблоко", "дом", "программирование", "код", "питон", "автоматизация"]
result = filter_long_strings(words)

print(result)
# Выведет: ['яблоко', 'программирование', 'автоматизация']
