import random
import time

LOAD_THRESHOLD = 85
ITERATIONS_COUNT = 10
SLEEP_DURATION = 0.2


class Numbers:

    def task_1_numbers_break(self):
        numbers = list(range(1, 8))
        for n in numbers:
            if n == 5:
                break
            print(n)

    def task_2_strings(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    def task_3_rostics_monitoring(self):
        iteration = 0
        while iteration < ITERATIONS_COUNT:
            current_load = random.randint(0, 100)
            print(f"Итерация {iteration + 1}: Нагрузка {current_load}%")

            if current_load > LOAD_THRESHOLD:
                print(
                    f"⚠️ ВНИМАНИЕ: Высокая нагрузка на Rostics! "
                    f"(> {LOAD_THRESHOLD}%)"
                )

            time.sleep(SLEEP_DURATION)
            iteration += 1


if __name__ == "__main__":
    practice = Numbers()

    print("--- Задача 1 (Числа) ---")
    practice.task_1_numbers_break()

    print("\n--- Задача 2 (Строки) ---")
    practice.task_2_strings()

    print("\n--- Задача 3 (Мониторинг Ростикс) ---")
    practice.task_3_rostics_monitoring()
