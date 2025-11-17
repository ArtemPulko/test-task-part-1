import subprocess
import sys
import os


def run_tests():
    """Запуск всех тестов с pytest"""

    cmd = [
        "pytest",
        "-v",
        "--tb=short",
        "--color=yes",
    ]

    cmd.extend(sys.argv[1:])

    print("Запуск тестов...")
    print(f"Команда: {' '.join(cmd)}")
    print("-" * 50)

    result = subprocess.run(cmd)

    return result.returncode

if __name__ == "__main__":
    sys.exit(run_tests())