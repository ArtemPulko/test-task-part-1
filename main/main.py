import subprocess
import sys
import os


def run_tests():
    """Запуск всех тестов с pytest"""

    # Команда для запуска pytest
    cmd = [
        "pytest",
        "-v",  # подробный вывод
        "--tb=short",  # короткий формат traceback
        "--color=yes",  # цветной вывод
    ]

    # Добавляем аргументы командной строки
    cmd.extend(sys.argv[1:])

    print("Запуск тестов...")
    print(f"Команда: {' '.join(cmd)}")
    print("-" * 50)

    # Запускаем pytest
    result = subprocess.run(cmd)

    # Возвращаем код возврата
    return result.returncode


if __name__ == "__main__":
    sys.exit(run_tests())