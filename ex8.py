formatter="{} {} {} {}"

print (formatter.format(1 , 2 , 3 , 4))
print(formatter.format("раз", "два", "три", "четыре"))
print(formatter.format(True ,False ,True ,False))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Спят в конюшне пони,",
    "Начал лес дремать,",
    "Только мальчик Джонни",
    "Не ложится спать!"
    ))