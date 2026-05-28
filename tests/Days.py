def get_day(number):
    match number:
        case 1: return "Понедельник"
        case 2: return "Вторник"
        case 3: return "Среда"
        case 4: return "Четверг"
        case 5: return "Пятница"
        case 6: return "Суббота"
        case 7: return "Воскресенье"
        case _: return "Неверный день"

# цикл для постоянного ввода цифр
while True:
    number = int(input("Введи число от 1 до 7; 0 - для выхода"))
    if number == 0:
        break
    print(get_day(number))