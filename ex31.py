print("""Ты находишься в темной комнате с двумя дверями.
В какую дверь ты войдешь? 1 или 2???""")

door = input("> ")

if door == "1":
    print("В этой комнате гигантский медведь поедает сырок 'Дружба'.")
    print("Твои действия?")
    print("1. Отберу сырок!")
    print("2. Заору медведю в ухо!")

    bear = input("> ")

    if bear == "1":
        print("Медведь вцепился тебе в лицо. Ты обоосрался!")
    elif bear == "2":
        print("Медведь укусил тебя за ногу. Ты обосрался!")
    else:
        print(f"Прекрасно, это действие {bear} было единственным  верным.")
        print("Медведь убежал прочь, но твои портки подмокли...")

elif door == "2":
    print("Ты смотришь в бесконечную пропасть глаз Ктулху. Твои действия?")
    print("1. Расскажу Ктулху про топи в Сибири.")
    print("2. Потреплю свои желтые пуговки на своей куртке...")
    print("3. Попробую насвистеть песню 'Черный ворон'")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Ты спасся, потому что ктулху превратился в желе.")
        print("Просто прекрасно!")
    else:
        print("Безумие охватило тебя, и ты упал в бассейн...")
        print("Просто прекрасно!")

else:
    print("Безумие охватило тебя, и ты разодрал себе сраку. Отличная работа!")
