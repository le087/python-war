the_count = [1, 2, 3, 4, 5]
fruits = ["яблоко", "апельсин", "персик", "абрикос"]
change = [1, "чирик", 2, "полтос", 3, "сотня"]

# цикл for перевого типа обрабатывает список
for number in the_count:
    print(f"Счетчик: {number}")

# то же, что и выше
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# так же можно обрабатывать смешанные списки
# Обратите внимание, что используются символы {}, так как не известен 
# тип значения
for i in change:
    print(f"Я получил {i}")

# так же мы можем создавать списки, начнем с пустого
elements = []

# Затем используется функция range{} для ограничения диапазона
for i in range(3,6):
    print(f"Добавление {i} в список.")
    # append  - функция для добавления элементов в список
    elements.append(i)

# теперь мы их выводим
for i in elements:
    print(f"Номер элемента: {i}")
